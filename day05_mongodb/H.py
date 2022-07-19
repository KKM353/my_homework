from pymongo import mongo_client

url = "mongodb://localhost:27017/"
mgClient = mongo_client.MongoClient(url)
db = mgClient["soodb"] # Database
col = db["adress"] # table

import datetime
dt_now = datetime.datetime.now() 

dics = [
  { "_id":1, "name": "가길동", "addr": "서울", "rdate":dt_now},
  { "_id":2, "name": "나길동", "addr": "경기", "rdate":dt_now},
  { "_id":3, "name": "다길동", "addr": "부산", "rdate":dt_now},
  { "_id":4, "name": "라길동", "addr": "인천", "rdate":dt_now},
  { "_id":5, "name": "마길동", "addr": "대구", "rdate":dt_now},
  { "_id":6, "name": "바길동", "addr": "광주", "rdate":dt_now},
  { "_id":7, "name": "사길동", "addr": "대전", "rdate":dt_now},
  { "_id":8, "name": "아길동", "addr": "울산", "rdate":dt_now},
  { "_id":9, "name": "자길동", "addr": "창원", "rdate":dt_now},
  { "_id":10, "name": "차길동", "addr": "청주", "rdate":dt_now}
]

#rows = col.insert_many(dics)
#col.insert_one({ "_id":11, "name": "천길동", "addr": "서천", "rdate":dt_now})

# (1) 1 row 수정
#where = {"addr":"부산"} # where addr = '부산' update address set addr
#new = {"$set":{"addr":"제주", "name":"오유현"}} #set addr = 제주
#col.update_one(where, new)

#(2) n row 수정
where = {"addr": {"$regex": "^서"}} # where addr like '서%'
new = {"$set":{"addr":"가산역", "name":"15강의실"}} #set addr = 제주
rows = col.update_many(where , new)
print("rows.modified_count",rows.modified_count)

# 결과 확인
docs = col.find()
for doc in docs:
    print(doc) 

#col.drop()