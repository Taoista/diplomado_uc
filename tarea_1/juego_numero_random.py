import random

estado = True
intentos = 0
puntos = 0

numero = random.randrange(1,101)

get_nombre = input("Ingresa tu nombre: \n")

while estado == True:
    intentos = intentos + 1
    get_intento = input("Ingresa un numero que crees que es (0 para salir)\n")
    if get_intento.isdigit():
        
        if get_intento == 0:
            estado = False
        else:
            get_intento = int(get_intento)
            if numero == get_intento:
                print(f'Felicitaciones {get_nombre} lo lograste en {intentos} intentos')
                estado = False
            else:
                if get_intento < numero :
                    if ( numero - 5 ) <= get_intento:
                        print(f"Sorry ,{get_nombre}, ese no es pero estas a una distancia menor a 5")
                    elif ( numero - 10) <= get_intento:
                        print(f"Sorry {get_nombre}, ese no es pero estas a una distancia menor a 10")
                    elif ( numero - 20) <= get_intento:
                        print(f"Sorry {get_nombre}, ese no es pero estas a una distancia menor a 20")
                    else:
                        print("sigue siendo menor")
                else:
                    if (numero + 5) >= get_intento:
                        print(f"Sorry {get_nombre} ese no es pero estas a una distancia mayor a 5")
                    elif (numero + 10) >= get_intento:
                        print(f"Sorry ,{get_nombre}, ese no es pero estas a una distancia mayor a 10")
                    elif (numero + 20) >= get_intento:
                        print(f"Sorry ,{get_nombre}, ese no es pero estas a una distancia mayor a 20")
                    else:
                        print("es mucho mayor")

    else:
        print("no es numero")





    