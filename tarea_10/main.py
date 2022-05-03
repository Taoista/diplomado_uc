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
    colect_all = mydb["feriadosAll"]

    #feriados_2022
    response = requests.get("https://apis.digital.gob.cl/fl/feriados/2020",headers={
        "User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
    })

    response_all = requests.get("https://apis.digital.gob.cl/fl/feriados",headers={
        "User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
    })

    data = response.json()
    data_all = response_all.json()
    ##### 
    ##### inserta todos los datos del 2022   
    #####
    # colect.insert_many(data)
    # colect_all.insert_many(data_all)
    # print("insert completo")
    ##### 
    ##### siguientes consultas
    #####

    ##### muestra todo
    print("===== Todos los Feriados de 2020 ====")
    for i in colect.find({}):
        # print(f"El día de {i['nombre']} es un feriado de tipo {i['tipo']} y se celebra el {i['fecha']}")
        pass

    print("===== Solo los Feriados Civiles de 2020 =====")
    for i in colect.find({"tipo":"Civil" }):
        # print(f"El día de Todos {i['nombre'] } es un feriado de tipo {i['tipo']} y se celebra el {i['fecha']}")
        pass

    print("===== Solo los Feriados Irrenunciables de 2020 =====")
    for i in colect.find({"irrenunciable":"1" }):
        # print(f"El día de {i['nombre']} es un feriado de tipo {i['tipo']} y se celebra el {i['fecha']}")
        pass
    print("===== Solo los Feriados que incluyen 'Santo' o 'Santos' =====")
    for i in colect.find({"nombre":{"$regex":"\w*Santo\w*"}},{"_id":0}):
        # print(f"El día de {i['nombre']} es un feriado de tipo {i['tipo']} y se celebra el {i['fecha']}")
        pass
    ####  obtener las leyes involucradas en el feriado del Plebiscito 
    for i in response_all.find({"comentarios":{"$regex":"\w*plebi\w*"}},{"_id":0}):
        print(i)
        pass


    print("______terminando________")



if __name__ == '__main__':
    main()
