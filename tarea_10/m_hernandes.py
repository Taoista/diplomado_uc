import pymongo as mongo
import json
import requests


def main():
    client = mongo.MongoClient("mongodb://localhost:27017/")
   
    mydb = client["mongo"]
    colect = mydb["feriados2020"]
    # print(mydb.list_collection_names())

    #feriados_2022
    response = requests.get("https://apis.digital.gob.cl/fl/feriados/2020",headers={
        "User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
    })
    # data = response.json()
    ##### 
    ##### inserta todos los datos del 2020  
    #####
    # colect.insert_many(data)
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
    print(" ===== Leyes relacionadas con el Plebiscito de Abril =====")
    print("Las leyes involucradas en el día del Plebiscito Constitucional son las siguientes:")
    # for i in colect.find({"leyes.nombre":"Ley 2.977"},{"_id":0}):

    print("===== Leyes relacionadas con el Plebiscito de Abril ====")
    print("Las leyes involucradas en el día del Plebiscito Constitucional son las siguientes:")
    for i in colect.find({"$or":[{"leyes.nombre":"Ley 2.977"}, {"leyes.nombre":"Ley 18.700"}]},{}):
        print(i["fecha"])
        for x in i["leyes"]:
            print(f"La ley involucrada en el Plebiscito es { x['nombre'] } revisar en { x['url'] }")


        print("================")


    print("______terminando________")



if __name__ == '__main__':
    main()
