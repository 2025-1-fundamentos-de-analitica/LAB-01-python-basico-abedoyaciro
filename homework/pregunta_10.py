"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]


    """
    # Ruta del archivo de datos
    ruta = "files/input/data.csv"
    
    # Lista para almacenar los resultados
    resultado = []
    
    # Leer el archivo línea por línea
    with open(ruta, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            # Separar las columnas por tabulador
            columnas = linea.strip().split("\t")
            
            # Verificar que la línea tenga al menos 5 columnas
            if len(columnas) >= 5:
                letra = columnas[0]      # Primera columna (letra)
                columna_4 = columnas[3]  # Cuarta columna (índice 3)
                columna_5 = columnas[4]  # Quinta columna (índice 4)
                
                # Contar elementos en columna 4
                # Los elementos están separados por comas
                elementos_col4 = columna_4.split(",")
                cantidad_col4 = len(elementos_col4)
                
                # Contar elementos en columna 5
                # Los elementos son pares clave:valor separados por comas
                elementos_col5 = columna_5.split(",")
                cantidad_col5 = len(elementos_col5)
                
                # Agregar tupla (letra, cantidad_col4, cantidad_col5)
                resultado.append((letra, cantidad_col4, cantidad_col5))
    
    return resultado
