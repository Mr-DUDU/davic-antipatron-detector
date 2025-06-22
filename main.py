from core.api_importer import obtener_code_smells

if __name__ == "__main__":
    print("Obteniendo Code Smells desde SonarQube Cloud...\n")

    sqc_codes = obtener_code_smells()

    if not sqc_codes:
        print("⚠️ No se encontraron code smells o hubo un problema en la extracción.")
    else:
        print(f"✅ Se encontraron {len(sqc_codes)} code smells únicos:")
        for i, code in enumerate(sqc_codes, 1):
            print(f"{i:02d}: {code}")
