# Data-Analyser
python coursework

F20SC: Industrial Programming CW2: Data Analytics (50%) 2016/17 Assessed Coursework 2 — Data Analysis of a Document Tracker
==============

The application must provide the following functionality:
1. Python: The core logic of the application should be implemented in Python.
2. Views by country/continent: We want to analyse, for a given document, from which countries and continents the document has been viewed. The data should be displayed as a histogram of countries, i.e. counting the number of occurrences for each country in the input file.
(a) The application should take a string as input, which uniquely specifies a document (a document UUID), and return a histogram of countries of the viewers. The histogram can be displayed using mathplot.
(b) Use the data you have collected in the previous task, group the countries by continent, and generate a histogram of the continents of the viewers. The histogram can be displayed using mathplot.
3. Views by browser: In this task we want to identify the most popular browser. To this end, the application has to examine the visitor useragent field and count the number of occurrences for each value in the input file.
(a) The application should return and display a histogram of all browser identifiers of the viewers.
(b) In the previous task, you will see that the browser strings are very verbose, distinguishing browser by e.g. version and OS used. Process the input of the above task, so that only the main browser name is used to distinguish them (e.g. Mozilla), and again display the result as a histogram.
4. Reader profiles: In order to develop a readership profile for the site, we want to identify the most avid readers. We want to determine, for each user, the total time spent reading documents. The top 10 readers, based on this analysis, should be printed.
5. “Also likes” functionality: Popular document-hosting web sites, such as Amazon, provide informa- tion about related documents based on document tracking information. One such feature is the “also likes” functionality: for a given document, identify, which other documents have been read by this document’s readers. The idea is that, without examining the detail of either document, the informa- tion that both documents have been read by the same reader relates two documents with each other. Figure 1 gives an example of this functionality. In this task, you should write a function that generates such an “other readers of this document also like” list, which is parametrised over the function to determine the order in the list of documents. Display the top 10 documents, which are “liked” by other readers.
To achieve this task you will need to do the following:
(a) Implement a function that takes a document UUID and returns all visitor UUIDs of readers of that document.
(b) Implement a function that takes a visitor UUID and returns all document UUIDs that have been read by this visitor.
(c) Using the two functions above, implement a function to implement the “also like” functionality, which takes as parameters the above document UUID and visitor UUID, and additionally a sorting function on documents. The function should return a list of “liked” documents, sorted by the sorting function parameter. Note: the implementation of this function must not fix the way how documents are sorted.
 Deadline: 3:30PM on Friday 2nd/Sunday 4th of December 2016; (individual project)
F20SC: Industrial Programming CW2: Data Analytics (50%) 2016/17 Documents Readers
Input
Also read ...
Result (most also readers)
Figure 1: Example of identifying also-likes documents. Starting from the current reader and document (green), all readers are identified, who have also read the input document (blue). From the other documents, read by these readers, the top 10 documents, counted by number of readers are identified and displayed. In this example the red document is top of this list.
(d) Use this function to produce an “also like” list of documents, using the above function, based on readership profile for sorting the documents.
(e) Use this function to produce an “also like” list of documents, using a sorting function, based on the number of readers of the same document.
(f) In each of the above two use cases, provide a document UUID and visitor UUID as input and produce a list of top 10 document UUIDs as a result.
6. GUI usage: To read the required data and to display the statistical data, develop a simple GUI that reads the user inputs described above, and with buttons to process the data as required per task.
7. Command-lineusage:Theapplicationshallprovideacommand-lineinterfacetotestitsfunctionality in an automated way, like this:
to check the results of implementing task task_id using inputs user_uuid for the user UUID and doc_uuid for the document UUID.
