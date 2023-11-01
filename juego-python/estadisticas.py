class Estadistica():
    """Seguimiento de las estadísticas del juego"""
    def __init__(self,ai_configuraciones):
        """Inicializa las estadísticas"""
        self.ai_configuraciones = ai_configuraciones
        self.reset_stats()
    def reset_stats(self):
        """Inicializa las estaditicas  que pueden cambiar durante el juego """
        #Puntuación máxima
        self.puntuacion_maxima = 0
        #Nivel
        self.nivel = 1