from pymongo import MongoClient
from pprint import pprint
import datetime


class DataBase:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        

    def connect(self):
        client = MongoClient(f'mongodb+srv://{self.username}:{self.password}@cluster1.vy6ck.mongodb.net/?retryWrites=true&w=majority')
        db = client.database1
        self.table1 = db.table1 
        

    def show_table(self, num):
        if num == 1:
            for i,notes in enumerate(self.table1.find()):
                print(f'\n{i+1} -> ',notes['comments'])

    
# load_dotenv('./token/.env')

# client = MongoClient(f'mongodb+srv://{os.getenv("username")}:{os.getenv("password")}@cluster1.vy6ck.mongodb.net/?retryWrites=true&w=majority')


# db = client.database1
# table1 = db.table1

# for notes in table1.find():
#     pprint(notes)

# table1.delete_one(table1.find()[1])

# data = {

#     "name": "Juca",
#     "comments": "Olá, essa é minha segunda nota",
#     "date": datetime.datetime.utcnow()
# }

# table1_id = table1.insert_one(data).inserted_id
# print(table1_id)

# list = db.list_collection_names()
# print(list)

# pprint(table1.find_one())