import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Sirve para representar a un solo alienigena en la pantalla"""
    def __init__(self,ai_configuraciones,pantalla):
        """Inicializa el alieny establece su pocion"""
        super(Alien,self).__init__()
        self.pantalla = pantalla
        
        self.ai_configuraciones = ai_configuraciones
        #carga la imagen del alien y establec su punto rect
         #carga la imagen y obtiene su red
        self.image=pygame.image.load("image/alien.bmp")
        self.rect = self.image.get_rect()
        #self.pantalla_rect = pantalla.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        #almacena la pocion exacta del alien
        self.x = float(self.rect.x)
    def blitme(self):
        """Dibuja el alien en su ubicacion actual"""
        self.pantalla.blit(self.image,self.rect)

    def check_edges(self):
        """Devuelve true si el alien esta en el borde de la pantalla"""
        screen_rect=self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <=0:
            return True
    
    def update(self):
        """Mueve el alien  a la derecha"""
        self.x += (self.ai_configuraciones.alien_speed_factor *self.ai_configuraciones.fleet_direction)
        self.rect.x = self.x