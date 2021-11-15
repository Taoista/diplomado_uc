import csv
import pandas as pd


def cargar_diccionario_ingredientes():
    ingredientes = []
    file = open('ingredientes.txt','r', encoding='utf-8')
    lineas = file.readlines()
    for i in lineas:
        item = i.replace("\n"," ").split(" ")
        ingredientes.append({"item": item[0],"Inventario" : float(item[1])})
    return ingredientes


def cargar_diccionario_recetas():
    lista = list()

    for line in open ("recetas.csv"):
        item = line.split(" ")
        for i in item:
            lista.append(i.split(","))

    men_u = []

    for i in lista:
        diccionary = {"plato": i [0]}
        del i[0]
        diccionary["Inventario"] = i
        men_u.append(diccionary)
    return men_u

def buscar_en_menu(key, recetas):

    estado = False


    for i in recetas:

        if i["plato"].lower() == key.lower():

            estado = True

    return estado


def disminuir_stock(items, ingredientes, key):
    print("Stock actual de ingredientes disponibles")
    status = True
    item = ""
    for index in range(len(ingredientes)):
        for i in items:
            if ingredientes[index]["item"].lower() == i.lower():
                if ingredientes[index]["Inventario"] == 0:
                    item = i
                    status = False
                    break

    if status == True:
        for index in range(len(ingredientes)):
            for i in items:
                if ingredientes[index]["item"].lower() == i.lower():
                    ingredientes[index]["Inventario"] -= 1

    else:
         print(f"* No se puede hacer {key} porque falta { item } *")

    printStock(ingredientes)



def prepararReceta(estado_platillo, key, recetas,ingredientes):
    if estado_platillo == False:
        print(f"* Lo sentimos pero no preparamos {key} *")
    else:
        for i in recetas:
            if i["plato"].lower() == key.lower():
                disminuir_stock(i["Inventario"], ingredientes, key)


def reponerIngredientes(keys, ingredientes):
    for i in keys:
        for x in ingredientes:
            if i.lower() == x["item"].lower():
                x["Inventario"] += 1


    printStock(ingredientes)

def printStock(ingredientes):
    print(pd.DataFrame(ingredientes, columns=["item", "Inventario"]))

def main():
    ingredientes = cargar_diccionario_ingredientes()
    recetas = cargar_diccionario_recetas()

    comenzar = True

    while comenzar == True:
        key = input("Ingresa la receta que quieres o REPONER : \n").split()
        if key[0].lower() == "stop":
            comenzar = False
        elif key[0].lower() == "preparar":
            if len(key) < 2:
                print("No ingreso el platillo a preparar u ocurrio un error")
            else:
                estado_platillo = buscar_en_menu(key[1], recetas)
                prepararReceta(estado_platillo, key[1],recetas,ingredientes)
        elif key[0].lower() == "reponer":
            if len(key) < 2:
                print("No ingreso nada para Reponer u ocurrio un error")
            else:
                reponerIngredientes(key,ingredientes)
        else:
            print("no se reconoce el comando, intente nuevamente \n")



if __name__ == '__main__':
    main()
