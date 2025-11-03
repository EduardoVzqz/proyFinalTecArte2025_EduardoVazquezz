import pandas as pd
import math

from funciones import triangulo, rectangulo, circulo

dataFile = pd.read_csv("figuras.csv")

for index, row in dataFile.iterrows():
    figura = row['FIGURA'].strip().lower() 
    m1 = row['MEDIDA1']
    m2 = row['MEDIDA2']
    area = None

    if figura == 't':
        area = triangulo(m1, m2)
    elif figura == 'c':
        area = circulo(m1, m2)
    elif figura == 'r':
        area = rectangulo(m1, m2)

    if area is not None:
        print(f"FIGURA = {row['FIGURA']} Medida1 = {m1} Medida2 = {m2} Area = {area}")
    else:
        print(f"FIGURA = {row['FIGURA']} No se pudo calcular el área")

