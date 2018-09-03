from pymongo import MongoClient
from bson.objectid import ObjectId
uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

client = MongoClient(uri)
db = client.get_default_database()

posts = db['posts']
customers = db['customers']

post = {
    'title' : 'Châm ngôn sống',
    'author' : 'thebach',
    'content': 'Đừng bao giờ \n'+
    'đánh mất niềm tin vào bản thân mình \n'+
    'Chỉ cần tin là mình có thế làm được là bạn lại có \n'+
    'thêm lí do để cố gắng thực hiện điều đó.'
}
posts.insert_one(post);