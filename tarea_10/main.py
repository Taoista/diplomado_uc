import pymongo as mongo
import requests
import json

# video mod/page/view.php?id=1161162

def main():
    print("_______iniciando________")
    # conexion
    client = mongo.MongoClient("mongodb://localhost:27017/")
    # verificar base de datos
    # print(client.list_database_names())
    mydb = client["mongo"]
    colect = mydb["feriados2020"]
    # print(mydb.list_collection_names())
    

    #feriados_2022
    response = requests.get("https://apis.digital.gob.cl/fl/feriados/2022",headers={
        "User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
    })

    data = response.json()

    ##### 
    ##### inserta todos los datos del 2022   
    #####
    # colect.insert_many(data)

    ##### 
    ##### siguientes consultas
    #####

    ##### muestra todo
    for i in colect.find({}):
        # print(i)
        pass

    ##### obtener solo los feriados civiles
    for i in colect.find({"tipo":"Civil" }):
        # print(i)
        pass
    ##### obtener solo los feriados irrenunciables
    for i in colect.find({"irrenunciable":1 }):
        # print(i)
        pass
    ##### obtener solo los feriados que incluyen el texto "Santo" en el nombre
    for i in colect.find({
        
    }):
        print(i)


    print("______terminando________")



if __name__ == '__main__':
    main()
