# import pymongo modules
import pymongo

# get client object
mongo_client = pymongo.MongoClient("mongodb://localhost:27017/")

# database to use
my_database = mongo_client["Practice"]

#collection to use
my_table = my_database["employee"]

# create list of dictionaries
sql = [
	{"Name": "Pradeep", "Profile" : "Designer"},
	{"Name" : "Rahul", "Profile" : "WebApp"}
		]

# use insert_many to insert above list	
my_table.insert_many(sql)

# find() returns all records from collection
for x in my_table.find():
	print(x)


