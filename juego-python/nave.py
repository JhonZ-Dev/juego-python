import pygame
class Nave():
    """Sirve para gestionar el comportamiento de la nave"""
    def __init__(self,pantalla):
        """Inicializa la nacve y establece la posicion de partida"""
        self.pantalla=pantalla
        
        #carga la imagen y obtiene su red
        self.imagen=pygame.image.load("image/nave.bmp")
        self.rect = self.imagen.get_rect()
        self.pantalla_rect = pantalla.get_rect()
        
        #empieza la nave en la parte inferior de la pantalla
        self.rect.centerx = self.pantalla_rect.centerx
        self.rect.bottom = self.pantalla_rect.bottom
        
        #bandera de movimiento
        self.moving_rigth = False
        
    def update(self):
        """Actualiza la posicion de la nave segun el valor que tenga la bandera de movimiento"""
        if self.moving_rigth:
            self.rect.centerx +=1


    def blitme(self):
        """Dibuja la nave en su ubicacion actua"""
        self.pantalla.blit(self.imagen, self.rect)