"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la
    cantidad de registros por cada mes, tal como se muestra a continuación.

    Rta/
    [('01', 3),
     ('02', 4),
     ('03', 2),
     ('04', 4),
     ('05', 3),
     ('06', 3),
     ('07', 5),
     ('08', 6),
     ('09', 3),
     ('10', 2),
     ('11', 2),
     ('12', 3)]

    """
    # Ruta del archivo de datos
    ruta = "files/input/data.csv"
    
    # Diccionario para contar registros por mes
    contador_meses = {}
    
    # Leer el archivo línea por línea
    with open(ruta, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            # Separar las columnas por tabulador
            columnas = linea.strip().split("\t")
            
            # Verificar que la línea tenga al menos 3 columnas
            if len(columnas) >= 3:
                # Extraer la fecha (columna 2, índice 2)
                fecha = columnas[2]
                
                # Extraer el mes de la fecha (formato YYYY-MM-DD)
                # Dividir por '-' y tomar el segundo elemento (mes)
                partes_fecha = fecha.split("-")
                if len(partes_fecha) >= 2:
                    mes = partes_fecha[1]  # Obtener el mes en formato MM
                    
                    # Contar las ocurrencias de cada mes
                    if mes in contador_meses:
                        contador_meses[mes] += 1
                    else:
                        contador_meses[mes] = 1
    
    # Convertir a lista de tuplas y ordenar por mes
    resultado = sorted(contador_meses.items())
    
    return resultado
