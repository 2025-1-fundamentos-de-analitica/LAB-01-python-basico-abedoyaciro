"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla
    contiene  el valor de la segunda columna; la segunda parte de la tupla
    es una lista con las letras (ordenadas y sin repetir letra) de la
    primera  columna que aparecen asociadas a dicho valor de la segunda
    columna.

    Rta/
    [(0, ['C']),
     (1, ['B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E']),
     (4, ['B', 'E']),
     (5, ['B', 'C', 'D', 'E']),
     (6, ['A', 'B', 'C', 'E']),
     (7, ['A', 'C', 'D', 'E']),
     (8, ['A', 'B', 'D', 'E']),
     (9, ['A', 'B', 'C', 'E'])]

    """
    # Ruta del archivo de datos
    ruta = "files/input/data.csv"
    
    # Diccionario para asociar valores de columna 2 con conjuntos de letras
    # Usar conjuntos (set) para evitar duplicados
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
                    
                    # Agregar la letra al conjunto del valor correspondiente
                    if valor in letras_por_valor:
                        letras_por_valor[valor].add(letra)
                    else:
                        letras_por_valor[valor] = {letra}  # Crear nuevo conjunto
                        
                except ValueError:
                    # Ignorar líneas donde la columna 2 no sea un número
                    continue
    
    # Convertir a lista de tuplas y ordenar por valor
    resultado = []
    for valor in sorted(letras_por_valor.keys()):
        letras_conjunto = letras_por_valor[valor]
        
        # Convertir conjunto a lista ordenada (sin duplicados)
        letras_ordenadas = sorted(list(letras_conjunto))
        
        # Agregar tupla (valor, lista_de_letras_ordenadas_sin_duplicados)
        resultado.append((valor, letras_ordenadas))
    
    return resultado
