import pytest

from core import translator
from core.translator import traducir_code_smells

def test_cargar_diccionario_equivalencias():
    path = "davic/data/code_smells_translation.csv"
    equivalencias = translator.cargar_diccionario_equivalencias(path)
    assert isinstance(equivalencias, dict)
    assert "python:S5918" in equivalencias
    assert equivalencias["python:S5918"] == "test smells"

def test_traducir_code_smells():
    sqc_code = ["python:S7507", "python:S2737", "python:S9999"]
    moha_compatible = {
        "python:S7507": "Method No Parameter",
        "python:S2737": "Method No Parameter"
    }

    traducciones, trazabilidad = traducir_code_smells(sqc_code, moha_compatible)

    assert isinstance(traducciones, set)
    assert isinstance(trazabilidad, list)

    # Debe haber una sola traducción de tipo Moha (aunque dos SQC apunten a ella)
    assert traducciones == {"Method No Parameter"}

    # Trazabilidad debe incluir solo los dos códigos válidos
    assert ("python:S7507", "Method No Parameter") in trazabilidad
    assert ("python:S2737", "Method No Parameter") in trazabilidad
    assert not any("python:S9999" in t for t in trazabilidad)