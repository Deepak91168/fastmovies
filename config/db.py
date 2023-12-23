from pymongo import MongoClient
conn = MongoClient("mongodb+srv://ds9210048:ds9210048@cluster0.otmffrq.mongodb.net/")

try:
    conn.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = conn['sample_mflix']  
collection = db['movies'] 
movies = collection.find().limit(10)
movie_list = list(movies)


    