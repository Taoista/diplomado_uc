import mysql.connector as db
import csv
from Querys import *

def conector():
    try:
        mydb = db.connect(
            host='localhost',
            user='root',
            passwd='',
            database='cine'
        )
        return mydb
    except:
        return "--- DB no existe, selecciona otra opcion --"

def insertActors():
    mydb = db.connect(
            host='localhost',
            user='root',
            passwd='',
            database='cine'
    )
    try:
        with open("actors.csv",encoding="utf-8") as csvfile:
            fileCsv = csv.reader(csvfile, delimiter=';')
            lista = list()
            first = next(fileCsv)
            for row in fileCsv:
                lista.append(tuple([int(row[0]), row[1], row[2]]))
        cursor = mydb.cursor()
        sql = "INSERT INTO actors(id, first_name, last_name) VALUES (%s, %s, %s)"
        cursor.executemany(sql, lista)
        mydb.commit()
        print("---- final exitoso-----")
    except:
        print("---- Error, intente crear db para continuar y/o los datos ya estan ingresados -----")


def insertDirectors():
    mydb = db.connect(
        host='localhost',
        user='root',
        passwd='',
        database='cine'
    )
    try:
        with open("directors.csv",encoding="utf-8") as csvfile:
            fileCsv = csv.reader(csvfile, delimiter=';')
            lista = list()
            first = next(fileCsv)
            for row in fileCsv:
                lista.append(tuple([int(row[0]), row[1], row[2]]))

            cursor = mydb.cursor()
            sql = "INSERT INTO directors(id, first_name, last_name) VALUES (%s, %s, %s)"
            cursor.executemany(sql, lista)
            mydb.commit()
            print("insert_correct")
    except:
        print("error")
    
def insertMoviesActors():
    mydb = db.connect(
        host='localhost',
        user='root',
        passwd='',
        database='cine'
    )
    try:
        with open("movies_actors.csv",encoding="utf-8") as csvfile:
            fileCsv = csv.reader(csvfile, delimiter=';')
            lista = list()
            first = next(fileCsv)
            for row in fileCsv:
                lista.append(tuple([int(row[0]), row[1], row[2]]))

            cursor = mydb.cursor()
            sql = "INSERT INTO movies_actors(actor_id, movie_id, role) VALUES (%s, %s, %s)"
            cursor.executemany(sql, lista)
            mydb.commit()
    except:
        print("error")


def cargaMoviesDirectors():
    mydb = db.connect(
        host='localhost',
        user='root',
        passwd='',
        database='cine'#no existe
    )

    with open("movies_directors.csv",encoding="utf-8") as csvfile:
        fileCsv = csv.reader(csvfile, delimiter=';')
        lista_csv = list()
        first = next(fileCsv)
        for row in fileCsv:
            lista_csv.append(tuple([int(row[0]), int(row[1])]))

        cursor = mydb.cursor()
        sql = "INSERT INTO movies_directors(director_id, movie_id) VALUES (%s, %s)"
        cursor.executemany(sql, lista_csv)
        mydb.commit()
        

def insertMovies():
    mydb = db.connect(
        host='localhost',
        user='root',
        passwd='',
        database='cine'#no existe
    )

    with open("movies.csv",encoding="utf-8") as csvfile:
        fileCsv = csv.reader(csvfile, delimiter=';')
        lista = list()
        next(fileCsv)
        next(fileCsv)
        for row in fileCsv:
            lista.append(tuple([int(row[0]), row[1], int(row[2]), row[3]]))
       

        cursor = mydb.cursor()
        sql = "INSERT INTO movies(id, name, year, ranking) VALUES (%s, %s, %s, %s)"
        cursor.executemany(sql, lista)

        mydb.commit()

def crearBasedeDatos():
    try:
        mydb = db.connect(
            host='localhost',
            user='root',
            passwd='',
            database='cine'
        )
        print("-----------------------------")
        print("====> BASE DE DATOS CREDA <====
        print("-----------------------------")
        cursor = mydb.cursor()
    except:
        mydb = db.connect(
            host='localhost',
            user='root',
            passwd='',
            database=''
        )
        schema = 'CREATE DATABASE IF NOT EXISTS cine' 
        cursor = mydb.cursor() 
        cursor.execute(schema)
        mydb = db.connect(
            host='localhost',
            user='root',
            passwd='',
            database='cine'
        )
        cursor = mydb.cursor()
        print("-----------------------------")
        print("====> BASE DE DATOS CREDA <====
        print("-----------------------------")

    sqlCreateTable = " CREATE TABLE IF NOT EXISTS movies(\
                                id INTEGER PRIMARY KEY AUTO_INCREMENT,\
                                name VARCHAR(100),\
                                year INTEGER(4),\
                                ranking VARCHAR(5)\
    )"
    cursor.execute(sqlCreateTable)

    sqlCreateTable2 = "CREATE TABLE IF NOT EXISTS actors(\
                        id INTEGER PRIMARY KEY AUTO_INCREMENT,\
                        first_name VARCHAR(100),\
                        last_name VARCHAR(100)\
    )"
    cursor.execute(sqlCreateTable2)

    sqlCreateTable3 = "CREATE TABLE IF NOT EXISTS directors(\
                        id INTEGER PRIMARY KEY AUTO_INCREMENT,\
                        first_name VARCHAR(100),\
                        last_name VARCHAR(100)\
    )"
    cursor.execute(sqlCreateTable3)

    sqlCreateTable4 = "CREATE TABLE IF NOT EXISTS movies_actors(\
            actor_id INTEGER NOT NULL,\
            movie_id INTEGER NOT NULL,\
            role VARCHAR(100) NOT NULL\
    )"
    
    cursor.execute(sqlCreateTable4)

    sqlCreateTable5 = "CREATE TABLE IF NOT EXISTS movies_directors(\
            director_id INTEGER NOT NULL,\
            movie_id INTEGER NOT NULL\
    )"
    
    cursor.execute(sqlCreateTable5)



def main():
    inicio = True
    while inicio == True:
        try:
            select = int(input("""
                                Selecciona que hacer:
                                ____________________________
                                1 - CREAR base de datos
                                2 - Insertar Datos -> actors
                                3 - Consulta datos -> 3.1
                                4 - Consulta datos -> 3.2
                                5 - Consulta datos -> 3.3
                                0 - SALIR
                                +++++++++++++++++++++++++++++
                                \n"""))
            if select == 1:
               print("crear base de datos....")
               crearBasedeDatos()
            elif select == 2:
                try:
                    insertActors()
                    insertDirectors()
                    insertMoviesActors()
                    cargaMoviesDirectors()
                    insertMovies()
                except:
                    print(conector())
            elif select == 3:
                datos = resultados(1)
                df = pd.DataFrame(datos, columns = ["Pelicula", "Agno", "Directo", "Puntaje"])
                print(df.loc[:10])
                print("------ TERMINO LOC DB-------")
            elif select == 4:
                data = resultados(2)
                df = pd.DataFrame(datas, columns = ["Pelicula", "Agno", "Directo", "Puntaje"])
                print(df.iloc[20:50])
                print("------ TERMINO ILOC DF -------")
            elif select == 5:
                data = resultados(3)
                for i in data:
                    print(i)
                print("------ TERMINO FOR-------")
            elif select == 0:
                print("Selecionaste salir del programa")
                inicio = False
        except:
            print("Ocurrio un error intente nuevamente \n")
    
    

if __name__ == '__main__':
    main()