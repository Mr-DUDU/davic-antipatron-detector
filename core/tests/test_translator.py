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
    sqc_data = [
        {
            "rule": "python:S7507",
            "severity": "MAJOR",
            "archivo": "app/module1.py",
            "linea": 42,
            "url": "https://sonarcloud.io/project/issues?id=Project&open=abc123"
        },
        {
            "rule": "python:S2737",
            "severity": "MINOR",
            "archivo": "app/module2.py",
            "linea": 10,
            "url": "https://sonarcloud.io/project/issues?id=Project&open=def456"
        },
        {
            "rule": "python:S9999",  # ← no está en el diccionario, se ignora
            "severity": "INFO",
            "archivo": "app/module3.py",
            "linea": 88,
            "url": "https://sonarcloud.io/project/issues?id=Project&open=zzz999"
        }
    ]

    moha_compatible = {
        "python:S7507": "Method No Parameter",
        "python:S2737": "Method No Parameter"
    }

    traducciones, trazabilidad = traducir_code_smells(sqc_data, moha_compatible)

    assert isinstance(traducciones, set)
    assert isinstance(trazabilidad, list)

    # Solo se deben registrar las equivalencias válidas
    assert traducciones == {"Method No Parameter"}
    assert len(trazabilidad) == 2

    for item in trazabilidad:
        assert "moha_equivalent" in item
        assert item["moha_equivalent"] == "Method No Parameter"
        assert item["rule"] in moha_compatible
