
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import certifi

uri = "mongodb+srv://shishiraiyar:jyotishetty@cluster0.nfgzye6.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
print(certifi.where())
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection

mydb = client["lol"]
print(client.list_database_names())

mycol = mydb["customers"]
print(mydb.list_collection_names())

mydict = { "name": "John", "address": "Highway 37" }

x = mycol.insert_one(mydict)
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)