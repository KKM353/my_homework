from pymongo import mongo_client
from bs4 import BeautifulSoup
import requests

weburl = "https://finance.naver.com/item/sise_day.nhn?code=068270&page=1"
response = requests.get(weburl, headers={'User-agent':'Mozilla/5.0'})
source = response.text

url = "mongodb://localhost:27017/"
mgClient = mongo_client.MongoClient(url)
db = mgClient["parkdb"]
col = db["cell"]

soup = BeautifulSoup(source, 'lxml')
td_pgRR = soup.find('td', class_='pgRR')
a_href = td_pgRR.a['href']
a_href_split_list = a_href.split("=")
last_page = a_href_split_list[-1]

import pandas as pd
df = pd.DataFrame()
base_url = "https://finance.naver.com/item/sise_day.nhn?code=068270"
#for page in range(1, int(last_page)+1):
for page in range(1, 3):
    url = "{}&page={}".format(base_url, page)
    response = requests.get(url, headers={'User-agent':'Mozilla/5.0'})
    source = response.text
    html = pd.read_html(source, header=0)[0]
    df = pd.concat([df, html])
df = df.dropna()
df = df.sort_values(by='날짜')
df = df.to_dict('records')

#print(df)

#col.insert_many(df)

#where = {"종가":{"$gt":185000}} # 종가가 185000보다 큰 값만 출력
#where = {"날짜":{"$gte":"2022.07.01"}} #날짜가 2022.07.01이후의 값만 출력
#where = {"날짜":{"$lte":"2022.06.29"}} #날짜가 2022.06.29이전의 값만 출력
where = {"시가":{"$gte":160000}} #시가가 160000원 이상의 값만 출력
docs = col.find(where, {"_id":0, "날짜":1})
for doc in docs:
    print(doc)
#col.drop()