import mysql.connector as db
import csv
from Querys import *
import pandas as pd

def respuesta_1(opt):
    """
    solo funciona con la opcion 3 :(
    """
    df = pd.DataFrame(query_selection(opt), columns = ["Pelicula", "Agno", "Directo", "Puntaje"])
    print(df.loc[:10])

def respuesta_2(opt):
    """
    solo funciona con la opcion 3 :(
    """
    df = pd.DataFrame(query_selection(opt), columns = ["Pelicula", "Agno", "Directo", "Puntaje"])
    print(df.iloc[20:50])
