import csv
import matplotlib.pyplot as plt
# import pandas as pd

NOMBRE_ARCHIVO = "ley-de-presupuestos-inicial-y-vigentenivel-partidaa--mayo-2021.csv"


usd_a_clp = 800


## Partidas debe ser un conjunto con pares id_partida y nombre_partida, los pares son únicos. 
def set():
    data = list()
    with open(NOMBRE_ARCHIVO, newline='',  encoding="utf-8") as File:  
        next(File)

        search = False
        reader = csv.reader(File)
        for row in reader:
            data.append({"id_partida": row[4], "nombre_partida" : row[5]})

    filtro = list()

    for element in data:
        if element not in filtro:
            filtro.append(element)
    return filtro

partidas = set()



## Datos partidas debe ser un diccionario indexado por el ID de cada partida, y que contenga los datos
## de todos los subtítulos de esa partida. Es decir, la key es id_partida y el value los subtítulos de esa partida.
def dict():
    data = list()
    data_mont = list()
    with open(NOMBRE_ARCHIVO, newline='',  encoding="utf-8") as File:
        next(File)

        search = False
        reader = csv.reader(File)
        for row in reader:
            data.append({"id_partida": row[4], "nombre_partida": row[5],"moneda":row[3],"id_subtitulo": row[6], "subtitulo":row[7], "monto_inicial":int(row[8].replace(".","")), "monto_final":int(row[9].replace(".",""))})

    return data

datos_partidas = dict()



    

## Esta función carga los datos desde el archivo. Debe completarla las partes que se indican.
def cargar_datos(archivo, partidas, datos_partidas):

    ####### ESTA PARTE DE ABAJO NO SE MODIFICA ######
    with open(archivo, "r", encoding="utf-8") as lineas:
        next(lineas)
        for linea in lineas:
            data = linea.strip("\n").split(";")[0].split(",")
            id = data[0]
            año = data[1]
            mes = data[2]
            moneda = "USD" if data[3]=='DOLARES' else "CLP"
            id_partida = data[4]
            if len(data) == 11:
                nombre_partida = data[5][1:] + data[6][:-1]
                id_subtitulo = data[7]
                nombre_subtitulo = data[8]
                monto_original = float(data[9].replace(".",""))
                monto_a_marzo = float(data[10].replace(".",""))
            elif len(data) == 12:
                nombre_partida = data[5][1:] + data[6] + data[7][:-1]
                id_subtitulo = data[8]
                nombre_subtitulo = data[9]
                monto_original = float(data[10].replace(".",""))
                monto_a_marzo = float(data[11].replace(".",""))
            else:
                nombre_partida = data[5]
                id_subtitulo = data[6]
                nombre_subtitulo = data[7]
                monto_original = float(data[8].replace(".",""))
                monto_a_marzo = float(data[9].replace(".",""))
            ####### ESTA PARTE DE ARRIBA NO SE MODIFICA ######

            ## Por cada línea se entrega la siguiente información: 
            ## id, año, mes, moneda, id_partida, nombre_partida, id_subtitulo, nombre_subtitulo, monto_original y monto_a_marzo

            ## 1. Agregar datos a estructuras apropiadas.
            ##    Construir conjunto con nombres de partidas
            ##    Partidas debe ser un conjunto con pares id_partida y nombre_partida. 
            ## COMPLETAR AQUí

            ##
            ##
            ##

            ## 1. Agregar datos a estructuras apropiadas.
            ##    Construir diccionario con informacion de todas las ejecuciones de una partida
            ##    datos_partidas debe ser un diccionario indexado por el ID de cada partida, y que contenga los datos
            ##    de todos los subtítulos de esa partida.
            ## COMPLETAR AQUI

            ##
            ##
            ##

    print("Datos leidos.")
    print("Cantidad de partidas distintas leidas:", len(partidas))
    print("")


