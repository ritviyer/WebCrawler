#Reference - https://dev.to/fprime/how-to-create-a-web-crawler-from-scratch-in-python-2p46
# https://www.analyticsvidhya.com/blog/2020/11/words-that-matter-a-simple-guide-to-keyword-extraction-in-python/

from fileinput import filename
import requests
import re    
from urllib.parse import urlparse  
import os
from bs4 import BeautifulSoup
import time

class Crawler(object):    
    def __init__(self, starting_url, dataPath):    
        self.starting_url = starting_url   
        self.dataPath = dataPath
        self.filePath = dataPath + 'files/'
        self.extracted = list()
        self.ignored = set()
        self.failed = set()
        self.crawled = set()
        self.content = list()
        self.nameMapping = dict()
        self.maxLinks = 1100
        self.fileNum = 0   
        self.startTime = time.time()
        self.lastTime = time.time() 
        self.timeCalculate = 50
        self.timeKeeper = list()

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
                self.extracted.append(links[i]) 

        return set(filter(lambda x: 'mailto' not in x, links))    

    def extract_info(self, url):    
        html = self.get_html(url)
        soup = BeautifulSoup(html, 'html.parser')
        meta = re.findall("<meta .*?name=[\"'](.*?)['\"].*?content=[\"'](.*?)['\"].*?>", html)    
        title = ""
        if not soup.title is None:
            title = soup.title.string
        else:
            title = " "
        return title, dict(meta)    

    def crawl(self, url):
        if not re.search('(.*goal\..*)|(.*bit..*)',url):
            self.ignored.add(url)
            return
        if(len(self.crawled)%self.timeCalculate == 0 and len(self.crawled) > 0):
            currTime = time.time()
            self.timeKeeper.append([len(self.crawled), currTime - self.lastTime , currTime - self.startTime])
            self.lastTime = currTime

        title,info = self.extract_info(url)
        if url in self.failed:
            return
        self.crawled.add(url)
        self.content.append([self.nameMapping[url],url,title,info.get('description'),info.get('keywords')])
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

    def end(self):
        currTime = time.time()
        self.timeKeeper.append([len(self.crawled), currTime - self.lastTime , currTime - self.startTime])
        self.lastTime = currTime
        with open(self.dataPath + 'stats.txt', 'w', encoding="utf-8") as file:
            file.write("Total URL's Extracted - " + str(len(self.extracted)) + '\n')
            file.write("Unique URL's Extracted - " + str(len(set(self.extracted))) + '\n')
            file.write("Total URL's Ignored - " + str(len(self.ignored)) + '\n')
            file.write("Total URL's Failed - " + str(len(self.failed)) + '\n')
            file.write("Total URL's Crawled - " + str(len(self.crawled)) + '\n')