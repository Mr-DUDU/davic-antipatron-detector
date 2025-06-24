from core.api_importer import obtener_code_smells
from core.translator import cargar_diccionario_equivalencias, traducir_code_smells
from core.analyzer import analizar_antipatrones
from core.tests.data.samples_moha_sets import *

if __name__ == "__main__":
    # Ruta al CSV de equivalencias
    ruta_csv = "davic/data/code_smells_translation.csv"

    # Cargar el diccionario de equivalencias
    equivalencias = cargar_diccionario_equivalencias(ruta_csv)

    # PRUEBA 1: con datos quemados en nuevo formato

    # Feature 2: Traducción
    moha_set, trazabilidad = traducir_code_smells(sqc_codes_SC_COMPLETE, equivalencias)

    # Mostrar resultados
    print("✅ Set de categorías Moha detectadas:")
    print(moha_set)

    print("\n📌 Trazabilidad (completa):")
    for code_smell in trazabilidad:
        print(f"- {code_smell['rule']} → {code_smell['moha_equivalent']} "
              f"(archivo: {code_smell['archivo']}, línea: {code_smell['linea']})")

    # Feature 3: Análisis de antipatrones
    resultado = analizar_antipatrones(moha_set)
    print("\n📊 Resultado del análisis:")
    print(resultado)

    '''
    # PRUEBA 2: con datos de la API
    print("🛰️  Conectando con SonarQube Cloud...\n")
    datos_code_smells = obtener_code_smells()

    if not datos_code_smells:
        print("⚠️  No se encontraron code smells o hubo un error en la conexión.")
    else:
        print(f"✅ Se extrajeron {len(datos_code_smells)} issues desde la API.")

        # Traducir los code smells
        traducciones, trazabilidad = traducir_code_smells(datos_code_smells, equivalencias)

        print("\n🧠 Traducciones a categorías Moha:")
        print(traducciones)

        print("\n📌 Trazabilidad enriquecida:")
        for entrada in trazabilidad:
            print(f"- {entrada['rule']} → {entrada['moha_equivalent']}")
            print(f"  ↳ Archivo: {entrada['archivo']} (Línea {entrada['linea']})")
            print(f"  ↳ Severidad: {entrada['severity']}")
            print(f"  ↳ URL: {entrada['url']}")
            print()

        # 4. Analizar antipatrón
        resultado = analizar_antipatrones(traducciones)
        print(resultado)
    '''