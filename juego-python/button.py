import pygame.font

class Button():
    """Clase para crear botones"""
    def __init__(self,ai_configuraciones,pantalla,msg):
        """Inicializa los atributos del boton"""
        self.pantalla = pantalla
        self.pantalla_rect = pantalla.get_rect()
        
        #dimensiones y propiedades del boton
        self.width, self.height = 200,50
        self.button_color = (0,255,0)
        self.text_color = (255,255,255)
        self.font = pygame.font.SysFont(None,48)
        
        #construye el objeto rectangulo del boton y lo centra
        self.rect = pygame.Rect(0,0,self.width,self.height)
        self.rect.center = self.pantalla_rect.center
        
        #el mensaje del boton debe prepararse una vez
        self.prep_msg(msg)