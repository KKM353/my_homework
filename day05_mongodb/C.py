from pymongo import mongo_client

url = "mongodb://localhost:27017/"
mgClient = mongo_client.MongoClient(url)
#print(mClient)
db = mgClient["soodb"] # Database
col = db["adress"] # table

import datetime
dt_now = datetime.datetime.now() # 파이썬은 함수를 변수로 만들수 있다
print(dt_now) 
#print(type(dt_now))

dic = {"name":"최길동", "addr":"Jejudo", "rdate":dt_now} #JSON( insert into customers values(???) )
row = col.insert_one(dic) # x는 하나의 row
print(row.inserted_id) # _id 컬럼이 자동으로 생성되어 겹치지 않는 해쉬코드값이 자동 입력됨( inserted_id = praimary key  )

#(1)  처음 insert된 row가 출력
doc = col.find_one()
print(doc) # 처음 insert된 row가 출력, 1개의 row만 출력한다.
print()

#(2)  모든 row가 출력
#docs = col.find() # 입력된 순서대로 리스팅
#docs = col.find().sort("_id") #order by _id asc
docs = col.find().sort("_id", -1) #order by _id  desc
#mgDocs = col.find().sort("name") # order by name asc , asc와 +1은 생략 가능 ("name", +1)
#mgDocs = col.find().sort("name", -1) # order by name desc
#mgDocs = col.find().sort("rdate")  # order by rdate asc
#mgDocs = col.find().sort("rdate",-1)  # order by rdate desc
for doc in docs: #selecting
    print(doc) # 모든 row가 출력된다, #여러개를 셀렉팅할 때

col.drop() #기존 컬렉션 삭제