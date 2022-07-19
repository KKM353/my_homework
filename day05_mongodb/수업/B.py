from pymongo import mongo_client

url = "mongodb://localhost:27017/"
mgClient = mongo_client.MongoClient(url)
#print(mClient)
db = mgClient["soodb"]
col = db["address"] 

col_list = db.list_collection_names()
print(col_list)
if "address" in col_list:
    print("address 컬렉션 존재") #Collection에 내용이 입력되기 전까지는 생성되지 않음

