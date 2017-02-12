import argparse, json
import matplotlib.pyplot as plt
import httpagentparser
import re

parser = argparse.ArgumentParser()
parser.add_argument("-u",
                    help="input user id")
parser.add_argument("-d",
                    help="input document id")
parser.add_argument("-t", help = "input task id")
parser.add_argument("-g", 
                    help = "loads Graphical User Interface")
parser.add_argument("-f", 
                    help = "loads file")                    
args = vars(parser.parse_args())
user_id = args['u']
doc_id = args['d']
task_id = args['t']
GUI = args['g']
file = args['f']

#perform task2a
def task2a(doc_id):
    result = get_countries(doc_id, search(content, 'subject_doc_id', doc_id))
    return histogram(result, "task2a")
    print(result)
    
#perform task2b    
def task2b(doc_id):
    result = get_continents(doc_id, search(content, 'subject_doc_id', doc_id))
    return histogram(result, "task2b")
    print(result)
    
#perform task3a    
def task3a():
    result = browser_data_3a(content)
    return histogram(result, "task3a")
    print(result)
    
#perform task3b
def task3b():
    result = clean_browser_data(content)
    return histogram(result, "task3b")
    print(result)

#perform task4
def task4():
    result = users_top10(content)
    text = ""
    text += "Top 10 Users\n"
    print("Top 10 Users")
    for i in range(len(result)):
        print(i + 1, result[i])
        text += '{0} {1}\n'.format(i + 1, result[i])
    return text
        
#perform task5a        
def task5a(doc_id):
    result = all_users(search(content, "subject_doc_id", doc_id))
    text = ""
    text += "All Viewers of {} Document\n".format(doc_id)
    print("All Viewers of ", doc_id, "Document")
    for i in range(len(result)):
        print(i + 1, result[i])
        text += '{0} {1}\n'.format(i + 1, result[i])
    return text
        
#perform task5b        
def task5b(visitor_uuid):
    result = all_docs(search(content, "visitor_uuid", visitor_uuid))
    print("All Documents viewed by", visitor_uuid)
    text = ""
    text += "All Documents viewed by {}\n".format(visitor_uuid)
    for i in range(len(result)):
        print(i + 1, result[i])
        text += "{0} {1}\n".format(i+1, result[i])
    return text
        
#perform task5c
def task5c(doc_id, visitor_uuid, sorting=None):
    users_read = []
    if doc_id is not None:
        d = search(content, "subject_doc_id", doc_id)
        u = all_users(d)
        if visitor_uuid in u:
            for i in u:
                if i is not visitor_uuid:
                    u2 = search(content, "visitor_uuid", i)
                    users_read.append(
                            all_docs(search(docs_not_read(u2, "subject_doc_id", doc_id), "event_type", "read")))
                docs = dict()
            for i in users_read:
                for j in i:
                    if j is not None:
                        if j not in docs.keys():
                            docs.update({j: 1})
                        else:
                            docs[j] += 1
            if sorting is not None:
                result = sorting(docs)
                print(result)
            else:
                result = docs
                for i in result.keys():
                    print(i, result[i])
        else:
            result = []
            print("Please Enter a Valid User ID")
    else:
        result = []
        print("Please Enter a Valid Document ID")
    return result
    print(result)
    

#task
def sort_readership(content):
    result = dict()
    for i in content.keys():
        temp = search(content, "subject_doc_id", i)
        for j in temp:
            if j.get("event_readtime") is not None:
                if i not in result:
                    result.update({i: j.get("event_readtime")})
                else:
                    result[i] += j.get("event_readtime")
        print(result)
        return sort_number(result)

def sort_number(content):
    if len(content) < 11:
        return sorted(content.keys(), reverse=True, key=content.__getitem__)
    else:
        return sorted(content.keys(), reverse=True, key=content.__getitem__)[:10]

