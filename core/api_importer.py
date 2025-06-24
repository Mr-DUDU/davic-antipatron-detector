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
        print("Conexión exitosa a la API de SonarCloud")
        data = response.json()
    else:
        response.raise_for_status()  # Lanza un error si la solicitud falla

    issues = data.get("issues", [])
    sqc_data = []
    for issue in issues:
        try:
            sqc_data.append({
                "rule": issue["rule"],
                "severity": issue["severity"],
                "archivo": issue["component"].split(":", 1)[1],
                "linea": issue.get("line", "N/A"),
                "url": f"https://sonarcloud.io/project/issues?id={issue['project']}&open={issue['key']}"
            })
        except KeyError as e:
            print(f"⚠️ Issue malformado: {e}")
            continue

    return sqc_data
