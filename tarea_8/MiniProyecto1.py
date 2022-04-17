import mysql.connector as db

def main():
    try:
        mydb = db.connect(
            host = "localhost",
            user = "root",
            passwd = "",
            database = "InfoAeropuertos"
        )
        print("contado a la base de datos")
    except:
        mydb = db.connect(
            host = "localhost",
            user = "root",
            passwd = "",
            database = ""
        )
        print("conexion sin db")

    sql_create = """
        CREATE DATABASE IF NOT EXISTS InfoAeropuertos
    """

    cursor = mydb.cursor() 
    cursor.execute(sql_create)

    sql_create_table = """ CREATE TABLE IF NOT EXISTS Aeropuertos(
          id INTEGER AUTO_INCREMENT PRIMARY KEY,
            ident VARCHAR(4) NOT NULL,
            type VARCHAR(8) NOT NULL,
            name VARCHAR(50) NOT NULL,
            elevation_ft FLOAT NOT NULL,
            municipality VARCHAR(50),
            iata_code INT(10) NOT NULL,
            score INT(10)
    )
    """
    cursor.execute(sql_create_table)
    

    sql_insert = """
        INSERT INTO Aeropuertos(id, ident, type, name, elevation_ft, municipality, score) 
        VALUES(%s, %s, %s,%s, %s, %s, %s)
    """

    datos = [
        (39340, "SHCC", "heliport", 'Clinica Las Condes Heliport', 2461, "Santiago",25),
        (39379, "SHMA", "heliport", 'Clinica Santa Maria Heliport ', 2028, "Santiago",25),
        (39390, "SHPT", "heliport", 'Portillo Heliport', 9000, "Los Andes ",25)
    ]

    for i in datos:
        cursor.execute(sql_insert, i)

    #### descomentar para ejecutar pero ya los contiene
    # mydb.commit()

    sql_search = "SELECT name, type, municipality, elevation_ft FROM Aeropuertos WHERE elevation_ft > 5000"

    cursor.execute(sql_search)
    rows = cursor.fetchall()

    for row in rows:
        print(row)




if __name__ == "__main__":
    main()