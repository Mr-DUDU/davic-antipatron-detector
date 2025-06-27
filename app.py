from flask import Flask, render_template, request
from core.api_importer import obtener_code_smells
from core.reporter import generar_reporte_xml
from core.translator import cargar_diccionario_equivalencias, traducir_code_smells
from core.analyzer import analizar_antipatrones
import os

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

from flask import Flask, render_template, request
from core.api_importer import obtener_code_smells
from core.translator import cargar_diccionario_equivalencias, traducir_code_smells

@app.route("/analizar", methods=["POST"])
def analizar():
    try:
        component_key = request.form["component_key"]
        token = request.form["token"]
        language = request.form["language"]

        # Volvemos a obtener los code smells (deberían venir cacheados en produccion)
        sqc_data = obtener_code_smells(component_key, token)

        # Cargar equivalencias Moha
        equivalencias = cargar_diccionario_equivalencias(RUTA_CSV_EQUIVALENCIAS)

        # Feature 2: Traduccion
        moha_set, trazabilidad = traducir_code_smells(sqc_data, equivalencias)

        # Paso 3: Análisis de antipatrones (Feature 3)
        resultado = analizar_antipatrones(moha_set)

        # Generar el XML en una ruta dentro de /static/reports
        nombre_archivo = "reporte_demo.xml"
        ruta_xml = os.path.join("static", "reports", nombre_archivo)
        generar_reporte_xml(resultado, trazabilidad, ruta_xml)

        return render_template(
            "reporte_generado.html",
            lenguaje=language,
            moha_set=moha_set,
            trazabilidad=trazabilidad,
            resultado=resultado,
            ruta_xml=ruta_xml
        )

    except Exception as e:
        return render_template("index.html", mensaje=f"Error en análisis: {str(e)}")


if __name__ == "__main__":
    app.run(debug=True)