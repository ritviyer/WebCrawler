import keywordExtraction as KE
import pandas as pd
import time

dataPath = 'data/'

while True:
    print()
    query = input("Enter your query : ")
    print()

    start = time.time()
    df = pd.read_csv(dataPath + 'fileSummary_updated.csv')
    vectorizer, df_mat = KE.ExtractKeyWord(df)
    KE.Get_Similar_Articles(str(query), df_mat, df, vectorizer)


    end = time.time()
    print("Query Execution time : ")
    print(str(end-start) + " seconds")
    print()

    check = input("Enter '1' to exit. Press enter to search again : ")
    if str(check) == '1':
        break

print()
input("Press enter key to Exit")

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