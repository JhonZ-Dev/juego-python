class Estadistica():
    """Seguimiento de las estadísticas del juego"""
    def __init__(self,ai_configuraciones):
        """Inicializa las estadísticas"""
        self.ai_configuraciones = ai_configuraciones
        self.reset_stats()
        #Puntuación máxima
        self.puntuacion_maxima = 0
        #Nivel
        self.nivel = 1