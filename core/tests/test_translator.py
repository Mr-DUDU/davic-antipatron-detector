import pytest

from core import translator

def test_cargar_diccionario_equivalencias():
    path = "./davic/data/code_smells_translation.csv"
    equivalencias = translator.cargar_diccionario_equivalencias(path)
    assert isinstance(equivalencias, dict)
    assert "python:S5918" in equivalencias
    assert equivalencias["python:S5918"] == "test smells"