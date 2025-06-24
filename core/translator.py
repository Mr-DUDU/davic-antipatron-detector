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
'''
Nombre de la funcion traducir_code_smells porque es la que se usa en el core, ademas para manterner la consistencia
con el nombre de la funcion en el csv
'''
def traducir_code_smells(sqc_data, moha_compatible):
    traducciones = set()
    trazabilidad = []

    # aqui es donde se itera sobre los rules que son los códigos de los code smells de SQC_Code
    for item in sqc_data:
        rule = item.get("rule")
        if rule in moha_compatible:
            moha_equivalente = moha_compatible[rule]
            traducciones.add(moha_equivalente)
            item["moha_equivalent"] = moha_equivalente
            trazabilidad.append(item)
    return traducciones, trazabilidad
