import pymongo as mongo
import json
import requests


def main():
    cliente = mongo.MongoClient("mongodb://localhost:27017/")
    mydb = cliente["nicodb"]
    clt = mydb["feriados2020"]

    response = requests.get("https://apis.digital.gob.cl/fl/feriados/2020",headers={
        "User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
    })
    json = response.json()
    clt.insert_many(json)


    print("===== Todos los Feriados de 2020 ====")
    for i in clt.find({}):
        print("El día de {0} es un feriado de tipo {1} y se celebra el {2}".format(i['nombre'],i['tipo'],i['fecha']))

    print("===== Solo los Feriados Civiles de 2020 =====")
    for i in clt.find({"tipo":"Civil" }):
        print("El día de Todos {0} es un feriado de tipo {1} y se celebra el {2}".format(i['nombre'],i['tipo'],i['fecha']))

    print("===== Solo los Feriados Irrenunciables de 2020 =====")
    for i in clt.find({"irrenunciable":"1" }):
        print("El día de {0} es un feriado de tipo {1} y se celebra el {2}".format(i['nombre'],i['tipo'],i['fecha']))

    print("===== Solo los Feriados que incluyen 'Santo' o 'Santos' =====")
    for i in clt.find({"nombre":{"$regex":"\w*Santo\w*"}},{"_id":0}):
        print("El día de {0} es un feriado de tipo {1} y se celebra el {2}".format(i['nombre'],i['tipo'],i['fecha']))
   
    print(" ===== Leyes relacionadas con el Plebiscito de Abril =====")
    print("Las leyes involucradas en el día del Plebiscito Constitucional son las siguientes:")

    print("===== Leyes relacionadas con el Plebiscito de Abril ====")
    print("Las leyes involucradas en el día del Plebiscito Constitucional son las siguientes:")
    for i in clt.find({"$or":[{"leyes.nombre":"Ley 2.977"}, {"leyes.nombre":"Ley 18.700"}]},{}):
        print("fecha --- {0}".format(i["fecha"]))
        for x in i["leyes"]:
            print(f"La ley involucrada en el Plebiscito es {0} revisar en {1}".format(x['nombre'], x['url']))




if __name__ == '__main__':
    main()
