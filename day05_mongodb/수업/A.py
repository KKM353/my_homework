from pymongo import mongo_client

url = "mongodb://localhost:27017/"
mgClient = mongo_client.MongoClient(url)
#print(mgClient)
db = mgClient["soodb"]
#print(db)

db_list = mgClient.list_database_names()
#print(db_list)

if "soodb" in db_list: 
    print("soodb 존재함") #DB에 내용이 입력되기 전까지는 생성되지 않음