from core.reporter import generar_reporte
from flask import Flask, render_template, request
from core.api_importer import obtener_code_smells
from core.translator import cargar_diccionario_equivalencias, traducir_code_smells

from core.analyzer import analizar_antipatrones
import os, re

# app.py
RUTA_CSV_EQUIVALENCIAS = "data/code_smells_translation.csv"

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api_importer", methods=["POST"])
def api_importer():
    try:
        component_key = request.form["component_key"]
        token = request.form["token"]
        language = request.form["language"]
        sqc_data = obtener_code_smells(component_key, token)

        if not sqc_data:
            raise Exception("Conexión exitosa, pero no se encontraron code smells. Verifica el componente o el token.")
        return render_template("detectando.html",component_key= component_key, token= token,
                               language=language, data=sqc_data)
    except Exception as e:
        return render_template("index.html", mensaje=str(e))

@app.route("/analizar", methods=["POST"])
def analizar():
    try:
        component_key = request.form["component_key"]
        token = request.form["token"]
        language = request.form["language"]

        sqc_data = obtener_code_smells(component_key, token)
        equivalencias = cargar_diccionario_equivalencias(RUTA_CSV_EQUIVALENCIAS)
        moha_set, trazabilidad = traducir_code_smells(sqc_data, equivalencias)
        resultado = analizar_antipatrones(moha_set)

        # Generar XML y la estructura de datos
        nombre_sanitizado = re.sub(r'[^\w\-_.]', '_', component_key)
        nombre_archivo = f"{nombre_sanitizado}_detectado_antipatrones.xml"
        ruta_xml = os.path.join("static", "reports", nombre_archivo)

        # Genera XML y datos
        antipatrones_estructura = generar_reporte(resultado, trazabilidad, ruta_xml, component_key)

        return render_template(
            "reporte_generado.html",
            lenguaje=language,
            component_key=component_key,
            moha_set=moha_set,
            trazabilidad=trazabilidad,
            resultado=resultado,
            ruta_xml=ruta_xml,
            antipatrones_estructura=antipatrones_estructura  # Pasa la estructura para el reporte HTML
        )

    except Exception as e:
        return render_template("index.html", mensaje=f"Error en análisis: {str(e)}")


if __name__ == "__main__":
    app.run(debug=True)