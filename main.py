from core.api_importer import obtener_code_smells
from core.translator import cargar_diccionario_equivalencias, traducir_code_smells
from core.analyzer import analizar_antipatrones
from core.tests.data.samples_moha_sets import *

if __name__ == "__main__":
    # Ruta al CSV de equivalencias
    ruta_csv = "davic/data/code_smells_translation.csv"

    # 1. Cargar el diccionario de equivalencias
    equivalencias = cargar_diccionario_equivalencias(ruta_csv)

    # PRUEBA: Feature 2 con datos quemados (Swiss Army Knife - Complete)
    # 3. Ejecutar traducción
    moha_set, trazabilidad = traducir_code_smells(sqc_codes_SC_EMPTY, equivalencias)

    # Mostrar resultados
    print("✅ Set de categorías Moha detectadas:")
    print(moha_set)

    print("\n📌 Trazabilidad:")
    for code, moha in trazabilidad:
        print(f"- {code} → {moha}")

    # 4. Analizar antipatrón
    resultado = analizar_antipatrones(moha_set)
    print(type(resultado))


    '''
    print("Obteniendo Code Smells desde SonarQube Cloud...\n")
    # Paso 1: Obtener lista de códigos SQC desde SonarCloud
    sqc_codes = obtener_code_smells()
    if not sqc_codes:
        print("⚠️ No se encontraron code smells o hubo un problema en la extracción.")
    else:

        print(f"✅ Se encontraron {len(sqc_codes)} code smells únicos:")
        for i, code in enumerate(sqc_codes, 1):
            print(f"{i:02d}: {code}")

        print("\nCargando diccionario de equivalencias...\n")

        # Paso 2: Cargar el diccionario de equivalencias Moha desde CSV
        ruta_csv = "davic/data/code_smells_translation.csv"
        moha_compatible = cargar_diccionario_equivalencias(ruta_csv)

        # Paso 3: Traducir los SQC_Code usando el diccionario cargado
        traducciones, trazabilidad = traducir_code_smells(sqc_codes, moha_compatible)

        # Paso 4: Mostrar resultados
        print("\n✅ Traducciones Moha encontradas:")
        print(traducciones)
        print(trazabilidad)

    '''