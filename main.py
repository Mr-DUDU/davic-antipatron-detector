from core.api_importer import obtener_code_smells
import csv

def cargar_diccionario_equivalencias(ruta_csv):
    equivalencias = {}
    with open(ruta_csv, mode='r', encoding='utf-8-sig') as archivo:
        lector = csv.DictReader(archivo, delimiter=';')
        print("Encabezados detectados:", lector.fieldnames)
        for fila in lector:
            print("Fila:", fila)
    return equivalencias

if __name__ == "__main__":
    path = "./davic/data/code_smells_translation.csv"
    cargar_diccionario_equivalencias(path)

