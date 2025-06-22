import pytest
from core.api_importer import obtener_code_smells


def test_obtener_code_smells_responde():
    # Act
    resultado = obtener_code_smells()

    # Assert
    assert isinstance(resultado, dict)
    assert "total" in resultado  # esperamos al menos esta clave que siempre viene
