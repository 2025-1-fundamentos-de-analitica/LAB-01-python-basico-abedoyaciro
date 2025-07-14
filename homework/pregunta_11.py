"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """
    # Ruta del archivo de datos
    ruta = "files/input/data.csv"
    
    # Diccionario para acumular la suma por cada letra de la columna 4
    suma_por_letra = {}
    
    # Leer el archivo línea por línea
    with open(ruta, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            # Separar las columnas por tabulador
            columnas = linea.strip().split("\t")
            
            # Verificar que la línea tenga al menos 4 columnas
            if len(columnas) >= 4:
                try:
                    # Obtener el valor de la columna 2 (índice 1)
                    valor_col2 = int(columnas[1])
                    
                    # Obtener las letras de la columna 4 (índice 3)
                    columna_4 = columnas[3]
                    
                    # Separar las letras por comas
                    letras = columna_4.split(",")
                    
                    # Sumar el valor de la columna 2 a cada letra de la columna 4
                    for letra in letras:
                        # Limpiar espacios en blanco si los hay
                        letra = letra.strip()
                        
                        # Acumular la suma para esta letra
                        if letra in suma_por_letra:
                            suma_por_letra[letra] += valor_col2
                        else:
                            suma_por_letra[letra] = valor_col2
                            
                except ValueError:
                    # Ignorar líneas donde la columna 2 no sea un número
                    continue
    
    # Ordenar el diccionario por clave alfabéticamente
    # Crear un nuevo diccionario ordenado
    resultado = {}
    for letra in sorted(suma_por_letra.keys()):
        resultado[letra] = suma_por_letra[letra]
    
    return resultado
