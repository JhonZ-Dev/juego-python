import pygame.font

class Marcador():
    """Clase destinada para reportar informacion sobre la punacino"""
    def __init__(self,ai_configuraciones,pantalla,estadisticas):
        """Registro de puntake"""
        self.pantalla = pantalla
        self.pantalla_rect = pantalla.get_rect()
        
        self.ai_configuraciones = ai_configuraciones
        self.estadisticas = estadisticas
        
        #ajustes de fuentes para informacion de puntacion
        self.text_color = (30,30,30)
        self.font=pygame.font.SysFont(None,48)
        
        #prepara la imagen del puntake inicial
        self.prep_puntaje()
        self.prep_puntaje_alto()
        
    def prep_puntaje(self):
        """Convierte el mercador en unaimagen rendereizada"""
        puntaje_redeondeado = int(round(self.estadisticas.puntaje,-1))
        puntaje_str="{:,}".format(puntaje_redeondeado)
        self.puntaje_imagen = self.font.render(puntaje_str,True,self.text_color,self.ai_configuraciones.bg_color)
        
        #Muestra el puntaje en la esquina superior derecha de la pantalla
        self.puntaje_rect = self.puntaje_imagen.get_rect()
        self.puntaje_rect.right = self.pantalla_rect.right-20
        self.pantalla_rect.top=20
    
    
        
    def prep_puntaje_alto(self):
        """Convierte el puntaje alto en una imagen renderizada"""
        puntaje_alto = int(round(self.estadisticas.alto_puntaje,-1))
        puntaje_alto_str = "{:,}".format(puntaje_alto)
        self.alto_puntaje_imagen = self.font.render(puntaje_alto_str,True,self.text_color,self.ai_configuraciones.bg_color)
        
        #centra el puntaje alto en la parte superior de la pantalla
        self.alto_puntaje_rect = self.alto_puntaje_imagen.get_rect()
        self.alto_puntaje_rect.centerx = self.pantalla_rect.centerx
        self.alto_puntaje_rect.top = self.pantalla_rect.top 
    
    def muestra_puntaje(self):
        """Dibuj la puntacion en la pantalla"""
        self.pantalla.blit(self.puntaje_imagen,self.puntaje_rect)
        self.pantalla.blit(self.alto_puntaje_imagen,self.alto_puntaje_rect)   