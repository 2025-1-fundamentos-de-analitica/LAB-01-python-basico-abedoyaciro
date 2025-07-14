"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """
    # Ruta del archivo de datos
    ruta = "files/input/data.csv"
    
    # Diccionario para contar apariciones de cada clave
    contador_claves = {}
    
    # Leer el archivo línea por línea
    with open(ruta, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            # Separar las columnas por tabulador
            columnas = linea.strip().split("\t")
            
            # Verificar que la línea tenga al menos 5 columnas
            if len(columnas) >= 5:
                # La columna 5 (índice 4) contiene los pares clave:valor
                columna_5 = columnas[4]
                
                # Separar los diferentes pares por coma
                pares = columna_5.split(",")
                
                # Procesar cada par clave:valor
                for par in pares:
                    # Separar clave y valor por ':'
                    if ":" in par:
                        clave, _ = par.split(":", 1)  # Solo dividir en la primera ':'
                        
                        # Contar la aparición de esta clave
                        if clave in contador_claves:
                            contador_claves[clave] += 1
                        else:
                            contador_claves[clave] = 1
    
    # Ordenar el diccionario por clave alfabéticamente
    # Crear un nuevo diccionario ordenado
    resultado = {}
    for clave in sorted(contador_claves.keys()):
        resultado[clave] = contador_claves[clave]
    
    return resultado
