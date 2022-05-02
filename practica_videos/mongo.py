import pymongo


client = pymongo.MongoClient("mongodb://localhost:27017/")

#mostrar todas la bases de dastos
print(client.list_database_names())

# conexion db especifico1
mydb = client["mydatabases"]

# lista de colecciones en la base de datos (colecciones es el conjunto de documentos)
print(mydb.list_collection_names())

# mydb = client["test"]
# colect = mydb["miColeccion"]

# colect.insert_one({"x":10, "y": 20})
# colect.insert_one({"x":35, "y": 80})





