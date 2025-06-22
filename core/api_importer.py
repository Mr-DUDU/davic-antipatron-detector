import requests

def obtener_code_smells():
    url = "https://sonarcloud.io/api/issues/search"
    params= {
        "componentKeys": "Mr-DUDU_PoliPerritos2",
        "types": "CODE_SMELL",
        "ps": 500
    }
    headers = {
        "Authorization": "dcd1ed5e56c26f39ca2c660060d331558899c8c8"
    }
    response = requests.get(url, params=params, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()  # Lanza un error si la solicitud falla
    data = response.json()
    return data
