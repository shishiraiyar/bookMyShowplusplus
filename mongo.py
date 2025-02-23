from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
# import certifi

from dotenv import dotenv_values

config = dotenv_values(".env")

class MongoDatabase:
    def __init__(self):
        url = config["MONGO_CONNECTION_STRING"]
        # Create a new client and connect to the server
        self.client = MongoClient(url, server_api=ServerApi('1'))
        self.db = self.client["MovieApp"] 
        self.col = self.db["seats"]
        self.col2 = self.db["passwords"]
        self.col3 = self.db["admins"]
        print("INITTED")

    def listDatabases(self):
        print(self.client.list_database_names())
    
    def listCollections(self):
        print(self.db.list_collection_names())

    def displayDatabase(self):
        for col in self.db.list_collection_names():
            curr_col = self.db[col]
            for x in curr_col.find():
                print(x) 

    def insert(self,showID,seats):
        doc = {"_id":showID,"seatMatrix":seats}
        self.col.insert_one(doc)

    def update(self,showID,row,col):
        doc = self.getSeats(showID)
        if doc is not None:
            seats=doc["seatMatrix"]
            seats[row][col] = 1
            query={"_id":showID}
            newvalues = { "$set": { "seatMatrix": seats } }
            self.col.update_one(query,newvalues)     

    def addDummyData(self):
        matrix=[[0,1,0],[1,0,1],[0,0,0]]
        self.insert(1,matrix)
        self.insert(2,matrix)
        self.insert(3,matrix)
        self.insert(4,matrix)

    def getSeats(self,showID):
        query={"_id":showID}
        doc = self.col.find_one(query)
        return doc
    
    def validate(self,email,password):
        query={"_id":email}
        doc = self.col2.find_one(query)
        if doc["password"]==password:
            return True
        else:
            return False
        
    def validateAdmin(self,email,password):
        query={"_id":email}
        doc = self.col3.find_one(query)
        if doc and doc["password"]==password:
            return True
        else:
            return False
        
    def addUser(self,email,username,password):
        doc = {"_id":email,"username":username,"password":password}
        self.col2.insert_one(doc)
        

if __name__ == "__main__":
    # Cluster-> Database -> Collection -> Document

    database = MongoDatabase()
    # database.addDummyData()
    # database.addUser("tavashikumar.cs21@rvce.edu.in","tavashi","hello")
    # print(database.validate("tavashikumar.cs21@rvce.edu.in","hello"))
    # print(database.validate("tavashikumar.cs21@rvce.edu.in","hellorwrw"))
    # print(database.validateAdmin("tavashi123@gmail.com","hello123"))


    database.displayDatabase()

    # update seat for a given show
    # matrix=[[1,1,1],[1,0,1],[0,0,0]]
    # database.update(1,0,0)

    # fetching seat info given a particular showID
    # info = database.getSeats(3)
    # print(info["seatMatrix"])

    

  
    
    # print(certifi.where())

    # # Send a ping to confirm a successful connection
    # try:
    #     client.admin.command('ping')
    #     print("Pinged your deployment. You successfully connected to MongoDB!")
    # except Exception as e:
    #     print(e)