from pymongo import MongoClient
from bson import ObjectId ,decode_all
from  tornado.escape import json_decode

class user(object):
    def __init__(self,first_name=None,last_name=None,date=None):
        client=MongoClient('localhost', 27017)# or  uri from MongoDB Atlas 
        self.db=client.user
        self.first_name=first_name
        self.last_name=last_name
        self.date=date
        
    def add(self):
        
        return self.db.users.insert_one({"first_name":self.first_name,"last_name":self.last_name,"date":self.date})
        
    def delete(self,_id):
        self.db.users.find_one_and_delete({"_id":ObjectId(_id)})

    def update(self,_id):
        self.db.users.find_one_and_replace({"_id":ObjectId(_id)},{"first_name":self.first_name,"last_name":self.last_name,"date":self.date})
        

    def get(self):
        data=list()
        documents=self.db.users.find_raw_batches()
        for document in documents:
            data.append(str(decode_all(document)))
        return data
        