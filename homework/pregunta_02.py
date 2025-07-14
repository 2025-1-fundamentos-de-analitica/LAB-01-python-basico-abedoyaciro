"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """
    ruta = "files/input/data.csv"

    # Diccionario para contar las letras
    contador = {}

    with open(ruta, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            columnas = linea.strip().split("\t")
            if len(columnas) > 0:
                letra = columnas[0]
                if letra in contador:
                    contador[letra] += 1
                else:
                    contador[letra] = 1

    # Convertir a lista de tuplas y ordenar alfabéticamente
    resultado = sorted(contador.items())

    return resultado