#draws histogram from tasks
def histogram(result, title):
    length = len(result)
    plt.close('all')
    plt.figure()
    plt.bar(range(length), list(result.values()), align = 'center')
    plt.xticks(range(length), list(result.keys()), rotation=45)
    plt.title(title)
    return plt.gcf()
        
#an initial filteraion of the data      
def search(content, search_query, key_value):
    query = []
    for v in content:
        try:
            if v.get(search_query) == key_value:
                query.append(v)
        except:
            pass
    return query 

#function to get all users from visitor uuid 
def all_users(content):
    users = []
    for i in content:
        if i.get("visitor_uuid") not in users:
            users.append(i.get("visitor_uuid"))
    return users

def all_gui_users():
    users = []
    for i in content:
        if i.get("visitor_uuid") not in users:
            users.append(i.get("visitor_uuid"))
    return users

#function to get all documents from doc id        
def all_docs(content):
    docs = []
    for i in content:
        if i.get("subject_doc_id") not in docs:
            docs.append(i.get("subject_doc_id"))
    return docs
    
#function to get all documents from doc id        
def all_gui_documents():
    docs = []
    for i in content:
        if i.get("subject_doc_id") not in docs:
            docs.append(i.get("subject_doc_id"))
    return docs
    
#function filtering documents not read by a user    
def docs_not_read(data, filter_key, value):
    results = []
    for i in data:
        if not i.get(filter_key) == value:
            results.append(i)
    return results
        
#function that returns the top 10 users                
def users_top10(data):
    count = dict()
    users = all_users(data)
    for i in users:
        count.update({i: 0})
    for j in data:
        if not j.get("event_readtime") is None:
            count[j["visitor_uuid"]] += j.get("event_readtime")
    results = sorted(count, key=count.get, reverse=True)
    results = results[:10]
    return results
        
#function that returns the data of the browsers used to access documents       
def browser_data_3a(data):
    web_browser = {}
    for i in data:
        b = httpagentparser.simple_detect(i["visitor_useragent"])[1]
        if b not in web_browser:
            web_browser.update({b: 1})
        else:
            web_browser[b] += 1
    return web_browser

#function that cleans the browser data and truncates the name                        
def clean_browser_data(data):
    results = {}
    browsers = browser_data_3a(data)
    for i in browsers.keys():
        r = re.findall('.+ [0-9]', i)
        for j in r:
            if j[:-2] not in results:
                results.update({j[:-2]: browsers[i]})
            else:
                results[j[:-2]] += browsers[i]
    return results

#function which gets all the countires where documents have been viewed        
def get_countries(doc_id, data):
    countries = dict()
    for x in data:
        if x.get("subject_doc_id") == doc_id:
            if x.get("visitor_country") in countries.keys():
                countries[x["visitor_country"]] += 1
            else:
                countries.update({x.get("visitor_country"):1})
    return countries

#function which returns the continents documents have been viewed by associating countries with continents        
def get_continents(doc_id, data):
    continents = {"AF": 0, "EU": 0, "OC": 0, "NA": 0, "SA": 0, "AS": 0}
    data = get_countries(doc_id, data)
    if data is None:
        return
    for i in data.keys():
        if country_to_continent[i] == "AF":
            continents["AF"] += data[i]
        elif country_to_continent[i] == "EU":
            continents["EU"] += data[i]
        elif country_to_continent[i] == "OC":
            continents["OC"] += data[i]
        elif country_to_continent[i] == "NA":
            continents["NA"] += data[i]
        elif country_to_continent[i] == "SA":
            continents["SA"] += data[i]
        elif country_to_continent[i] == "AS":
            continents["AS"] += data[i]
    return continents
            
