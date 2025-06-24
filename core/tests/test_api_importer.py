import pytest
from core.api_importer import obtener_code_smells

def test_obtener_code_smells_formato_enriquecido():
    resultados = obtener_code_smells()

    # Debe devolver una lista
    assert isinstance(resultados, list)
    assert len(resultados) > 0

    # Cada ítem debe ser un dict con las claves necesarias
    for item in resultados:
        assert isinstance(item, dict)
        assert "rule" in item
        assert "severity" in item
        assert "archivo" in item
        assert "linea" in item
        assert "url" in item

        # Validaciones extra de formato
        assert isinstance(item["rule"], str)
        assert ":" in item["rule"]  # formato esperado python:S1234
        assert item["url"].startswith("https://sonarcloud.io/project/issues")
