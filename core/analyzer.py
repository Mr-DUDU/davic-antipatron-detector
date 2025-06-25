from davic.data.antipattern_rules import ANTIPATTERN_RULES

def analizar_antipatrones(traducciones):
    lenguaje = "python"  # ← Esto luego puede venir desde la UI

    detectados = []
    posibles = []

    conocidos = set()  # Acumulará todas las reglas evaluadas (para hallar aislados)

    for nombre, definicion in ANTIPATTERN_RULES.items():
        versiones = definicion.get("versiones", [])

        for version in versiones:
            # Comprobar si la versión aplica al lenguaje actual
            if lenguaje not in version.get("lenguajes", []):
                continue

            reglas = version["reglas"]
            core = set(reglas["core"])
            refuerzo = set(reglas.get("reforzador", []))
            umbral = version.get("umbral", len(core))

            conocidos.update(core | refuerzo)

            interseccion_core = traducciones & core
            interseccion_refuerzo = traducciones & refuerzo

            if len(interseccion_core) >= umbral:
                detectados.append(nombre)
                break  # Ya se detectó, no analizar más versiones
            elif interseccion_refuerzo:
                posibles.append(nombre)
                break

    return {
        "lenguaje": lenguaje,
        "detectados": sorted(set(detectados)),
        "posibles": sorted(set(posibles)),
    }
