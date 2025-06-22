import csv

def cargar_diccionario_equivalencias(ruta_csv):
    equivalencias = {}

    with open(ruta_csv, mode='r', encoding='utf-8-sig') as archivo:
        lector = csv.DictReader(archivo, delimiter=';')
        for fila in lector:
            codigo_sonar = fila['SQC_Code'].strip()
            moha_equivalente = fila['Moha_Compatible'].strip()
            equivalencias[codigo_sonar] = moha_equivalente
    return equivalencias

