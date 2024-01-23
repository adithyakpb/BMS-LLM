#to handle the knowledge base in mongoDB

import pymongo

class KnowledgeBase:
    """Knowledge Base class to handle the knowledge base in mongoDB"""
    def __init__(self, collection) -> None:
        self.client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.db = self.client["bms-kb"]
        self.collection = self.db[collection]
    
    def insert(self, data) -> bool:
        """Insert data into the collection"""
        try:
            self.collection.insert_one(data)
            return True
        except:
            return False
    
    def find(self, query) -> list:
        """Find data in the collection"""
        return self.collection.find_one(query)
