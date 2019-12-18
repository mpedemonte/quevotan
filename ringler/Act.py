import pymongo
from pymongo import MongoClient

cliente= MongoClient()
cliente= MongoClient('mongodb://localhost:27017/')

db= mongoClient.quevotan


consulta= db.Sesion.find().sort({$natural:-1}).limit(1)

print consulta