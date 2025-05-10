# archivo: server.py
from flask import Flask, request, jsonify
from ia_crucigrama import CrucigramaIA

app = Flask(__name__)
ia = CrucigramaIA()

@app.route('/jugada', methods=['POST'])
def jugada():
    data = request.json
    letras = data.get('letras', [])
    jugada = ia.calcular_jugada(letras)
    return jsonify({'jugada': jugada})

@app.route('/pistas', methods=['GET'])
def pistas():
    return jsonify({'pistas': ia.obtener_pistas()})

@app.route('/estadistica', methods=['POST'])
def estadistica():
    data = request.json
    jugador = data['jugador']
    puntuacion = data['puntuacion']
    ia.registrar_estadistica(jugador, puntuacion)
    return jsonify({'ok': True})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
