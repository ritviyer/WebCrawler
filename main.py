#Reference - https://towardsdatascience.com/create-a-simple-search-engine-using-python-412587619ff5

import CrawlingFunctions as CF
import pandas as pd

dataPath = 'data/'
seedURL = "https://www.goal.com/"   

# crawler = CF.Crawler(seedURL, dataPath)     
# crawler.start()
# crawler.end()
# df = pd.DataFrame(crawler.content, columns=['FilePath','URL','Title','Description','Keywords'])
# df.to_csv(dataPath + 'fileSummary.csv', index=False) 
# df = pd.DataFrame(crawler.timeKeeper, columns=['Pages Crawled','Time Since last', 'Total Time'])
# df.to_csv(dataPath + 'timeStats.csv', index=False) 