country_to_continent = {
        'AP': 'AS',
        'AF': 'AS',
        'AX': 'EU',
        'AL': 'EU',
        'DZ': 'AF',
        'AS': 'OC',
        'AD': 'EU',
        'AO': 'AF',
        'AI': 'NA',
        'AQ': 'AN',
        'AG': 'NA',
        'AR': 'SA',
        'AM': 'AS',
        'AW': 'NA',
        'AU': 'OC',
        'AT': 'EU',
        'AZ': 'AS',
        'BS': 'NA',
        'BH': 'AS',
        'BD': 'AS',
        'BB': 'NA',
        'BY': 'EU',
        'BE': 'EU',
        'BZ': 'NA',
        'BJ': 'AF',
        'BM': 'NA',
        'BT': 'AS',
        'BO': 'SA',
        'BQ': 'NA',
        'BA': 'EU',
        'BW': 'AF',
        'BV': 'AN',
        'BR': 'SA',
        'IO': 'AS',
        'VG': 'NA',
        'BN': 'AS',
        'BG': 'EU',
        'BF': 'AF',
        'BI': 'AF',
        'KH': 'AS',
        'CM': 'AF',
        'CA': 'NA',
        'CV': 'AF',
        'KY': 'NA',
        'CF': 'AF',
        'TD': 'AF',
        'CL': 'SA',
        'CN': 'AS',
        'CX': 'AS',
        'CC': 'AS',
        'CO': 'SA',
        'KM': 'AF',
        'CD': 'AF',
        'CG': 'AF',
        'CK': 'OC',
        'CR': 'NA',
        'CI': 'AF',
        'HR': 'EU',
        'CU': 'NA',
        'CW': 'NA',
        'CY': 'AS',
        'CZ': 'EU',
        'DK': 'EU',
        'DJ': 'AF',
        'DM': 'NA',
        'DO': 'NA',
        'EC': 'SA',
        'EG': 'AF',
        'SV': 'NA',
        'GQ': 'AF',
        'ER': 'AF',
        'EE': 'EU',
        'ET': 'AF',
        'FO': 'EU',
        'FK': 'SA',
        'FJ': 'OC',
        'FI': 'EU',
        'FR': 'EU',
        'GF': 'SA',
        'PF': 'OC',
        'TF': 'AN',
        'GA': 'AF',
        'GM': 'AF',
        'GE': 'AS',
        'DE': 'EU',
        'GH': 'AF',
        'GI': 'EU',
        'GR': 'EU',
        'GL': 'NA',
        'GD': 'NA',
        'GP': 'NA',
        'GU': 'OC',
        'GT': 'NA',
        'GG': 'EU',
        'GN': 'AF',
        'GW': 'AF',
        'GY': 'SA',
        'HT': 'NA',
        'HM': 'AN',
        'VA': 'EU',
        'HN': 'NA',
        'HK': 'AS',
        'HU': 'EU',
        'IS': 'EU',
        'IN': 'AS',
        'ID': 'AS',
        'IR': 'AS',
        'IQ': 'AS',
        'IE': 'EU',
        'IM': 'EU',
        'IL': 'AS',
        'IT': 'EU',
        'JM': 'NA',
        'JP': 'AS',
        'JE': 'EU',
        'JO': 'AS',
        'KZ': 'AS',
        'KE': 'AF',
        'KI': 'OC',
        'KP': 'AS',
        'KR': 'AS',
        'KW': 'AS',
        'KG': 'AS',
        'LA': 'AS',
        'LV': 'EU',
        'LB': 'AS',
        'LS': 'AF',
        'LR': 'AF',
        'LY': 'AF',
        'LI': 'EU',
        'LT': 'EU',
        'LU': 'EU',
        'MO': 'AS',
        'MK': 'EU',
        'MG': 'AF',
        'MW': 'AF',
        'MY': 'AS',
        'MV': 'AS',
        'ML': 'AF',
        'MT': 'EU',
        'MH': 'OC',
        'MQ': 'NA',
        'MR': 'AF',
        'MU': 'AF',
        'YT': 'AF',
        'MX': 'NA',
        'FM': 'OC',
        'MD': 'EU',
        'MC': 'EU',
        'MN': 'AS',
        'ME': 'EU',
        'MS': 'NA',
        'MA': 'AF',
        'MZ': 'AF',
        'MM': 'AS',
        'NA': 'AF',
        'NR': 'OC',
        'NP': 'AS',
        'NL': 'EU',
        'NC': 'OC',
        'NZ': 'OC',
        'NI': 'NA',
        'NE': 'AF',
        'NG': 'AF',
        'NU': 'OC',
        'NF': 'OC',
        'MP': 'OC',
        'NO': 'EU',
        'OM': 'AS',
        'PK': 'AS',
        'PW': 'OC',
        'PS': 'AS',
        'PA': 'NA',
        'PG': 'OC',
        'PY': 'SA',
        'PE': 'SA',
        'PH': 'AS',
        'PN': 'OC',
        'PL': 'EU',
        'PT': 'EU',
        'PR': 'NA',
        'QA': 'AS',
        'RE': 'AF',
        'RO': 'EU',
        'RU': 'EU',
        'RW': 'AF',
        'BL': 'NA',
        'SH': 'AF',
        'KN': 'NA',
        'LC': 'NA',
        'MF': 'NA',
        'PM': 'NA',
        'VC': 'NA',
        'WS': 'OC',
        'SM': 'EU',
        'ST': 'AF',
        'SA': 'AS',
        'SN': 'AF',
        'RS': 'EU',
        'SC': 'AF',
        'SL': 'AF',
        'SG': 'AS',
        'SX': 'NA',
        'SK': 'EU',
        'SI': 'EU',
        'SB': 'OC',
        'SO': 'AF',
        'ZA': 'AF',
        'GS': 'AN',
        'SS': 'AF',
        'ES': 'EU',
        'LK': 'AS',
        'SD': 'AF',
        'SR': 'SA',
        'SJ': 'EU',
        'SZ': 'AF',
        'SE': 'EU',
        'CH': 'EU',
        'SY': 'AS',
        'TW': 'AS',
        'TJ': 'AS',
        'TZ': 'AF',
        'TH': 'AS',
        'TL': 'AS',
        'TG': 'AF',
        'TK': 'OC',
        'TO': 'OC',
        'TT': 'NA',
        'TN': 'AF',
        'TR': 'AS',
        'TM': 'AS',
        'TC': 'NA',
        'TV': 'OC',
        'UG': 'AF',
        'UA': 'EU',
        'AE': 'AS',
        'GB': 'EU',
        'US': 'NA',
        'UM': 'OC',
        'VI': 'NA',
        'UY': 'SA',
        'UZ': 'AS',
        'VU': 'OC',
        'VE': 'SA',
        'VN': 'AS',
        'WF': 'OC',
        'EH': 'AF',
        'YE': 'AS',
        'ZM': 'AF',
        'ZW': 'AF',
        'ZZ': 'Unknown',
        'EU': 'Unknown'
    }
    
content = []
def init(path_to_json):
    with open(path_to_json) as f:
        for l in f.readlines():
            content.append(json.loads(l))
            
if __name__ == "__main__":
    init()
    #print(content)
    if(args["t"] == "2a"):
        task2a(args["d"])
    elif(args["t"] == "2b"):
        task2b(args["d"])
    elif(args["t"] == "3a"):
        task3a()
    elif(args["t"] == "3b"):
        task3b()
    elif(args["t"] == "4"):
        task4()
    elif(args["t"] == "5a"):
        task5a(args["d"])
    elif(args["t"] == "5b"):
        task5b(args["u"])
    elif(args["t"] == "5c"):
        task5c(args["d"],args["u"], None)
    elif(args["t"] == "5d"):
        task5c(args["d"],args["u"], sort_readership)
    elif(args["t"] == "5e"):
        task5c(args["d"],args["u"], sort_number)