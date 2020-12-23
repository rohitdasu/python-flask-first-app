from flask_pymongo import pymongo
import urllib.parse

username = urllib.parse.quote_plus('rohitdasu')
password = urllib.parse.quote_plus('Rohit123!@#123')

CONNECTION_STRING = "mongodb+srv://"+username+":"+password+"@cluster0-fdams.mongodb.net/test?retryWrites=true&w=majority"

client = pymongo.MongoClient(CONNECTION_STRING)

db = client.get_database('flask_database')