# 1. Connect to database
from pymongo import MongoClient
from bson.objectid import ObjectId
uri = "mongodb://thebach:66dcht22707@ds025792.mlab.com:25792/c4e21"

client = MongoClient(uri)
db = client.get_default_database()

# 2. Select collection
posts = db["posts"]
# 3. Create document
post = {
    "title": "Hom nay di hoc",
    "content": "buon ngu vl",
}
# 4. Insert document
# posts.insert_one(post)
post_list = posts.find()
# for post in post_list: 
    # post_list ~ collection ~ list
    # print(post)
    # post ~ document ~ dictionary
cond = {
    "title":{
        "$regex": "hom nay",
        "$options": "i"
    }
}
post = posts.find_one(cond)
print(post)