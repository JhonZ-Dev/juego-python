class Configuraciones(object):
    """Esta clase sirve para almacenar todas las configuraciones de invacion alienigena"""
    def __init__(self):
        self.screen_width=990
        self.screen_height=690
        self.bg_color=(243, 156, 18)
        
    #Configuracion de lña nava}
        self.cantidad_naves=3 #cantidad de naves
        
        #configuracion de balas
        
        self.bala_width = 3
        self.bala_height = 15
        self.bala_color=(60, 60, 60)
        self.balas_allowed = 3
        
        #configuracion de los aliens
        
        self.fleet_drop_speed=10
        #que tan rapido se acelera el juego
        self.escala_aceleracion=1.1
        self.inicializa_configuraciones_dinamicas()
        self.fleet_direction = 1
    def inicializa_configuraciones_dinamicas(self):
        """Inicializa la configuracion que cambia a lo largo del juego"""
        self.factor_velocidad_nave=1.5 #tiempo pixel del juego
        self.bala_factor_velocidad = 3
        self.alien_speed_factor=1
               
        
        