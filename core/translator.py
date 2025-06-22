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
def traducir_code_smells(sqc_code, moha_compatible):
    traducciones = set()
    trazabilidad = []

    # aqui es donde se itera sobre los codigos de SQC_Code
    for code in sqc_code:
        # aqui se comprueba si el codigo existe en el diccionario de equivalencias de moha_compatible
        if code in moha_compatible:
            # Obtiene el valor traducido (la categoría Moha compatible).
            moha_encontrado = moha_compatible[code]
            # se agrega el codigo y su traduccion al set
            traducciones.add(moha_encontrado)
            trazabilidad.append((code, moha_encontrado))

    return traducciones, trazabilidad
