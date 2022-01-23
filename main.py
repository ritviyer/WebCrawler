#Reference - https://towardsdatascience.com/create-a-simple-search-engine-using-python-412587619ff5

import CrawlingFunctions as CF
import pandas as pd

dataPath = 'data/'
seedURL = "https://www.goal.com/en-us/news/rashford-man-utd-top-four-rangnick-gamble-west-ham/bltcd66097e1b4403b6"   
crawler = CF.Crawler(seedURL, dataPath)     
crawler.start()

df = pd.DataFrame(crawler.content, columns=['FilePath','URL','Description','Keywords'])
df.to_csv(dataPath + 'fileSummary.csv', index=False) 


#documents = CF.CombineContent(links)

#print(len(documents))