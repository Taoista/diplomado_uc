import pandas as pd
import mysql.connector as db


def main():
    mydb = db.connect(
        host='127.0.0.1',
        user='root',
        passwd='',
        database='Energia'#no existe
    )
    #leyendo un archivo csv directamente a un datagrame
    df1 = pd.read_csv("data/personas3.csv", seip=";")
    df2 = df1[["nombre", "rut", "fecha_nac"]]

    tupla_list = [tuple(l) for l in df.values.toList()]



def main():
    print("iniciando")


if __name__ == "__main__":
    main()