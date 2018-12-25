# select multiple rows from mongo db

import pymongo

my_connection = pymongo.MongoClient("mongodb://localhost:27017/")

my_db = my_connection["yourdb"]

my_collection = my_db["yourcollection"]


# select all columns and all rows
for x in my_collection.find():
	print(x)

# select specific columns 
for x in my_collection.find({},{"_id" : 0, "column1" : 1, "column2": 1}):
	print(x)	
