import pandas as pd
import csv

df = pd.read_csv("ingredientes.txt", encoding = "ISO-8859-1")

print(df)
