from pymongo import mongo_client

url = "mongodb://localhost:27017/"
Client = mongo_client.MongoClient(url)
#print(mClient)
Db = Client["soodb"]
#print(mgDb)

db_list = Client.list_database_names()
#print()

if "soodb" in db_list:
    print("soodb 존재함") # DB에 내용이 입력되기 전까지는 생성되지 않음