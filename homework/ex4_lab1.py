from pymongo import MongoClient
from matplotlib import pyplot

uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

client = MongoClient(uri)
db = client.get_default_database()

posts = db['posts']
customers = db['customers']

customers_list = customers.find()
ref = [0, 0, 0]
for customers in customers_list:
    if customers['ref'] == 'events':
        ref[0] += 1
    elif customers['ref'] == 'wom':
        ref[1] += 1
    else:
        ref[2] +=1
print(ref)
ref_name = ['events', 'wom', 'ads']
pyplot.pie(ref, labels=ref_name, autopct="%.1f%%", shadow=True, explode=[0, 0.1, 0] )
pyplot.title("Tỷ lệ phần trăm cho mỗi tham chiếu")
pyplot.axis("equal")
pyplot.show()