import pytest
from core.api_importer import obtener_code_smells

def test_obtener_code_smells_devuelve_lista_de_sqc():
    sqc_codes = obtener_code_smells()

    assert isinstance(sqc_codes, list)
    assert all(isinstance(code, str) for code in sqc_codes)
    assert any(":" in code for code in sqc_codes)  # ejemplo: "python:S1192"
