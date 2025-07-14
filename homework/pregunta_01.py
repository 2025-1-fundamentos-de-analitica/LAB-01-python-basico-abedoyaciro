"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """

    ruta = "files/input/data.csv"

    with open(ruta, "r", encoding="utf-8") as archivo:
        suma = 0
        for linea in archivo:
            columnas = linea.strip().split("\t")
            if len(columnas) > 1:
                try:
                    valor = int(columnas[1])
                    suma += valor
                except ValueError:
                    continue
        return suma
