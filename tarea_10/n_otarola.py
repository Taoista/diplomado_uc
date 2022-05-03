import pymongo as mongo
from datetime import datetime # lo vi y me gusto insertarlo :(
import json
import requests

def main():
    clt = mongo.MongoClient("mongodb://localhost:27017/")
   
    mydb = clt["mongo"]
    collection = mydb["feriados2020"]
    headers = {"User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
    response = requests.get("https://apis.digital.gob.cl/fl/feriados/2020", headers = headers)
    data = response.json()
   

    # collection.insert_many(data)

    print("===== Todos los Feriados de 2020 ====")
    for item in collection.find({}):
        print(f"El día de {item['nombre']} es un feriado de tipo {item['tipo']} y se celebra el {item['fecha']}")

    print("===== Solo los Feriados Civiles de 2020 =====")
    for item in collection.find({"tipo":"Civil" }):
        print(f"El día de Todos {item['nombre'] } es un feriado de tipo {item['tipo']} y se celebra el {item['fecha']}")

    print("===== Solo los Feriados Irrenunciables de 2020 =====")
    for item in collection.find({"irrenunciable":"1" }):
        print(f"El día de {item['nombre']} es un feriado de tipo {item['tipo']} y se celebra el {item['fecha']}")

    print("===== Solo los Feriados que incluyen 'Santo' o 'Santos' =====")
    for item in collection.find({"nombre":{"$regex":"\w*Santo\w*"}},{"_id":0}):
        print(f"El día de {item['nombre']} es un feriado de tipo {item['tipo']} y se celebra el {item['fecha']}")

    print(" ===== Leyes relacionadas con el Plebiscito de Abril =====")
    print("Las leyes involucradas en el día del Plebiscito Constitucional son las siguientes:")

    meses = ("Enero", "Febrero", "Marzo", "Abri", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
    print("Las leyes involucradas en el día del Plebiscito Constitucional son las siguientes:")
    for item in collection.find({"$or":[{"leyes.nombre":"Ley 2.977"}, {"leyes.nombre":"Ley 18.700"}]},{}):
        full_fecha = datetime.strptime(item["fecha"], '%Y-%m-%d')
        print(f"===== Leyes relacionadas con el Plebiscito de {meses[full_fecha.month -1]} del {full_fecha.year}=====")
        lista = list()
        list_clean = list()
        for select in item["leyes"]:
            lista.append({"nombre":select["nombre"], "ulr" : select["url"]})

        for element in lista:
            if element not in list_clean:
                list_clean.append(element)
    
        for item in list_clean:
            print(f"La ley involucrada en el Plebiscito es {item['nombre']} revisar en {item['ulr']}")


if __name__ == '__main__':
    main()
