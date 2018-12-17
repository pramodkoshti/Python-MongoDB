import pymongo

mongo_client = pymongo.MongoClient("mongodb://localhost:27017/")

my_database = mongo_client["Practice"]

my_table = my_database["employee"]

sql = [
	{"Name": "Pradeep", "Profile" : "Designer"},
	{"Name" : "Rahul", "Profile" : "WebApp"}
		]
	
my_table.insert_many(sql)

for x in my_table.find():
	print(x)


	