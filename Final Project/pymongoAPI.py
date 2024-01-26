import pymongo 
from pymongo import MongoClient
from bson import ObjectId

# Connect to MongoDB
client = pymongo.MongoClient('mongodb://3.120.174.0:27017')

# Create or get the database
db = client.c19_project
coll = db.resources

# Create a document
resource_data = {
    "_id": 4,
    "resource": "redivis",
    "title": "Coronavirus COVID-19 Global Cases",
    "link": "https://redivis.com/datasets/rxta-4v35cgyzf",
    "last_update": "12/07/2020",
    "comment": "This data comes from the data repository for the 2019 Novel Coronavirus Visual Dashboard operated by the Johns Hopkins University Center for Systems Science and Engineering (JHU CSSE). This database was created in response to the Coronavirus public health emergency to track reported cases in real-time."
}
# Insert the document into the collection
result = coll.insert_one(resource_data)

print(f"Inserted document ID: {result.inserted_id}")




# coll.delete_one({"_id":'65b3d8e1844237d58a532a25'})

res = coll.find_one({"_id": 4})


for value in res:
    print(res)

client.close()