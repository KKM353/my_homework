from pymongo import mongo_client

url = "mongodb://localhost:27017/"
mgClient = mongo_client.MongoClient(url)
db = mgClient["soodb"] # Database
col = db["adress"] # table

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

#rows = col.insert_many(dics) #insert가 된 리스트만 가져옴
#print("rows.inserted_ids", rows.inserted_ids)
#print()

#(1) 모든 컬럼(field)을 가져온다
#docs = col.find()
#for doc in docs:
    #print(doc)

 
#(2-1) 특정 컬럼(field)를  가져옴1
#docs = col.find({}, {"_id":1}) # id컬럼들만 호출
#for doc in docs:
    #print(doc)
    
#(2-2) 특정 컬럼(field)를  가져옴2
#docs = col.find({}, {"_id":0}) # id컬럼만 제외하고 나머지 호출
#for doc in docs:
    #print(doc)
'''
#(2-3) 특정 컬럼(field)를  가져옴3
docs = col.find({}, {"name":1}) # id컬럼과 name 포함
for doc in docs:
    print(doc)
    
#(2-4) 특정 컬럼(field)를  가져옴4
docs = col.find({}, {"name":1, "addr":1 }) # id + name + addr
for doc in docs:
    print(doc)   
    
#(2-5) 특정 컬럼(field)를  가져옴4
docs = col.find({}, {"name":1 }) #error : 가져오고 싶지 않은 필드는 안쓰면된다 _id는 디폴트가 1이라 표시를 해줘야 되지만 나머지의 디폴트는 0이기에 그냥 안쓰면 된다.
for doc in docs:
    print(doc)
'''
#(2-6)   
docs = col.find({}, {"_id":1,"name":0,"addr":0,"rdate":0}) 
for doc in docs:
    print(doc)
    
# id는 default 값으로  1이 기본으로 되서 출력이 같이 된다. "_id":1 <- 디폴드값
# _id 는 디폴트 : 1 ( 0일때 명시 필요 ) , id 가 아닌 필드는 디폴트 : 0 ( 1 일때 명시 필요 )


#col.drop() #기존 컬렉션 삭제