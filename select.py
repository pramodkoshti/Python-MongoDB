import pymongo

mongo_client = pymongo.MongoClient("mongodb://localhost:27017/")

my_database = mongo_client["Practice"]

my_table = my_database["employee"]

# will select first recod from the collection with all columns
print(my_table.find_one())

# select only name column
print(my_table.find_one({},{ "_id": 0, "Name": 1, "Profile": 1 }))

