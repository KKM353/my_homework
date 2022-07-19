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

col.insert_one({ "_id":13, "name": "천길동", "addr": "서천", "rdate":dt_now})

#where ={"addr":"서울"} # where addr = '서울'
#where ={"addr":{"$gt":"서울"}} # $gt = > 라는 뜻 str에서는 오름차순? 어쨋든 ㅅ ㅇ ㅈ ㅊ 한글은 이순서 이기에 서울보다 큰건 ㅇ 으로 시작하는 단어들 # where addr >'서울'
#where ={"addr":{"$lt":"서울"}} # $lt = < 라는 뜻 str에서는 내림차순? 어쨋든 ㄱ ㄴ ㄷ ㄹ ㅁ ㅂ ㅅ 한글은 이순서 이기에 서울보다 작건 ㅂ 으로 내려가는 단어들 # where < '서울'
#where ={"addr":{"$lt":"서"}} # where addr < '서'
#where ={"addr":{"$lte":"서울"}} # $lte <= 작거나 같다  #where addr <= '서울'
#where ={"addr":{"$gte":"서울"}} # $gte >= 크거나 같다  #where addr >= '서울'
#where ={"addr":{"$ne":"서울"}} # $ne != 같지 않다  # where addr != '서울'
where = {"addr":{"$regex":"^서"}} # where addr like '서%'
docs = col.find(where)
for doc in docs:
    print(doc)
    
col.drop() #기존 컬렉션 삭제