import pygame
class Nave():
    """Sirve para gestionar el comportamiento de la nave"""
    def __init__(self,ai_configuraciones,pantalla):
        """Inicializa la nacve y establece la posicion de partida"""
        self.pantalla=pantalla
        self.ai_configuraciones = ai_configuraciones
        
        #carga la imagen y obtiene su red
        self.imagen=pygame.image.load("image/nave.bmp")
        self.rect = self.imagen.get_rect()
        self.pantalla_rect = pantalla.get_rect()
        
        #empieza la nave en la parte inferior de la pantalla
        self.rect.centerx = self.pantalla_rect.centerx
        self.rect.bottom = self.pantalla_rect.bottom
        
        #almacena un valor decimal para el centro de la nave
        self.center = float(self.rect.centerx)
        
        #bandera de movimiento
        self.moving_rigth = False
        self.moving_left = False
        
    def update(self):
        """Actualiza la posicion de la nave segun el valor que tenga la bandera de movimiento"""
        if self.moving_rigth:
            self.center += self.ai_configuraciones.factor_velocidad_nave
            
            
        if self.moving_left:
            self.center -=self.ai_configuraciones.factor_velocidad_nave
            
        self.rect.centerx = self.center


    def blitme(self):
        """Dibuja la nave en su ubicacion actua"""
        self.pantalla.blit(self.imagen, self.rect)