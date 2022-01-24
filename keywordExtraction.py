from fileinput import filename
import requests
from bs4 import BeautifulSoup
import re    
import string
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import numpy as np
import time

def GetContent(file):
    f = open(file, 'r', encoding="utf-8")  
    r = f.read()  

    soup = BeautifulSoup(r, 'html.parser')
    # para = ""
    # for p in soup.find_all('p'):
    #     para = para + " " + p.get_text()
    para = soup.get_text()
    return para

def CleanContent(content):
    content = re.sub(r'[^\x00-\x7F]+', ' ', content)
    content = re.sub(r'@\w+', '', content)
    content = content.lower()
    content = re.sub(r'[%s]' % re.escape(string.punctuation), ' ', content)
    content = re.sub(r'[0-9]', '', content)
    content = re.sub(r'\s{2,}', ' ', content)
    return content

def ExtractKeyWord(df):
    vectorizer = TfidfVectorizer(stop_words='english')
    X = vectorizer.fit_transform(df['Content'])
    X = X.T.toarray()
    df = pd.DataFrame(X, index=vectorizer.get_feature_names())
    return vectorizer, df

def Get_Similar_Articles(q, df, df_full, vectorizer):
    print("query:", q)
    q = [q]
    q_vec = vectorizer.transform(q).toarray().reshape(df.shape[0],)
    sim = {}

    for i in range(len(df.columns)):
        sim[i] = np.dot(df.loc[:, i].values, q_vec) / np.linalg.norm(df.loc[:, i]) * np.linalg.norm(q_vec)

    sim_sorted = sorted(sim.items(), key=lambda x: x[1], reverse=True)

    topR = 5
    for k, v in sim_sorted:
        if v != 0.0:
            print("Similarity Index:", v)
            print(df_full['Title'][k])
            print(df_full['URL'][k])
            print(df_full['Description'][k])
            print()
            print()
            topR-=1
        if(topR <= 0):
            break