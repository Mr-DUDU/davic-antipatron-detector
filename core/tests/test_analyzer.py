import pytest
from core.translator import cargar_diccionario_equivalencias, traducir_code_smells
from core.analyzer import analizar_antipatrones
from core.tests.data.samples_moha_sets import *

def test_detecta_SAK_completo():
    # Arrange
    path = "davic/data/code_smells_translation.csv"
    equivalencias = cargar_diccionario_equivalencias(path)
    traducciones, trazabilidad = traducir_code_smells(sqc_codes_SAK_COMPLETE, equivalencias)

    # Act
    resultado = analizar_antipatrones(traducciones)

    # Assert
    assert "Swiss Army Knife" in resultado["detectados"]

def test_no_detecta_SAK_solo_reforzador():
    path = "davic/data/code_smells_translation.csv"
    equivalencias = cargar_diccionario_equivalencias(path)
    traducciones, trazabilidad = traducir_code_smells(sqc_codes_SAK_ONLY_REINFORCER, equivalencias)

    resultado = analizar_antipatrones(traducciones)

    assert "Swiss Army Knife" not in resultado["detectados"]
    assert "Swiss Army Knife" in resultado["posibles"]

def test_no_detecta_SAK_nada():
    path = "davic/data/code_smells_translation.csv"
    equivalencias = cargar_diccionario_equivalencias(path)
    traducciones, trazabilidad = traducir_code_smells(sqc_codes_EMPTY, equivalencias)

    resultado = analizar_antipatrones(traducciones)

    assert "Swiss Army Knife" not in resultado["detectados"]
    assert "Swiss Army Knife" not in resultado["posibles"]
