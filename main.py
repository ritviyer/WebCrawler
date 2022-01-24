import crawler as CF
import pandas as pd
import requests

dataPath = 'data/'

seedURL = input("Please enter the seed URL : ")
while(True):
    try:
        response = requests.get(seedURL)
    except:
        print("URL does not exist on Internet. Please enter a valid URL")
        seedURL = input("Please enter the seed URL : ")
        continue
    break

crawler = CF.Crawler(seedURL, dataPath)     
crawler.start()
crawler.end()
df = pd.DataFrame(crawler.content, columns=['FilePath','URL','Title','Description','Keywords'])
df.to_csv(dataPath + 'fileSummary.csv', index=False) 
df = pd.DataFrame(crawler.timeKeeper, columns=['Pages Crawled','Time Since last', 'Total Time'])
df.to_csv(dataPath + 'timeStats.csv', index=False) 

input("Press enter key to Exit")