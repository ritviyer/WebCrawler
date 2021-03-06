# Web Crawler

This is a simple web crawler which takes as input a seed URL and starts crawling. It downloads and saves the content and learns what the webpage is about while extracting keywords from each page. It can also take user queries and return relevant web pages (sort of like a mini search engine).

**The exe files are slow to start as they have to unpack all the libraries to a temp directory before the application can start. Please give them 30-60 seconds to load after which you should see a prompt on the screen for a user input implying that the application has started.**

Order of execution is - 
1. main.py / main.exe
2. keywordGen.py / keywordGen.exe
3. search.py / search.exe

Sample files generated by crawling https://www.goal.com/ are provided if you just want to test the search feature, and not spend time on crawling or keyword extraction. You can directly run the search.py to try out. In case of error or missing files within the data folder, follow the order of execution defined above.

### crawler.py
Contains the main crawler class which is responsible for taking the seed URL and do the actual crawling  and downloading of pages.

### main.py / main.exe
Takes the seed URL as a user input and starts the crawler. It is a small crawler which crawls about 1000 URLs. Depending on various factors, user might need to wait 15-30 mins for all the URLs to be crawled.

### keywordExtraction.py
Contains functions to read the html content from the saved web pages, clean the content, vectorize them, and even search for relevant web pages based on a given query.

### keywordGen.py / keywordGen.exe
Starts the keyword generation process which reads and cleans the html content for the saved web pages, and generates top 10 keywords for each web page depending on the content.

### search.py / search.exe
Takes a user input query, and searches the saved documents using cosine similarity, to return relevant web pages for the user. Make sure to run the main.py and the keywordGen.py before searching for a query.

## Acknowledgement
Used the following references for guidance - 
* https://towardsdatascience.com/create-a-simple-search-engine-using-python-412587619ff5
* https://dev.to/fprime/how-to-create-a-web-crawler-from-scratch-in-python-2p46
* https://towardsdatascience.com/tf-idf-for-document-ranking-from-scratch-in-python-on-real-world-dataset-796d339a4089