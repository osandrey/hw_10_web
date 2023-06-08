from pymongo import MongoClient



# def check_mongo_connection():
#     uri = "mongodb+srv://osandreyman:1111@firstcluster.g6svumr.mongodb.net/hw?retryWrites=true&w=majority"
#     client = MongoClient(uri)
#     try:
#         # Access a collection or perform a query
#         db = client.hw
#         collection = db.author
#         result = collection.find_one()
#         if result is not None:
#             print("Connection to MongoDB successful!")
#         else:
#             print("Connection to MongoDB failed!")
#     except Exception as e:
#         print("An error occurred while connecting to MongoDB:", str(e))
#
#
# check_mongo_connection()
def get_mongo_db():
    uri = "mongodb+srv://osandreyman:1111@firstcluster.g6svumr.mongodb.net/hw?retryWrites=true&w=majority"
    client = MongoClient(uri)
    db = client.hw
    return db



