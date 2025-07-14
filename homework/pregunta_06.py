"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """
    # Ruta del archivo de datos
    ruta = "files/input/data.csv"
    
    # Diccionario para almacenar todos los valores de cada clave
    # Cada clave tendrá una lista de valores
    valores_por_clave = {}
    
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
                        clave, valor_str = par.split(":")
                        
                        try:
                            # Convertir el valor a entero
                            valor = int(valor_str)
                            
                            # Agregar el valor a la lista de la clave correspondiente
                            if clave in valores_por_clave:
                                valores_por_clave[clave].append(valor)
                            else:
                                valores_por_clave[clave] = [valor]
                                
                        except ValueError:
                            # Ignorar valores que no sean números
                            continue
    
    # Calcular mínimo y máximo para cada clave
    resultado = []
    for clave in sorted(valores_por_clave.keys()):
        valores = valores_por_clave[clave]
        minimo = min(valores)  # Valor mínimo
        maximo = max(valores)  # Valor máximo
        
        # Agregar tupla (clave, mínimo, máximo)
        resultado.append((clave, minimo, maximo))
    
    return resultado
