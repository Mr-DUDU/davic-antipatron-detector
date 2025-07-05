from data.antipattern_rules import ANTIPATTERN_RULES
import xml.etree.ElementTree as ET

def generar_reporte(resultado, trazabilidad, ruta_salida, component_key):
    # Generación del XML (igual que antes)
    root = ET.Element("reporte")
    lenguaje = resultado["lenguaje"]

    introduccion = ET.SubElement(root, "introduccion")
    ET.SubElement(introduccion, "lenguaje").text = lenguaje
    ET.SubElement(introduccion, "proyecto").text = component_key

    # ⬇ Sección I: Antipatrones
    seccion1 = ET.SubElement(root, "seccion_antipatrones")
    antipatrones_estructura = []

    if resultado["detectados"]:
        for nombre in resultado["detectados"]:
            atp = ET.SubElement(seccion1, "antipatron", nombre=nombre, estado="detectado")
            reglas_xml = ET.SubElement(atp, "reglas_detectadas")

            versiones = ANTIPATTERN_RULES[nombre]["versiones"]
            for v in versiones:
                if lenguaje in v["lenguajes"]:
                    core = v["reglas"]["core"]
                    refuerzo = v["reglas"].get("reforzador", [])
                    moha_relevantes = set(core + refuerzo)
                    break
            else:
                moha_relevantes = set()

            presentes = {item["moha_equivalent"] for item in trazabilidad}
            usados = moha_relevantes.intersection(presentes)

            reglas_detectadas = []
            for regla in sorted(usados):
                ET.SubElement(reglas_xml, "regla").text = regla
                reglas_detectadas.append(regla)

            antipatrones_estructura.append({
                "nombre": nombre,
                "estado": "detectado",
                "reglas_detectadas": reglas_detectadas
            })

    if resultado["posibles"]:
        for nombre in resultado["posibles"]:
            ET.SubElement(seccion1, "antipatron", nombre=nombre, estado="posible")
            antipatrones_estructura.append({
                "nombre": nombre,
                "estado": "posible",
                "reglas_detectadas": []
            })

    if not resultado["detectados"] and not resultado["posibles"]:
        ET.SubElement(seccion1, "antipatron", estado="limpio")

    # ⬇ Sección II: Code Smells detectados (detallados)
    seccion2 = ET.SubElement(root, "seccion_code_smells")
    for item in trazabilidad:
        ET.SubElement(
            seccion2,
            "code_smell",
            rule=item["rule"],
            archivo=item["archivo"],
            linea=str(item["linea"]),
            severity=item["severity"],
            moha=item["moha_equivalent"],
            url=item["url"]
        )

    # ⬇ Guardar archivo XML
    tree = ET.ElementTree(root)
    tree.write(ruta_salida, encoding="utf-8", xml_declaration=True)

    # Retorna la estructura para el template HTML
    return antipatrones_estructura
