"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla
    contiene un valor posible de la columna 2 y una lista con todas las letras
    asociadas (columna 1) a dicho valor de la columna 2.

    Rta/
    [(0, ['C']),
     (1, ['E', 'B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E', 'E', 'D']),
     (4, ['E', 'B']),
     (5, ['B', 'C', 'D', 'D', 'E', 'E', 'E']),
     (6, ['C', 'E', 'A', 'B']),
     (7, ['A', 'C', 'E', 'D']),
     (8, ['E', 'D', 'E', 'A', 'B']),
     (9, ['A', 'B', 'E', 'A', 'A', 'C'])]

    """
    # Ruta del archivo de datos
    ruta = "files/input/data.csv"
    
    # Diccionario para asociar valores de columna 2 con letras de columna 1
    # Cada valor tendrá una lista de letras (pueden repetirse)
    letras_por_valor = {}
    
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
                    
                    # Agregar la letra a la lista del valor correspondiente
                    if valor in letras_por_valor:
                        letras_por_valor[valor].append(letra)
                    else:
                        letras_por_valor[valor] = [letra]
                        
                except ValueError:
                    # Ignorar líneas donde la columna 2 no sea un número
                    continue
    
    # Convertir a lista de tuplas y ordenar por valor
    resultado = []
    for valor in sorted(letras_por_valor.keys()):
        letras = letras_por_valor[valor]
        
        # Agregar tupla (valor, lista_de_letras)
        # Nota: las letras mantienen el orden de aparición y pueden repetirse
        resultado.append((valor, letras))
    
    return resultado