## 2. Construir función que muestra el detalle de todos los subtítulos de una partida en particular.
##    Debe mostrar un menu con todas las partidas posibles y permitir al usuario elegir una.
##    Recibe como parámetros el conjunto de partidas existentes,
##    un diccionario con los datos de los subtítulos de cada partida y un parámetro de conversión de dólares a pesos.
##    
def montos_por_partida(partidas, datos_partidas, usd_a_clp):

    for i in partidas:
        print(int(i["id_partida"])," - ",i["nombre_partida"])

    print("")
    opcion = input("SELECCIONAR OPCION A ELEGIR \n")
    print("")

    encontrado = False
    valor = ''
    key = 0
    if opcion.isdigit():
        for i in partidas:
            if(int(i["id_partida"]) == int(opcion)):
                encontrado = True
                valor = i["id_partida"]," - ",i["nombre_partida"]
                key = i["id_partida"]
                break
            else:
                encontrado = False
    else:
        print("no selecciono nada u ocurrio un error")       
    if encontrado == True:
        print(valor)
    else:
        print("No existe esa opcion")

    for i in datos_partidas:
        if i["id_partida"] == key:
            if i["moneda"] == "DOLARES":
                monto_mostrar = i["monto_inicial"] * usd_a_clp
            else:
                monto_mostrar = i["monto_inicial"]      
            print(i["id_subtitulo"],i["subtitulo"], monto_mostrar)
    print("")

## 3. Construir función que imprima datos de los montos totales originales de cada partida, ordenados de mayor a menor.
##    Recibe como parámetros el conjunto de partidas existentes,
##    un diccionario con los datos de los subtítulos de cada partida y un parámetro de conversión de dólares a pesos.
def partidas_por_monto_original(partidas, datos_partidas, usd_a_clp):
    ## COMPLETAR AQUI
    ##
    ##
    ##
    data_get = list()
    data_filter = list()

    for i in datos_partidas:
        data_get.append({"id_partida" : i["id_partida"], "nombre_partida": i["nombre_partida"]})

    for element in data_get:
        if element not in data_filter:
            data_filter.append(element)

    for i in data_filter:
        suma = 0
        for x in datos_partidas:
            if i["id_partida"] == x["id_partida"]:
                if x["moneda"] == "DOLARES":
                    precio = x["monto_inicial"] * usd_a_clp
                else:
                    precio = x["monto_inicial"]

                suma += precio
                
        print(i["id_partida"], i["nombre_partida"], suma)

## 4. Agregar una función más que responda a una consulta definida por usted, usando los datos disponible en el archivo
##    Puede cambiar el nombre a la función, pero también deberá cambiarla en la opción 3 del menú.
def funcion_personalizada(partidas, datos_partidas, usd_a_clp):
    ## COMPLETAR AQUI
    ##
    ##
    ##

    data_get = list()
    data_filter = list()

    for i in datos_partidas:
        data_get.append({"id_partida" : i["id_partida"], "nombre_partida": i["nombre_partida"]})

    for element in data_get:
        if element not in data_filter:
            data_filter.append(element)

    list_grafico = list()

    for i in data_filter:
        suma = 0
        for x in datos_partidas:
            if i["id_partida"] == x["id_partida"]:
                if x["moneda"] == "DOLARES":
                    precio = x["monto_inicial"] * usd_a_clp
                else:
                    precio = x["monto_inicial"]

                suma += precio
        list_grafico.append({"id_partida": i["id_partida"], "nombre_partida":i["nombre_partida"], "suma":suma})


    
    lbl = list()
    precios = list()

    for i in list_grafico:
        lbl.append(i["nombre_partida"])
        precios.append(i["suma"])

    # fig, ax = plt.subplots()
    # ax.pie(precios, labels=lbl)
    # plt.show()

    plt.barh(lbl, precios)
    plt.ylabel('Nombre Partidas')
    
    ## Legenda en el eje x
    plt.xlabel('Precios')
    
    ## Título de Gráfica
    plt.title('Detalle Precios CLP Nombre partidas')
    
    ## Mostramos Gráfica
    plt.show()
    



############################################################################
## No necesita modificar este código ##
if __name__ == "__main__":
    cargar_datos(NOMBRE_ARCHIVO, partidas, datos_partidas)

    dict_opciones = {1: ("Montos de una partida", montos_por_partida),
                     2: ("Partidas ordenadas de mayor a menor, por monto original", partidas_por_monto_original),
                     3: ("Función personalizada", funcion_personalizada), ## puede cambiar este nombre en la parte 4.
                     0: ("Salir", None)
                    }
    op = -1
    while op != 0:
        
        for k, v in dict_opciones.items():
            print(f"{k}: {v[0]}")
        
        try:
            op = int(input("Opcion: "))
        
        except ValueError:
            print(f"Ingrese opción valida")
            op = -1
        
        if op != 0 and op in dict_opciones.keys():
            dict_opciones[op][1](partidas, datos_partidas, 800)
