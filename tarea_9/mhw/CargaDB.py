import mysql.connector as db
import csv
from Dataframes import *


def cargarActores():
    try:
        mydb = db.connect(
            host='localhost',
            user='root',
            passwd='',
            database='cine'
        )

        with open("actors.csv",encoding="utf-8") as csvfile:
            FILECSV = csv.reader(csvfile, delimiter=';')
            LISTCSV = []
            first = next(FILECSV)
            for t in FILECSV:
                LISTCSV.append(tuple([int(t[0]), t[1], t[2]]))



        cursor = mydb.cursor()
        SQL = "INSERT INTO actors(id, first_name, last_name)\
                VALUES (%s, %s, %s)"
        cursor.executemany(SQL, LISTCSV)
        mydb.commit()
        print("registros ACTORS insertados correctamente")
    except:
        print("ERROR-ACTORS db no existe y/o registros ya estan ingresados")


def cargarDirectores():
    try:
        mydb = db.connect(
            host='localhost',
            user='root',
            passwd='',
            database='cine'
        )

        with open("directors.csv",encoding="utf-8") as csvfile:
            FILECSV = csv.reader(csvfile, delimiter=';')
            LISTCSV = []
            first = next(FILECSV)
            for t in FILECSV:
                LISTCSV.append(tuple([int(t[0]), t[1], t[2]]))

        cursor = mydb.cursor()
        SQL = "INSERT INTO directors(id, first_name, last_name)\
                VALUES (%s, %s, %s)"
        cursor.executemany(SQL, LISTCSV)
        mydb.commit()
        print("registros DIRECTORS insertados correctamente")
    except:
        print("ERROR-DIRECTORS db no existe y/o registros ya estan ingresados")

    
def cargarMoviesActores():
    try:
        mydb = db.connect(
            host='localhost',
            user='root',
            passwd='',
            database='cine'
        )
        with open("movies_actors.csv",encoding="utf-8") as csvfile:
            FILECSV = csv.reader(csvfile, delimiter=';')
            LISTCSV = []
            first = next(FILECSV)
            for t in FILECSV:
                LISTCSV.append(tuple([int(t[0]), t[1], t[2]]))

        cursor = mydb.cursor()
        SQL = "INSERT INTO movies_actors(actor_id, movie_id, role)\
                VALUES (%s, %s, %s)"
        cursor.executemany(SQL, LISTCSV)
        mydb.commit()
        print("registros MOVIES_ACTORS insertados correctamente")
    except:
        print("ERROR-MOVIES_ACTORS db no existe y/o registros ya estan ingresados")

def cargarMoviesDirectores():
    try:
        mydb = db.connect(
            host='localhost',
            user='root',
            passwd='',
            database='cine'
        )

        with open("movies_directors.csv",encoding="utf-8") as csvfile:
            FILECSV = csv.reader(csvfile, delimiter=';')
            LISTCSV = []
            first = next(FILECSV)
            for t in FILECSV:
                LISTCSV.append(tuple([int(t[0]), int(t[1])]))

        cursor = mydb.cursor()
        SQL = "INSERT INTO movies_directors(director_id, movie_id)\
                VALUES (%s, %s)"
        cursor.executemany(SQL, LISTCSV)
        mydb.commit()
        print("registros MOVIES_DIRECTORS insertados correctamente")
    except:
        print("ERROR-MOVIES_DIRECTORS db no existe y/o registros ya estan ingresados")

def inertarMovies():
    try:
        mydb = db.connect(
            host='localhost',
            user='root',
            passwd='',
            database='cine'
        )

        with open("movies.csv",encoding="utf-8") as csvfile:
            FILECSV = csv.reader(csvfile, delimiter=';')
            LISTCSV = []
            next(FILECSV)
            next(FILECSV)
            for t in FILECSV:
                LISTCSV.append(tuple([int(t[0]), t[1], int(t[2]), t[3]]))

        cursor = mydb.cursor()
        SQL = "INSERT INTO movies(id, name, year, ranking) VALUES (%s, %s, %s, %s)"
        cursor.executemany(SQL, LISTCSV)

        mydb.commit()
        print("registros MOVIES insertados correctamente")
    except:
        print("ERROR-MOVIES db no existe y/o registros ya estan ingresados")



if __name__ == '__main__':
    cargarActores()
    cargarDirectores()
    cargarMoviesActores()
    cargarMoviesDirectores()
    inertarMovies()
    respuesta_1(3)
    respuesta_2(3)