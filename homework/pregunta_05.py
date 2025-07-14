"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    # Ruta del archivo de datos
    ruta = "files/input/data.csv"
    
    # Diccionario para almacenar valores por letra
    # Cada letra tendrá una lista de valores de la columna 2
    valores_por_letra = {}
    
    # Leer el archivo línea por línea
    with open(ruta, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            # Separar las columnas por tabulador
            columnas = linea.strip().split("\t")
            
            # Verificar que la línea tenga al menos 2 columnas
            if len(columnas) >= 2:
                letra = columnas[0]  # Primera columna (letra)
                
                try:
                    # Convertir el valor de la segunda columna a entero
                    valor = int(columnas[1])
                    
                    # Agregar el valor a la lista de la letra correspondiente
                    if letra in valores_por_letra:
                        valores_por_letra[letra].append(valor)
                    else:
                        valores_por_letra[letra] = [valor]
                        
                except ValueError:
                    # Ignorar líneas donde la columna 2 no sea un número
                    continue
    
    # Calcular máximo y mínimo para cada letra
    resultado = []
    for letra in sorted(valores_por_letra.keys()):
        valores = valores_por_letra[letra]
        maximo = max(valores)  # Valor máximo
        minimo = min(valores)  # Valor mínimo
        
        # Agregar tupla (letra, máximo, mínimo)
        resultado.append((letra, maximo, minimo))
    
    return resultado
