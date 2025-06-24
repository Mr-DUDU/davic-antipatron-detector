# Caso completo: contiene el code smell núcleo y un reforzador
sqc_codes_SAK_COMPLETE = [
    {
        "rule": "python:S6918",
        "severity": "MAJOR",
        "archivo": "modulo/dummy_file_0.py",
        "linea": 10,
        "url": "https://sonarcloud.io/project/issues?id=DummyProject&open=issue_key_0"
    },
    {
        "rule": "python:S104",
        "severity": "MINOR",
        "archivo": "modulo/dummy_file_1.py",
        "linea": 11,
        "url": "https://sonarcloud.io/project/issues?id=DummyProject&open=issue_key_1"
    },
    {
        "rule": "python:S5603",
        "severity": "MAJOR",
        "archivo": "modulo/dummy_file_2.py",
        "linea": 12,
        "url": "https://sonarcloud.io/project/issues?id=DummyProject&open=issue_key_2"
    },
    {
        "rule": "python:S2208",
        "severity": "MINOR",
        "archivo": "modulo/dummy_file_3.py",
        "linea": 13,
        "url": "https://sonarcloud.io/project/issues?id=DummyProject&open=issue_key_3"
    },
    {
        "rule": "python:S1481",
        "severity": "MAJOR",
        "archivo": "modulo/dummy_file_4.py",
        "linea": 14,
        "url": "https://sonarcloud.io/project/issues?id=DummyProject&open=issue_key_4"
    }
]

# Caso parcial: solo contiene el reforzador, no se detecta antipatrón
sqc_codes_SAK_ONLY_REINFORCER = [
    {
        "rule": "python:S1481",
        "severity": "MAJOR",
        "archivo": "modulo/dummy_file_0.py",
        "linea": 10,
        "url": "https://sonarcloud.io/project/issues?id=DummyProject&open=issue_key_0"
    }
]


# Caso completo: contiene el code smell núcleo y un reforzador
sqc_codes_FC_COMPLETE = [
    {
        "rule": "python:S4487",
        "severity": "MAJOR",
        "archivo": "modulo/dummy_file_0.py",
        "linea": 10,
        "url": "https://sonarcloud.io/project/issues?id=DummyProject&open=issue_key_0"
    },
    {
        "rule": "python:S1144",
        "severity": "MINOR",
        "archivo": "modulo/dummy_file_1.py",
        "linea": 11,
        "url": "https://sonarcloud.io/project/issues?id=DummyProject&open=issue_key_1"
    },
    {
        "rule": "python:S5603",
        "severity": "MAJOR",
        "archivo": "modulo/dummy_file_2.py",
        "linea": 12,
        "url": "https://sonarcloud.io/project/issues?id=DummyProject&open=issue_key_2"
    },
    {
        "rule": "python:S6397",
        "severity": "MINOR",
        "archivo": "modulo/dummy_file_3.py",
        "linea": 13,
        "url": "https://sonarcloud.io/project/issues?id=DummyProject&open=issue_key_3"
    },
    {
        "rule": "pythonenterprise:S7469",
        "severity": "MAJOR",
        "archivo": "modulo/dummy_file_4.py",
        "linea": 14,
        "url": "https://sonarcloud.io/project/issues?id=DummyProject&open=issue_key_4"
    }
]


# Caso completo: contiene el code smell núcleo y un reforzador
sqc_codes_SC_COMPLETE = [
    {
        "rule": "python:S138",
        "severity": "MAJOR",
        "archivo": "modulo/dummy_file_0.py",
        "linea": 10,
        "url": "https://sonarcloud.io/project/issues?id=DummyProject&open=issue_key_0"
    },
    {
        "rule": "python:S6019",
        "severity": "MINOR",
        "archivo": "modulo/dummy_file_1.py",
        "linea": 11,
        "url": "https://sonarcloud.io/project/issues?id=DummyProject&open=issue_key_1"
    },
    {
        "rule": "python:S6911",
        "severity": "MAJOR",
        "archivo": "modulo/dummy_file_2.py",
        "linea": 12,
        "url": "https://sonarcloud.io/project/issues?id=DummyProject&open=issue_key_2"
    },
    {
        "rule": "python:S3516",
        "severity": "MINOR",
        "archivo": "modulo/dummy_file_3.py",
        "linea": 13,
        "url": "https://sonarcloud.io/project/issues?id=DummyProject&open=issue_key_3"
    }
]

# Caso parcial: solo contiene el reforzador, no se detecta antipatrón
sqc_codes_SC_ONLY_REINFORCER = [
    {
        "rule": "python:S4144",
        "severity": "MAJOR",
        "archivo": "modulo/dummy_file_0.py",
        "linea": 10,
        "url": "https://sonarcloud.io/project/issues?id=DummyProject&open=issue_key_0"
    }
]

# Caso vacío: ningún code smell relevante
sqc_codes_EMPTY = [
    {
        "rule": "python:S9999",
        "severity": "MAJOR",
        "archivo": "modulo/dummy_file_0.py",
        "linea": 10,
        "url": "https://sonarcloud.io/project/issues?id=DummyProject&open=issue_key_0"
    },
    {
        "rule": "python:S7507",
        "severity": "MINOR",
        "archivo": "modulo/dummy_file_1.py",
        "linea": 11,
        "url": "https://sonarcloud.io/project/issues?id=DummyProject&open=issue_key_1"
    },
    {
        "rule": "python:S5603",
        "severity": "MAJOR",
        "archivo": "modulo/dummy_file_2.py",
        "linea": 12,
        "url": "https://sonarcloud.io/project/issues?id=DummyProject&open=issue_key_2"
    },
    {
        "rule": "python:S6019",
        "severity": "MINOR",
        "archivo": "modulo/dummy_file_3.py",
        "linea": 13,
        "url": "https://sonarcloud.io/project/issues?id=DummyProject&open=issue_key_3"
    }
]