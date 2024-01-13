import pymongo
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_URI = os.getenv('MONGO_URI')
client = MongoClient(MONGO_URI)
db = client['facts']

facts_collection = db['facts']

def get_all_facts():
  try:
    facts = facts_collection.find({},{"_id":0, "fact":1})
    return facts
  except: 
    print('Error retrieving facts')
    return []

def get_all_facts_text():
  try:
    facts = facts_collection.find({},{"_id":0, "fact":1})
    return [fact['fact'] for fact in facts]
  except: 
    print('Error retrieving facts')
    return []

def get_fact_by_id(id):
  try:
    fact = facts_collection.find_one({"id":id},{"_id":0, "fact":1})
    return fact
  except: 
    print('Error retrieving fact')
    return []

def get_fact_by_text(text):
  try:
    fact = facts_collection.find_one({"fact":text},{"_id":0, "fact":1})
    return fact
  except: 
    print('Error retrieving fact')
    return []

def add_fact(fact):
  try:
    facts_collection.insert_one(fact)
    return True
  except: 
    print('Error adding fact')
    return False

def delete_fact(id):
  try:
    facts_collection.delete_one({"id":id})
    return True
  except: 
    print('Error deleting fact')
    return False

def update_fact(id, fact):
  try:
    facts_collection.update_one({"id":id},{"$set":fact})
    return True
  except: 
    print('Error updating fact')
    return False

 



