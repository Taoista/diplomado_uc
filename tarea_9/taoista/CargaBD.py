import mysql.connector as db
import csv

def carga_actors():
    #cargan los archivos csv
    mydb = db.connect(
        host='localhost',
        user='root',
        passwd='',
        database='cine'#no existe
    )

    with open("actors.csv",encoding="utf-8") as csvfile:
        file_csv = csv.reader(csvfile, delimiter=';')
        lista_actores = list()
        first = next(file_csv)
        for row in file_csv:
            lista_actores.append(tuple([int(row[0]), row[1], row[2]]))



    cursor = mydb.cursor()
    sql = "INSERT INTO actors(id, first_name, last_name) VALUES (%s, %s, %s)"
    cursor.executemany(sql, lista_actores)
    mydb.commit()
    print("== termino del INSERT actors ==")


def carga_directors():
    mydb = db.connect(
        host='localhost',
        user='root',
        passwd='',
        database='cine'#no existe
    )

    with open("directors.csv",encoding="utf-8") as csvfile:
        file_csv = csv.reader(csvfile, delimiter=';')
        lista_csv = list()
        first = next(file_csv)
        for row in file_csv:
            lista_csv.append(tuple([int(row[0]), row[1], row[2]]))

        cursor = mydb.cursor()
        sql = "INSERT INTO directors(id, first_name, last_name) VALUES (%s, %s, %s)"
        cursor.executemany(sql, lista_csv)
        mydb.commit()
        print("== termino del INSERT directors ==")
    
def cargar_movies_actors():
    mydb = db.connect(
        host='localhost',
        user='root',
        passwd='',
        database='cine'#no existe
    )
    with open("movies_actors.csv",encoding="utf-8") as csvfile:
        file_csv = csv.reader(csvfile, delimiter=';')
        lista_csv = list()
        first = next(file_csv)
        for row in file_csv:
            lista_csv.append(tuple([int(row[0]), row[1], row[2]]))

        cursor = mydb.cursor()
        sql = "INSERT INTO movies_actors(actor_id, movie_id, role) VALUES (%s, %s, %s)"
        cursor.executemany(sql, lista_csv)
        mydb.commit()
        print("== termino del INSERT movies_actors ==")



def cargar_movies_directors():
    mydb = db.connect(
        host='localhost',
        user='root',
        passwd='',
        database='cine'#no existe
    )

    with open("movies_directors.csv",encoding="utf-8") as csvfile:
        file_csv = csv.reader(csvfile, delimiter=';')
        lista_csv = list()
        first = next(file_csv)
        for row in file_csv:
            lista_csv.append(tuple([int(row[0]), int(row[1])]))

        cursor = mydb.cursor()
        sql = "INSERT INTO movies_directors(director_id, movie_id) VALUES (%s, %s)"
        cursor.executemany(sql, lista_csv)
        mydb.commit()
        print("== termino del INSERT movies_directors ==")

def insert_movies():
    mydb = db.connect(
        host='localhost',
        user='root',
        passwd='',
        database='cine'#no existe
    )

    with open("movies.csv",encoding="utf-8") as csvfile:
        file_csv = csv.reader(csvfile, delimiter=';')
        lista_csv = list()
        next(file_csv)
        next(file_csv)
        for row in file_csv:
            lista_csv.append(tuple([int(row[0]), row[1], int(row[2]), row[3]]))


        for row in lista_csv:
            print(row)

        cursor = mydb.cursor()
        sql = "INSERT INTO movies(id, name, year, ranking) VALUES (%s, %s, %s, %s)"
        cursor.executemany(sql, lista_csv)

        mydb.commit()
        print("== termino del INSERT movies_directors ==")


if __name__ == '__main__':
    #ya esta ejecutada
    # carga_actors()
    #ya esta ejecutada
    # carga_directors()
    #ya estan insertados
    # cargar_movies_actors()
    #ya estan cargados
    # cargar_movies_directors()

    insert_movies()