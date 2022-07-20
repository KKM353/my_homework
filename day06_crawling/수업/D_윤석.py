from bs4 import BeautifulSoup
import requests

url = 'https://finance.naver.com/item/sise_day.nhn?code=068270&page=1'
response = requests.get(url, headers={'User-agent':'Mozilla/5.0'})
source = response.text

soup = BeautifulSoup(source, 'lxml')

#1. 마지막 페이지 가져오기
td_pgRR = soup.find('td', class_='pgRR') #body > table.Nnavi > tbody > tr > td.pgRR > a
a_href = td_pgRR.a['href']
a_href_split_list = a_href.split('=')
last_page = a_href_split_list[-1]

#2. 전체 페이지 읽어오기
import pandas as pd
df = pd.DataFrame()
base_url = 'https://finance.naver.com/item/sise_day.nhn?code=068270'
for page in range(1, int(last_page)+1):
    url = "{}&page={}".format(base_url, page)
    response = requests.get(url, headers={'User-agent':'Mozilla/5.0'})
    source = response.text
    html = pd.read_html(source, header=0)[0]
    df = pd.concat([df, html])

#3. DataFrame 가공
df = df.dropna()
df = df.iloc[0:2000] 
df = df.sort_values(by='날짜')

from pymongo import mongo_client

url = 'mongodb://localhost:27017/'
mgClient = mongo_client.MongoClient(url)
db = mgClient['cysDB']
col = db['Celltrion']

df.reset_index(inplace=True)
df_dict = df.to_dict("records")

col.insert_many(df_dict)

where = {'거래량':{'$gt':350000}} #거래량이 350000주 이상이였던 날
docs = col.find(where, {'_id':0, '날짜':1, '거래량':1}).sort('거래량', -1).limit(200)
for doc in docs: 
    print(doc)

# col.drop()