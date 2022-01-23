#Reference - https://dev.to/fprime/how-to-create-a-web-crawler-from-scratch-in-python-2p46


from fileinput import filename
import requests
from bs4 import BeautifulSoup
import re    
from urllib.parse import urlparse  
import os

# For each link, we retrieve paragraphs from it, combine each paragraph as one string, and save it to documents (Fig. 2)
def CombineContent(link):
    documents = []
    for i in link:
        # Make a request to the link
        r = requests.get(i)
    
        # Initialize BeautifulSoup object to parse the content 
        soup = BeautifulSoup(r.content, 'html.parser')
    
        # Retrieve all paragraphs and combine it as one
        sen = []
        for i in soup.find('div', {'class':'read__content'}).find_all('p'):
            sen.append(i.text)
    
        # Add the combined paragraphs to documents
        documents.append(' '.join(sen))
    return documents



class Crawler(object):    
    def __init__(self, starting_url, dataPath):    
        self.starting_url = starting_url   
        self.dataPath = dataPath
        self.filePath = dataPath + 'files/'
        self.ignored = set()
        self.failed = set()
        self.crawled = set()
        self.content = list()
        self.maxLinks = 10
        self.fileNum = 0    
        self.nameMapping = dict()

    def get_html(self, url):    
        try:    
            html = requests.get(url)
            self.nameMapping[url] = self.filePath + 'file' + str(self.fileNum) + '.html'
            with open(self.filePath + 'file' + str(self.fileNum) + '.html', 'w', encoding="utf-8") as file:
                file.write(html.content.decode('latin-1'))
            self.fileNum+=1
        except Exception as e:    
            print(e)
            self.failed.add(url)    
            return ""    
        return html.content.decode('latin-1')    

    def get_links(self, url):     
        file = open(self.nameMapping[url], 'r', encoding="utf-8")  
        html = file.read()  
        parsed = urlparse(url)    
        base = f"{parsed.scheme}://{parsed.netloc}"    
        links = re.findall('''<a\s+(?:[^>]*?\s+)?href="([^"]*)"''', html)    
        for i, link in enumerate(links):    
            if not urlparse(link).netloc:    
                link_with_base = base + link    
                links[i] = link_with_base    

        return set(filter(lambda x: 'mailto' not in x, links))    

    def extract_info(self, url):    
        html = self.get_html(url)
        meta = re.findall("<meta .*?name=[\"'](.*?)['\"].*?content=[\"'](.*?)['\"].*?>", html)    
        return dict(meta)    

    def crawl(self, url):
        if not re.search('(.*goal\..*)|(.*bit..*)',url):
            self.ignored.add(url)
            return
        self.crawled.add(url)
        info = self.extract_info(url)
        self.content.append([self.nameMapping[url],url,info.get('description'),info.get('keywords')])
        for link in self.get_links(url):    
            if link in self.crawled:    
                continue        
            if len(self.crawled) > self.maxLinks:
                break   
            self.crawl(link)
            

    def start(self):    
        os.makedirs(self.dataPath, exist_ok=True) 
        os.makedirs(self.filePath, exist_ok=True) 
        self.crawl(self.starting_url)    