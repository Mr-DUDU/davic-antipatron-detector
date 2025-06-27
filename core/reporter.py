from data.antipattern_rules import ANTIPATTERN_RULES
import xml.etree.ElementTree as ET

def generar_reporte_xml(resultado, trazabilidad, ruta_salida):
    root = ET.Element("reporte")

    lenguaje = resultado["lenguaje"]

    # ⬇ Introducción
    introduccion = ET.SubElement(root, "introduccion")
    ET.SubElement(introduccion, "lenguaje").text = lenguaje

    # ⬇ Sección I: Antipatrones
    seccion1 = ET.SubElement(root, "seccion_antipatrones")

    if resultado["detectados"]:
        for nombre in resultado["detectados"]:
            atp = ET.SubElement(seccion1, "antipatron", nombre=nombre, estado="detectado")
            reglas_xml = ET.SubElement(atp, "reglas_detectadas")

            # Buscar la versión de reglas compatible con el lenguaje
            versiones = ANTIPATTERN_RULES[nombre]["versiones"]
            for v in versiones:
                if lenguaje in v["lenguajes"]:
                    core = v["reglas"]["core"]
                    refuerzo = v["reglas"].get("reforzador", [])
                    moha_relevantes = set(core + refuerzo)
                    break
            else:
                moha_relevantes = set()

            # Comparar con los moha_equivalents detectados
            presentes = {item["moha_equivalent"] for item in trazabilidad}
            usados = moha_relevantes.intersection(presentes)

            for regla in sorted(usados):
                ET.SubElement(reglas_xml, "regla").text = regla

    if resultado["posibles"]:
        for nombre in resultado["posibles"]:
            ET.SubElement(seccion1, "antipatron", nombre=nombre, estado="posible")

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

    # ⬇ Guardar archivo
    tree = ET.ElementTree(root)
    tree.write(ruta_salida, encoding="utf-8", xml_declaration=True)
