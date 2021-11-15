import csv
import pandas as pd

def cargar_diccionario_ingredientes():
    ingredientes = []
    file = open('ingredientes.txt','r', encoding='utf-8')
    lineas = file.readlines()
    for i in lineas:
        item = i.replace("\n"," ").split(" ")
        ingredientes.append({"title": item[0], "buscador" : item[0].lower(), "stock" : float(item[1])})
    return ingredientes


def cargar_diccionario_recetas():
    demo = list()

    for line in open("recetas.csv"):
        item = line.split(" ")
        for i in item:
            demo.append(i.split(","))

    minuta_final = []

    cont = 0
    while cont < len(demo):
        d = {"title": demo[cont][0], "buscador":demo[cont][0].lower()}
        del demo[cont][0]
        d["items"] = demo[cont]

        minuta_final.append(d)
        cont += 1

    return minuta_final


def consultar_plato(key, platillos):
    cont = 0
    estado = False
    while cont < len(platillos):
        if platillos[cont]["buscador"] == key.lower():
            estado = True
        cont +=1


    return estado


def rebajar_intentario(items, ingredientes, key):
    # items productos a eleminar
    # invetario
    # palabra
    status = True
    item = ""
    for index in range(len(ingredientes)):
        for i in items:
            if ingredientes[index]["buscador"] == i.lower():
                if ingredientes[index]["stock"] == 0:
                    status = False
                    break

    if status == True:
        for index in range(len(ingredientes)):
            for i in items:
                if ingredientes[index]["buscador"] == i.lower():
                    ingredientes[index]["stock"] -= 1

    else:
         print(f"*** No se puede hacer {key} porque falta { item } ***")

    printStocks(ingredientes)


def prepararReceta(estado_platillo, key, platillos,ingredientes):
    if estado_platillo == False:
        print(f"*** Lo sentimos pero no preparamos {key} ***")
    else:
        cont = 0
        while cont < len(platillos):
            if platillos[cont]["buscador"] == key.lower():
                rebajar_intentario(platillos[cont]["items"], ingredientes, key)
            cont +=1

def reponerIngredientes(keys, ingredientes):
    for i in keys:
        for x in ingredientes:
            if i.lower() == x["buscador"]:
                x["stock"] += 1


    printStocks(ingredientes)


def printStocks(ingredientes):
    print(pd.DataFrame(ingredientes, columns=["title", "stock"]))


def main():
    ingredientes = cargar_diccionario_ingredientes()
    platillos = cargar_diccionario_recetas()

    iniciar = True

    while iniciar == True:
        key = input("Ingresa la receta que quieres o REPONER : \n").split()
        if key[0].lower() == "stop":
            iniciar = False
        elif key[0].lower() == "preparar":
            if len(key) < 2:
                print("No ingreso el platillo a preparar u ocurrio un error")
            else:
                estado_platillo = consultar_plato(key[1], platillos)
                prepararReceta(estado_platillo, key[1],platillos,ingredientes)
        elif key[0] == "reponer":
            if len(key) < 2:
                print("No ingreso nada para Reponer u ocurrio un error")
            else:
                reponerIngredientes(key,ingredientes)
        else:
            print("no se reconoce el comando, intente nuevamente \n")



if __name__ == '__main__':
    main()
