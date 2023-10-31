class Configuraciones(object):
    """Esta clase sirve para almacenar todas las configuraciones de invacion alienigena"""
    def __init__(self):
        self.screen_width=800
        self.screen_height=600
        self.bg_color=(243, 156, 18)
        
    #Configuracion de lña nava}
        self.factor_velocidad_nave=1.5 #tiempo pixel del juego
        
        #configuracion de balas
        self.bala_factor_velocidad = 3
        self.bala_width = 3
        self.bala_height = 15
        self.bala_color=(60, 60, 60)
        self.balas_allowed = 3
        
        #configuracion de los aliens
        self.alien_speed_factor=1
        self.fleet_drop_speed=10
        self.fleet_direction = 1
        
        
        