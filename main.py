import shutil
import os
import re
import datetime
from pathlib import Path

fecha_actual = datetime.date.today()
patron = r"N\D{3}-\d{5}"
ruta = 'C:\\Users\\loist\\Desktop\\LectorDirectorios\\CarpetaEjemplo'

archivo_encontrados = []
patron_encontrado = []

def buscar_patron(archivo,patron):
    with open(archivo,'r') as f:
        texto = f.read()
    if re.search(patron,texto):
        return re.search(patron,texto)
    else:
        return ''

def crear_lista():
    for carpeta, subcarpeta, archivo in os.walk(ruta):
        for i in archivo:
            resultado = buscar_patron(Path(carpeta,i), patron)
            if resultado != '':
                archivo_encontrados.append(i.title())
                patron_encontrado.append(resultado.group())


def decorador():
    indice = 0
    print("-" * 50)
    print(f"Fecha Busqueda: {fecha_actual.day}/{fecha_actual.month}/{fecha_actual.year}")
    print("\n")
    print("Archivo\t\t\tPatron")
    print("-------\t\t\t------")
    for i in archivo_encontrados:
        print(f"{i}\t{patron_encontrado[indice]}")
        indice += 1
    print("\n")
    print(f"Patrones Encontrados: {len(patron_encontrado)}")
    print("-" * 50)

crear_lista()
decorador()

