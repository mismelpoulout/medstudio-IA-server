from flask import Flask, request, jsonify
from ia_crucigrama import CrucigramaIA

app = Flask(__name__)
ia = CrucigramaIA()

@app.route("/", methods=["GET"])
def home():
    return "Servidor de IA de Crucigrama funcionando"

@app.route("/sugerir_jugada", methods=["POST"])
def sugerir_jugada():
    data = request.json
    tablero = data["tablero"]           # Matriz 10x10 (None o "" para celdas vacías)
    pistas = data["pistas"]             # Lista de pistas: clue, answer, row, col, isAcross
    letras = data["letras"]             # Letras disponibles para la IA, ej: ["B", "P", "C"]
    jugada = ia.sugerir_jugada(tablero, pistas, letras)
    return jsonify({"jugada": jugada})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
