NOMBRE_ARCHIVO = "ley-de-presupuestos-inicial-y-vigentenivel-partidaa--mayo-2021.csv"

## Partidas debe ser un conjunto con pares id_partida y nombre_partida, los pares son únicos. 
partidas = set()

def set():
    data = list()
    with open(NOMBRE_ARCHIVO, "r", encoding="utf-8") as lineas:
        next(lineas)
        for linea in lineas:
            data = linea.strip("\n").split(";")[0].split(",")
            id_partida = data[4]
            nombre_partida = data[5]
            if int(id_partida) % 2 == 0:
                for i in data:
                    if i["id_partida"] == int(id_partida):
                        pass
                    else:
                        data.append({"id_partida": int(id_partida), "nombre_partida": nombre_partida})
            

    print(data)

set()


## Datos partidas debe ser un diccionario indexado por el ID de cada partida, y que contenga los datos
## de todos los subtítulos de esa partida. Es decir, la key es id_partida y el value los subtítulos de esa partida.
datos_partidas = dict()

def dict():
    pass

    

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
    print(partidas)
    # pass
    ## COMPLETAR AQUI
    ##
    ##
    ##



## 3. Construir función que imprima datos de los montos totales originales de cada partida, ordenados de mayor a menor.
##    Recibe como parámetros el conjunto de partidas existentes,
##    un diccionario con los datos de los subtítulos de cada partida y un parámetro de conversión de dólares a pesos.
def partidas_por_monto_original(partidas, datos_partidas, usd_a_clp):
    pass
    ## COMPLETAR AQUI
    ##
    ##
    ##





## 4. Agregar una función más que responda a una consulta definida por usted, usando los datos disponible en el archivo
##    Puede cambiar el nombre a la función, pero también deberá cambiarla en la opción 3 del menú.
def funcion_personalizada(partidas, datos_partidas, usd_a_clp):
    pass
    ## COMPLETAR AQUI
    ##
    ##
    ##



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
