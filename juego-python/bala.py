import pygame 
from pygame.sprite import  Sprite

class Bala(Sprite):
    """Esta clase sirve para manejar las balas disparadas desde la nave.
    """
    def __init__(self, ai_configuraciones,pantalla,nave):
        super(Bala,self).__init__ ()
        self.pantalla = pantalla
        #crea una bala
        self.rect = pygame.Rect(0,0,ai_configuraciones.bala_width,ai_configuraciones.bala_height)
        self.rect.centerx = nave.rect.centerx
        self.rect.top = nave.rect.top
        
        #alamace la pocicion de la bala como un atributop decimal
        self.y = float(self.rect.y)
        self.color=ai_configuraciones.bala_color
        
        self.factor_velocidad = ai_configuraciones.bala_factor_velocidad
        
    def update(self):
        """Mueve la bala hacia arriba en la pantalla"""
        #Actualiza la posicion decimal de la bala
        self.y = self.factor_velocidad
        #actualiza la posicon del rect
        self.rect.y=self.y
    def draw_bala(self):
        """Dibuja la bala en la pantalla"""
        pygame.draw.rect(self.pantalla,self.color,self.rect)