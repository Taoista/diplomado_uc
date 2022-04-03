import mysql.connector as db

def main():
    my_database = db.connect(
        host = "localhost",
        user = "root",
        passwd = "",
        database = "InfoAeropuertos" 
    )
    apuntador = my_database.cursor() 
    apuntador.execute(schema)

    sql  = "INSERT INTO Aeropuertos(id, ident, type, name, elevation_ft, municipality, score) \
            VALUES(%s, %s, %s,%s, %s, %s, %s)"

    data = [
        (39340, "SHCC", "heliport", 'Clinica Las Condes Heliport', 2461, "Santiago",25),
        (39379, "SHMA", "heliport", 'Clinica Santa Maria Heliport ', 2028, "Santiago",25),
        (39390, "SHPT", "heliport", 'Portillo Heliport', 9000, "Los Andes ",25)
    ]

    apuntador.executemany(sql, data)

    # my_database.commit()

    sql = f"SELECT * FROM Aeropuertos WHERE elevation_ft >5000"

    apuntador.execute(sql)
    filas = apuntador.fetchall()

    for i in filas:
        print(i)


if __name__ == "__main__":
    main()