import certifi
from pymongo import MongoClient

uri = "mongodb+srv://colabwithagam:<password>@cluster0.6aiev.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(uri, tlsCAFile=certifi.where())

try:
    client.admin.command('ping')
    print("Pinged your deployment. Successfully connected to MongoDB!")
except Exception as e:
    print(f"Connection failed: {e}")
