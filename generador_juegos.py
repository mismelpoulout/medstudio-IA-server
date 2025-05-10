import random

class GeneradorJuegos:
    def __init__(self, gestor_datos):
        self.gestor_datos = gestor_datos

    def crear_nuevo_juego(self, dificultad=1):
        # Obtén pistas de la base de datos según dificultad
        pistas = self.gestor_datos.obtener_pistas(dificultad)
        # Selecciona aleatoriamente un subconjunto para el nuevo juego
        juego = random.sample(pistas, min(len(pistas), 15))  # Por ejemplo, 15 pistas por juego
        # Aquí puedes crear la estructura del tablero (matriz, posiciones, etc.)
        return juego

    def reiniciar_juego(self, dificultad=1):
        return self.crear_nuevo_juego(dificultad)
