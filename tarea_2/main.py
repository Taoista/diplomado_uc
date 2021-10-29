import random


def create_tablero():
    tablero = list()
    
    for i in range(1,21):
        tablero.append([i,2,1,3,"BULL","DOBLE BULL"])

    return tablero
    
def lanzar_dardo():
    return random.randint(0,20)

def start_users():
    user_1 = ""
    user_2 = ""
    usuarios = list()
    while user_1 == "":
        if user_1 == "":
            user_1 = input("Ingresa tu nombre para iniciar el juego : ")
            # user_1 = user_1[0:3].upper()
        if  len(user_1) < 3 or len(user_1) > 10:
            print("Tu nombre no debe contener menos de 3 caracteres y mayor a 10")
            user_1 = ""
        user_1 = user_1[0:3].upper()
    usuarios.append([user_1,501])
    while user_2 == "":
        if user_2 == "":
            user_2 = input("Ingresa tu nombre (2do Jugador) : ")
        if len(user_2) < 3 or len(user_2) > 10:
            print("Tu nombre no debe contener menos de 3 caracteres y mayor a 10")
            user_2 = ""
        if user_2[0:3].upper() == user_1:
            user_2 = user_2[0:3].upper()+"2"
        else:
            user_2 = user_2[0:3].upper()
        usuarios.append([user_2,501])
        
    return usuarios

def tiros_usaurio(tablero):
    puntaje = 501
    suma_puntaje = 0
    intentos = 0
    while intentos < 3:
        dardo = lanzar_dardo()
        # print(f'lanzando dardo {dardo}')
        if dardo == 0:
            print("fallaste salio del tablero")
        else:
            # print("------------ENTRO AL TABLERO--------")
            index_mult = random.randint(1,4)
            achuntador = tablero[dardo-1]
            if achuntador[index_mult] == "BULL":
                suma_puntaje += 25
                print("SINGLE BULL")
            elif achuntador[index_mult] == "DOBLE BULL":
                print("DOUBLE BULL")
                suma_puntaje += 50
            else:
                print(f"{index_mult} {achuntador[index_mult]}")
                suma_puntaje += achuntador[index_mult] * achuntador[0]

        intentos +=1
    return suma_puntaje


def main():
    print('---------LANZADOR DE DARDOS MANCOIBER---------')
    tablero = create_tablero()
    
    # for i in tablero:
    #     print(i)

    user_1 = ""
    user_2 = ""
    inicio = start_users()

    text_user_1 = inicio[0][0]+" "+str(inicio[0][1])
    text_user_2 = inicio[1][0]+" "+str(inicio[1][1]) 

    user_1 = inicio[0]
    user_2 = inicio[1]
    print(f'-----tiros del usuario {user_1[0]} ----')
    tiros_1 = tiros_usaurio(tablero)
    print(f'-----tiros del usuario {user_2[0]} ----')
    tiros_2 = tiros_usaurio(tablero)

    print("----------RESULTADOS----------")

    if tiros_1 == 0:
        print(f'Felicitaciones {user_1[0]}, ganaste')
    elif tiros_1 < 0:
        print(f'el usuario {user_1[0]} total de puntos lanzados {tiros_1}, resultados {((user_1[1] - tiros_1) * -1 ) }')
    else:
        print(f'el usuario {user_1[0]} total de puntos lanzados {tiros_1}, resultados {user_1[1] - tiros_1 }')

    if tiros_2 == 0:
        print(f' Felicitaciones {user_2[0]}, ganaste')
    elif tiros_1 < 0:
        print(f'el usuario {user_2[0]} total de puntos lanzados {tiros_2}, resultados {((user_2[1] - tiros_2) * -1 ) }')
    else:
        print(f'el usuario {user_2[0]} total de puntos lanzados {tiros_2}, resultados {user_2[1] - tiros_2 }')

  
  
    
    
    


if __name__ == "__main__":
    main()

