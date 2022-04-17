import mysql.connector as db
import csv
from Querys import *
import pandas as pd


def main_1():
    datas = querys()

    df = pd.DataFrame(datas, columns = ["Pelicula", "Agno", "Directo", "Puntaje"])

    print(df.loc[:10])

def main_2():
    datas = querys()

    df = pd.DataFrame(datas, columns = ["Pelicula", "Agno", "Directo", "Puntaje"])

    print(df.iloc[20:50])


if __name__ == '__main__':
    main_1()
    main_2()