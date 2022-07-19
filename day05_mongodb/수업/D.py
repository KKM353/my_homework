from pymongo import mongo_client

url = "mongodb://localhost:27017/"
mgClient = mongo_client.MongoClient(url)
db = mgClient["soodb"]
col = db["address"]

import datetime
dt_now = datetime.datetime.now()

'''
dics = [
  { "name": "가길동", "addr": "서울", "rdate":dt_now},
  { "name": "나길동", "addr": "경기", "rdate":dt_now},
  { "name": "다길동", "addr": "부산", "rdate":dt_now},
  { "name": "라길동", "addr": "인천", "rdate":dt_now},
  { "name": "마길동", "addr": "대구", "rdate":dt_now},
  { "name": "바길동", "addr": "광주", "rdate":dt_now},
  { "name": "사길동", "addr": "대전", "rdate":dt_now},
  { "name": "아길동", "addr": "울산", "rdate":dt_now},
  { "name": "자길동", "addr": "창원", "rdate":dt_now},
  { "name": "차길동", "addr": "청주", "rdate":dt_now}
]
'''
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

#rows = col.insert_many(dics) # insert가 된 리스트만 가져옴
#print("rows.inserted_ids", rows.inserted_ids)

#(1) 모든 컬럼(field)을 가져옴 
#docs =  col.find()
#for doc in docs:  
#    print(doc)
    
#(2-1) 특정 컬럼(field)을 가져옴
#docs =  col.find({}, {"_id":1}) #id컬럼만 포함
#for doc in docs:  
#    print(doc)
    
#(2-2) 특정 컬럼(field)을 가져옴 
#docs =  col.find({}, {"_id":0}) #id컬럼만 제외 
#for doc in docs:  
#    print(doc)
    
#(2-3) 특정 컬럼(field)을 가져옴
docs =  col.find({}, {"name":1}) #id컬럼과 name만 포함  
for doc in docs:  
    print(doc)
    
#(2-4) 특정 컬럼(field)을 가져옴
docs =  col.find({}, {"name":1, "addr":1}) #_id + name + addr만 포함
for doc in docs:  
    print(doc)
    
#(2-5) 특정 컬럼(field)을 가져옴(error발생)
#docs =  col.find({}, {"name":1, "addr":0}) #"addr":0에서 발생(가져오고싶지않는 필드는 쓰지말것!)
#for doc in docs:  
#    print(doc)
    
#"_id":1 가 디폴트값!

#col.drop() #컬렉션 삭제 