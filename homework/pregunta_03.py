"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

    """
    ruta = "files/input/data.csv"

    # Diccionario para sumar los valores por letra
    sumas = {}

    with open(ruta, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            columnas = linea.strip().split("\t")
            if len(columnas) > 1:
                letra = columnas[0]
                try:
                    valor = int(columnas[1])
                    if letra in sumas:
                        sumas[letra] += valor
                    else:
                        sumas[letra] = valor
                except ValueError:
                    continue

    # Convertir a lista de tuplas y ordenar alfabéticamente
    resultado = sorted(sumas.items())

    return resultado
