import requests

def obtener_code_smells(component_key, token):
    url = "https://sonarcloud.io/api/issues/search"
    params= {
        "componentKeys": component_key,
        "types": "CODE_SMELL",
        "ps": 500
    }
    headers = {
        "Authorization": token
    }
    response = requests.get(url, params=params, headers=headers)
    if response.status_code != 200:
        raise Exception("No se pudo conectar a SonarCloud.")

    data = response.json()
    # Validación REAL: ¿hay issues?
    if not data.get("issues"):
        raise Exception("Conexión exitosa, pero no se encontraron code smells. Verifica el componente o el token.")


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
