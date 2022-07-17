from pymongo import MongoClient
from pprint import pprint
from entities.note import note_body

class DataBase:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        

    def connect(self):
        client = MongoClient(f'mongodb+srv://{self.username}:{self.password}@cluster1.vy6ck.mongodb.net/?retryWrites=true&w=majority')
        db = client.database1
        self.table1 = db.table1 
        

    def list_notes(self):
        ids = []
        print('========All notes=======')        
        for i,notes in enumerate(self.table1.find()):
            print(f'{i+1} -> ',notes['title'])
            ids.append(notes['_id'])        
        return ids


    def create_note(self, title, content, date):
        note_body['title'] = title
        note_body['content']  = content
        note_body['date'] = date 
        self.table1.insert_one(note_body)


    def delete_note(self, note_id):
        self.table1.delete_one({"_id": note_id})


    def show_note_content(self, note_id):
        note = self.table1.find_one({'_id' : note_id})
        title = note['title']
        content = note['content']
        print(f'===={title}====')
        print(f'* {content}')