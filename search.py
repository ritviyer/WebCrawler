import keywordExtraction as KE
import pandas as pd
import main
import time

dataPath = main.dataPath

start = time.time()

df = pd.read_csv(dataPath + 'fileSummary_updated.csv')
vectorizer, df_mat = KE.ExtractKeyWord(df)
KE.Get_Similar_Articles('super league clubs', df_mat, df, vectorizer)
KE.Get_Similar_Articles('league clubs', df_mat, df, vectorizer)
KE.Get_Similar_Articles('Ronaldo', df_mat, df, vectorizer)
KE.Get_Similar_Articles('Latest News', df_mat, df, vectorizer)
KE.Get_Similar_Articles('Arsenal', df_mat, df, vectorizer)


end = time.time()
print(end-start)

# Run Times
# 1 Search
# 0.5020205974578857
# 0.49811887741088867
# 0.4858410358428955
# 0.48073673248291016
# 0.4934086799621582

# 5 Searches
# 1.434032917022705
# 1.6736869812011719
# 1.6210639476776123
# 1.539928674697876
# 1.6468555927276611