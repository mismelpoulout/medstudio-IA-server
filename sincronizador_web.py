import requests
import time

class SincronizadorWeb:
    def __init__(self, gestor_datos):
        self.gestor_datos = gestor_datos
        self.en_reposo = False

    def activar_reposo(self):
        self.en_reposo = True
        self.comparar_y_corregir()

    def desactivar_reposo(self):
        self.en_reposo = False

    def comparar_y_corregir(self):
        if not self.en_reposo:
            return
        # Ejemplo: comparar definiciones en Wikipedia solo en reposo
        pistas = self.gestor_datos.obtener_pistas()
        for pista in pistas:
            palabra = pista["respuesta"]
            url = f"https://es.wikipedia.org/api/rest_v1/page/summary/{palabra}"
            resp = requests.get(url)
            if resp.ok:
                data = resp.json()
                definicion = data.get("extract", "")
                # Aquí puedes comparar y corregir si hay errores
            time.sleep(1)  # Para no saturar la API
