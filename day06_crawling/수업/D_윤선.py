from bs4 import BeautifulSoup
import requests
import pandas as pd

# 데이터 크롤링
df = pd.DataFrame()
base_url = "https://finance.naver.com/item/sise_day.nhn?code=068270"
for page in range(1,10):
    url = "{}&page={}".format(base_url,page)
    response = requests.get(url,headers={'User-agent':'Mozilla/5.0'})
    source = response.text
    html = pd.read_html(source, header=0)[0]
    df = pd.concat([df, html],ignore_index=True) #인덱스 번호 무시하고 합치기  

# 데이터 가공
df = df.dropna()
df = df.sort_values(by='날짜',ascending=False) #내림차순
print(df.to_string())

#print(len(df))
a=df.to_dict()

# for x in a:
#     #print(x)
#     for y in df.index:
#         #print(y)
#         print(a[x][y])
    
# for x in df.index:
#     print(a['날짜'][x])

# DB데이터 입력
from pymongo import mongo_client
url = "mongodb://localhost:27017/"
mgClient = mongo_client.MongoClient(url)
db = mgClient["stockdb"]
col = db["celltrion"]

dics =[]
for x in df.index:
    dic = {"날짜":a['날짜'][x],"종가":a['종가'][x],"전일비":a['전일비'][x],"시가":a['시가'][x],"고가":a['고가'][x],"저가":a['저가'][x] ,"거래량":a['거래량'][x]}
    dics.append(dic)
print(dics)
 
rows = col.insert_many(dics)

# 데이터find
where = {"날짜":{"$gte":"2022.04.01"}}
#docs = col.find(where)
docs = col.find(where,{"_id":0,"날짜":1,"종가":1})
for doc in docs:
    print(doc)

# 차트그리기
import matplotlib.pyplot as plt
plt.title("Celltrion Closing Price(3Months)")
plt.xticks(rotation=45 )
plt.plot(df['날짜'],df['종가'],'b*-')
plt.grid(color='gray',linestyle='--')
plt.show()

# 컬렉션 삭제
#col.drop()

