import pygame
from pygame.sprite import _Group, Sprite

class Alien(Sprite):
    """Sirve para representar a un solo alienigena en la pantalla"""
    def __init__(self,ai_configuraciones,pantalla):
        """Inicializa el alieny establece su pocion"""
        super(Alien,self).__init__()
        self.pantalla = pantalla
        
        self.ai_configuraciones = ai_configuraciones
        #carga la imagen del alien y establec su punto rect
         #carga la imagen y obtiene su red
        self.imagen=pygame.image.load("image/alien.bmp")
        self.rect = self.imagen.get_rect()
        #self.pantalla_rect = pantalla.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        #almacena la pocion exacta del alien
        self.x = float(self.rect.x)
        