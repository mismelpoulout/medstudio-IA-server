class Aprendizaje:
    def __init__(self, gestor_datos):
        self.gestor_datos = gestor_datos

    def registrar_interaccion(self, usuario, jugada, acierto):
        # Guarda la jugada y si fue correcta o no
        self.gestor_datos.guardar_estadistica(usuario, jugada, acierto)

    def analizar_errores_frecuentes(self):
        # Analiza la base de datos para encontrar pistas difíciles
        return self.gestor_datos.obtener_pistas_mas_falladas()
