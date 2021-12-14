import csv
from io import BytesIO
from urllib.request import urlopen

import xlsxwriter

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

  
    xls = [] 
    total = 0
    xls.append(["id_aprtida", "nombre_partida", "suma", "Porcentaje"])


    for i in data_filter:
        suma = 0
        for x in datos_partidas:
            if i["id_partida"] == x["id_partida"]:
                if x["moneda"] == "DOLARES":
                    precio = x["monto_inicial"] * usd_a_clp
                else:
                    precio = x["monto_inicial"]

                suma += precio
        total += suma


    for i in data_filter:
        suma = 0
        for x in datos_partidas:
            if i["id_partida"] == x["id_partida"]:
                if x["moneda"] == "DOLARES":
                    precio = x["monto_inicial"] * usd_a_clp
                else:
                    precio = x["monto_inicial"]

                suma += precio
        calculo = "{0:.0f}%".format(suma/float(total) * 100)
        xls.append([i["id_partida"], i["nombre_partida"], suma, calculo])

  
    
    print("generando excel....")
    libro = xlsxwriter.Workbook('informe.xlsx')
    hoja = libro.add_worksheet()
    
    currency_format = libro.add_format({'num_format': '#,##0'})

    url_img = "data:image/png;base64,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"


    row = 17
    col = 0

    image_data = BytesIO(urlopen(url_img).read())

    hoja.insert_image('A1', url_img,{'image_data': image_data})

    hoja.set_column('A:A', 15)
    hoja.set_column('B:B', 100)
    hoja.set_column('C:C', 20)

    hoja.write("A11","Pontificia Universidad Católica de Chile", currency_format)
    hoja.write("A12","Clase Ejecutiva UC", currency_format)
    hoja.write("B15","Informe Datos Analizados", currency_format)

    for i in xls:
        hoja.write(row, col, i[0], currency_format)
        hoja.write(row, col + 1, i[1], currency_format)
        hoja.write(row, col + 2, i[2], currency_format)
        hoja.write(row, col + 3, i[3], currency_format)
        row +=1

    hoja.write(row, 0, 'Total:')
    hoja.write(row, 1, '=SUM(C:C)', currency_format)
    print("exportando excel")
    libro.close()
    print("archivo  excel generado con exito")




funcion_personalizada(partidas, datos_partidas, usd_a_clp)

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
