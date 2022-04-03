# version de PYTHON 3.8.0 (jamas usar ultima version ojala dos anterior a la ultima)
# 1 - se debe instalar el modulo mysql para trabajar 
# 
# 
# 

import mysql.connector as db

mydb = db.connect(
    host = "localhost", # este es el host o el servidor donde se va conectar, como no se tiene un servidro se usa el local
    user = "root",
    passwd = "",
    database = "basededatosenpython" # se va crear la base de datos por ende no se inserta
)

# objeto que permite interactuar con la base de datos
my_cursor = mydb.cursor() 

# es la sentencia o la query que se guarda en una variable

sql = " CREATE DATABASE IF NOT EXISTS basededatosenpython"

#ejecutar 
my_cursor.execute(sql)

sql2 = """
    CREATE TABLE IF NOT EXISTS users(
    name VARCHAR(45),
    email VARCHAR(45),
    age INTEGER(10),
    user_id INTEGER AUTO_INCREMENT PRIMARY KEY)
"""

my_cursor.execute(sql2)

#INSERTAR datos

sql3 = "INSERT INTO users(name, email, age) VALUES (%s, %s, %s)"

data = ("Pepe", "pepe@gmail.com", 33)

datas = [
    ("demo1", "demo1@gmail.com", 34),
    ("demo2", "demo2@gmail.com", 35),
    ("demo3", "demo3@gmail.com", 36)
]

#descomentar para insertar
# for i in datas:
#     my_cursor.execute(sql3, i)
# este si me funciono
# my_cursor.execute(sql3, datas)

# mydb.commit()

sql = "SELECT * FROM users"

my_cursor.execute(sql)
# rows = my_cursor.fetchall() # toma todo
# rows = my_cursor.fetchone() # toma la primera
rows = my_cursor.fetchmany(2) # toma la primera

for row in rows:
    print(row)


print("TABLA CREADA")