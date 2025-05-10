from gestor_datos import GestorDatos
from generador_juegos import GeneradorJuegos
from aprendizaje import Aprendizaje
from sincronizador_web import SincronizadorWeb

class CrucigramaIA:
    def __init__(self):
        self.gestor_datos = GestorDatos()
        self.generador_juegos = GeneradorJuegos(self.gestor_datos)
        self.aprendizaje = Aprendizaje(self.gestor_datos)
        self.sincronizador_web = SincronizadorWeb(self.gestor_datos)

    def nuevo_juego(self, dificultad=1):
        # Genera un nuevo crucigrama según la dificultad
        return self.generador_juegos.crear_nuevo_juego(dificultad)

    def sugerir_jugada(self, tablero, pistas, letras_disponibles):
        # Aquí va la lógica para sugerir la mejor jugada posible
        # Puedes delegar a un método de aprendizaje o lógica interna
        return self.aprendizaje.sugerir_jugada(tablero, pistas, letras_disponibles)

    def registrar_jugada(self, usuario, jugada, acierto):
        # Guarda la jugada y si fue correcta o no
        self.aprendizaje.registrar_interaccion(usuario, jugada, acierto)

    def importar_pistas(self, archivo_json):
        self.gestor_datos.importar_pistas_desde_json(archivo_json)

    def exportar_pistas(self, archivo_json):
        self.gestor_datos.exportar_pistas_a_json(archivo_json)

    def activar_reposo(self):
        self.sincronizador_web.activar_reposo()

    def desactivar_reposo(self):
        self.sincronizador_web.desactivar_reposo()
