from pymongo import MongoClient
from bson.objectid import ObjectId
uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

client = MongoClient(uri)
db = client.get_default_database()

posts = db['posts']
customers = db['customers']

post_list = posts.find()
for post in post_list:
    print(post)

