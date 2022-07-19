from pymongo import mongo_client

url = "mongodb://localhost:27017/"
mgClient = mongo_client.MongoClient(url)
#print(mClient)
db = mgClient["soodb"]
col = db["address"]

import datetime
dt_now = datetime.datetime.now()
print("dt_now", dt_now) # 2022-07-19 09:37:49.452759
#print(type(dt_now))


dic = {"name":"홍길동3", "addr":"서울3", "rdate":dt_now} #JSON Format 
row = col.insert_one(dic) 
print("row.inserted_id", row.inserted_id) # _id 컬럼이 자동으로 생성되어 해시코드값이 자동 입력됨 

#(1) 처음 insert된 row가 출력
doc = col.find_one()
print(doc) 
print()

#(2) 모든 row 출력
#docs =  col.find() #입력된 순서대로 리스팅 
#docs =  col.find().sort("_id") # order by _id asc
docs =  col.find().sort("_id", -1)  # order by _id desc
#docs =  col.find().sort("name") # order by name asc 
#docs =  col.find().sort("name", 1) # order by name asc
#docs =  col.find().sort("name", -1) # order by name desc
#docs =  col.find().sort("rdate", -1) # order by rdate desc
for doc in docs:  
    print(doc)
   
#col.drop() #컬렉션 삭제 

    
