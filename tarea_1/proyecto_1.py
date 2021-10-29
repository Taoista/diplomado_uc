import random

#variables
estado = True
intentos = 0
puntos = 0
#fin variable


numero = random.randrange(1,101)

variable_nombre = input("Ingresa tu nombre: ")

while estado == True:
    variable_numero = input(" Ingresa un número que representa un intento de adivinar el número: (o el cero para salir) \n").replace(" ","")

    intentos = intentos +1

    if variable_numero.isdigit() : 
        variable_numero = int(variable_numero)
        if variable_numero == 0:
            print(f"Saliste del juego, bye {variable_nombre}")
            estado = False
        else:
            if numero == variable_numero:
                print("Felicitaciones ", variable_nombre,"lo lograste en " ,intentos," intentos")
                estado = False
            else:

                if variable_numero < numero:
                    if (numero-5) <=variable_numero:
                        print("Sorry" ,variable_nombre, "ese no es pero estas a una distancia menor a 5") 
                    elif (numero-10) <=variable_numero:
                        print("Sorry" ,variable_nombre, "ese no es pero estas a una distancia menor a 10")
                    elif (numero-20) <=variable_numero:
                        print("Sorry" ,variable_nombre, "ese no es pero estas a una distancia menor a 20")      

                    else:
                        print("sigue siendo menor")
                else:
                    if (numero + 5) >= variable_numero:
                        print("Sorry" ,variable_nombre, "ese no es pero estas a una distancia mayor a 5")
                    elif (numero + 10) >= variable_numero:
                        print("Sorry" ,variable_nombre, "ese no es pero estas a una distancia mayor a 10")
                    elif (numero + 10) >= variable_numero:
                        print("Sorry" ,variable_nombre, "ese no es pero estas a una distancia mayor a 10")
                    else:
                        print("es muchisimo mayor")


        
    else :
        print ("no es un numero")





