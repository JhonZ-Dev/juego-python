class Estadistica():
    """Seguimiento de las estadísticas del juego"""
    def __init__(self,ai_configuraciones):
        """Inicializa las estadísticas"""
        self.ai_configuraciones = ai_configuraciones
        self.reset_stats()
        #inicia el juego en un estado activo
        self.game_active = False
        
        #La puntacion alta nunca debe reiniciarse
        self.alto_puntaje = 0
        
        
        
        
        
        
    def reset_stats(self):
        """Inicializa las estaditicas  que pueden cambiar durante el juego """
        #Puntuación máxima
        self.naves_restantes = self.ai_configuraciones.cantidad_naves
        self.puntaje = 0
    
    