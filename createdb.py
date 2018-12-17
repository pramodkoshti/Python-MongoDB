import pymongo

# get client object

mongo_client = pymongo.MongoClient("mongodb://localhost:27017/")

# create database

my_database = mongo_client["Practice"]

# mongo db don't create database until it has some db object

# create table using the database object

demo_table = my_database["employee"]


# mongo db don't create table until it has some db content

sql = {"Name" : "Pramod", "Profile" : "Developer"}

# insert record into table
demo_table.insert_one(sql)

# Now we can check if the database exists
print(mongo_client.list_database_names())

# Now check if collection exists in the database
print(my_database.list_collection_names()) 
