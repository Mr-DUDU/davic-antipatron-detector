import pytest
from core.translator import cargar_diccionario_equivalencias, traducir_code_smells
from core.analyzer import analizar_antipatrones
from core.reporter import generar_reporte_xml
from core.tests.data.samples_moha_sets import sqc_codes_SC_COMPLETE
import xml.etree.ElementTree as ET


def test_generar_xml_con_lenguaje(tmp_path):
    # Arrange
    ruta_csv = "davic/data/code_smells_translation.csv"
    equivalencias = cargar_diccionario_equivalencias(ruta_csv)
    traducciones, trazabilidad = traducir_code_smells(sqc_codes_SC_COMPLETE, equivalencias)
    resultado = analizar_antipatrones(traducciones)

    ruta_salida = tmp_path / "reporte.xml"

    # Act
    generar_reporte_xml(resultado, trazabilidad, ruta_salida)

    # Assert
    tree = ET.parse(ruta_salida)
    root = tree.getroot()

    lenguaje = root.find("introduccion/lenguaje")
    assert lenguaje is not None
    assert lenguaje.text == resultado["lenguaje"]
