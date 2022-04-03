import mysql.connector as db

def main():
    base_de_datos = "InfoAeropuertos"
    base_consulta = 5000

    try:
        mydb = db.connect(
            host = "localhost",
            user = "root",
            passwd = "",
            database = f"{base_de_datos}" 
        )
        puntero = mydb.cursor() 
        print("Base de datos conectada")
    except:
        mydb = db.connect(
            host = "localhost",
            user = "root",
            passwd = "",
            database = "" 
        )
        schema = f'CREATE DATABASE {base_de_datos}' 
        puntero = mydb.cursor() 
        puntero.execute(schema)
        print("Base de datos creada")

   

    sql  = "INSERT INTO Aeropuertos(id, ident, type, name, elevation_ft, municipality, score) \
                    VALUES(%s, %s, %s,%s, %s, %s, %s)"

    datos_tupla = [
        (39340, "SHCC", "heliport", 'Clinica Las Condes Heliport', 2461, "Santiago",25),
        (39379, "SHMA", "heliport", 'Clinica Santa Maria Heliport ', 2028, "Santiago",25),
        (39390, "SHPT", "heliport", 'Portillo Heliport', 9000, "Los Andes ",25)
    ]

    puntero.executemany(sql, datos_tupla)

    # mydb.commit()

    busqueda = f"SELECT * FROM Aeropuertos WHERE elevation_ft > {base_consulta}"

    puntero.execute(busqueda)
    rows = puntero.fetchall()

    for row in rows:
        print(row)




if __name__ == "__main__":
    main()