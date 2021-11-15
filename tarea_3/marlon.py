import csv
import pandas as pd


def cargar_diccionario_ingredientes():
    ingredientes = []
    file = open('ingredientes.txt','r', encoding='utf-8')
    lineas = file.readlines()
    for i in lineas:
        item = i.replace("\n"," ").split(" ")
        ingredientes.append({"item": item[0],"inventario" : float(item[1])})
    return ingredientes


def cargar_diccionario_recetas():
    comida = list()

    for line in open("recetas.csv"):
        item = line.split(" ")
        for i in item:
            comida.append(i.split(","))

    menu = []

    cont = 0
    while cont < len(comida):

        d = {"plato": comida[cont][0]}
        del comida[cont][0]
        d["items"] = comida[cont]

        menu.append(d)
        cont += 1

    return menu



def buscar_en_menu(key, recetas):
    estado = False

    for platito in recetas:
        if platito["plato"].lower() == key.lower():
            estado = True

    return estado


def disminuir_stock(items, ingredientes, key):
    print("Stock actual de ingredientes disponibles")
    status = True
    item = ""
    for index in range(len(ingredientes)):
        for i in items:
            if ingredientes[index]["item"].lower() == i.lower():
                if ingredientes[index]["inventario"] == 0:
                    item = i
                    status = False
                    break

    if status == True:
        for index in range(len(ingredientes)):
            for i in items:
                if ingredientes[index]["item"].lower() == i.lower():
                    ingredientes[index]["inventario"] -= 1

    else:
         print(f"* No se puede hacer {key} porque falta { item } *")

    print_stock(ingredientes)


def preparar_platillo(estado_platillo, key, recetas,ingredientes):
    if estado_platillo == False:
        print(f"* Lo sentimos pero no preparamos {key} *")
    else:
        cont = 0
        while cont < len(recetas):
            if recetas[cont]["plato"].lower() == key.lower():
                disminuir_stock(recetas[cont]["items"], ingredientes, key)
            cont +=1


def reponer_inventario(keys, ingredientes):
    for i in keys:
        for x in ingredientes:
            if i.lower() == x["item"].lower():
                x["inventario"] += 1

    print_stock(ingredientes)


def print_stock(ingredientes):
    print(pd.DataFrame(ingredientes, columns=["item", "inventario"]))

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
                preparar_platillo(estado_platillo, key[1],recetas,ingredientes)
        elif key[0].lower() == "reponer":
            if len(key) < 2:
                print("No ingreso nada para Reponer u ocurrio un error")
            else:
                reponer_inventario(key,ingredientes)
        else:
            print("no se reconoce el comando, intente nuevamente \n")



if __name__ == '__main__':
    main()
