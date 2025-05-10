import json
import sqlite3

class GestorDatos:
    def __init__(self, db_path="crucigrama.db"):
        self.db_path = db_path

    def importar_pistas_desde_json(self, archivo_json):
        with open(archivo_json, "r", encoding="utf-8") as f:
            pistas = json.load(f)
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        for p in pistas:
            cursor.execute(
                'INSERT INTO pistas (pista, respuesta, fila, columna, horizontal, dificultad) VALUES (?, ?, ?, ?, ?, ?)',
                (p["pista"], p["respuesta"], p["fila"], p["columna"], p["horizontal"], p.get("dificultad", 1))
            )
        conn.commit()
        conn.close()

    def exportar_pistas_a_json(self, archivo_json):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('SELECT pista, respuesta, fila, columna, horizontal, dificultad FROM pistas')
        pistas = cursor.fetchall()
        lista = [
            {"pista": p[0], "respuesta": p[1], "fila": p[2], "columna": p[3], "horizontal": bool(p[4]), "dificultad": p[5]}
            for p in pistas
        ]
        with open(archivo_json, "w", encoding="utf-8") as f:
            json.dump(lista, f, ensure_ascii=False, indent=2)
        conn.close()
