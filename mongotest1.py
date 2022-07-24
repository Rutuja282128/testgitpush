import pymongo
client = pymongo.MongoClient("mongodb+srv://RUTUJA:RUTUJA2821@cluster0.ravkzvj.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name":"Rutuja",
    "email":"jrutu133@gmail.com",
    "surname":"jadhav"

}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d )
