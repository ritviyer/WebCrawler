
import keywordExtraction as KE
import pandas as pd
import time

dataPath = 'data/'
print()
print("The keyword extraction process has started.")
print()
start = time.time()

df = pd.read_csv(dataPath + 'fileSummary.csv')
df['Content'] = df['FilePath'].apply(KE.GetContent)
df['Content'] = df['Content'].apply(KE.CleanContent)
df.to_csv(dataPath + 'fileSummary_updated.csv', index=False) 

df = pd.read_csv(dataPath + 'fileSummary_updated.csv')
vectorizer, df_mat = KE.ExtractKeyWord(df)
df_mat.to_csv(dataPath + 'TFIDF Matrix.csv') 

topWords = []
for col in df_mat.columns:
    topWords.append(','.join(df_mat[col].nlargest(10).index.tolist()))
df['Extracted Keywords'] = topWords
df.to_csv(dataPath + 'fileSummary_updated.csv', index = False) 

end = time.time()
print("Time taken to extract keywords : ")
print(str(end-start) + " seconds")
print()
input("Press enter key to Exit")

# Run Times
# 14.278074026107788
# 19.56166100502014
# 13.900164127349854
# 14.598106145858765
# 15.222592115402222
