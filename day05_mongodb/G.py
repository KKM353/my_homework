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

rows = col.insert_many(dics)

# (1) 1 row 삭제
#where = {"addr":"광주"} # where addrs = '부산'
#row = col.delete_one(where)
#print(row.deleted_count)

# N row 삭제
#where = {"addr": {"$lt": "서"}}
#where = {"addr": {"$regex": "^서"}}
#rows = col.delete_many(where)
#col.delete_many(where)
#print("rows.deleted_count",rows.deleted_count )

# (3) 모든 row 삭제
where = {}
rows = col.delete_many(where)
print("rows.deleted_count",rows.deleted_count )

# 결과 확인
docs = col.find()
for doc in docs:
    print(docs)
    
col.drop()