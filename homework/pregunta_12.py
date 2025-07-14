"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
    # Ruta del archivo de datos
    ruta = "files/input/data.csv"
    
    # Diccionario para acumular la suma de valores por letra
    suma_por_letra = {}
    
    # Leer el archivo línea por línea
    with open(ruta, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            # Separar las columnas por tabulador
            columnas = linea.strip().split("\t")
            
            # Verificar que la línea tenga al menos 5 columnas
            if len(columnas) >= 5:
                letra = columnas[0]      # Primera columna (letra)
                columna_5 = columnas[4]  # Quinta columna (índice 4)
                
                # Separar los pares clave:valor por comas
                pares = columna_5.split(",")
                
                # Suma total de valores para esta línea
                suma_linea = 0
                
                # Procesar cada par clave:valor
                for par in pares:
                    # Separar clave y valor por ':'
                    if ":" in par:
                        _, valor_str = par.split(":", 1)  # Solo dividir en la primera ':'
                        
                        try:
                            # Convertir el valor a entero y sumarlo
                            valor = int(valor_str)
                            suma_linea += valor
                            
                        except ValueError:
                            # Ignorar valores que no sean números
                            continue
                
                # Acumular la suma de esta línea a la letra correspondiente
                if letra in suma_por_letra:
                    suma_por_letra[letra] += suma_linea
                else:
                    suma_por_letra[letra] = suma_linea
    
    # Ordenar el diccionario por clave alfabéticamente
    # Crear un nuevo diccionario ordenado
    resultado = {}
    for letra in sorted(suma_por_letra.keys()):
        resultado[letra] = suma_por_letra[letra]
    
    return resultado
