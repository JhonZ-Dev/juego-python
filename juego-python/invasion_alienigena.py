
import pygame #crear el juego
from pygame.sprite import Group
from configuraciones import Configuraciones
from nave import Nave
import funciones_juego as fj

def run_game():
    pygame.init()
    ai_configuraciones = Configuraciones()
    pantalla = pygame.display.set_mode((ai_configuraciones.screen_width,ai_configuraciones.screen_height)) #crear ventana de visualización
    pygame.display.set_caption("Invasion alienigena");
    
    #crea la nave
    nave = Nave(ai_configuraciones,pantalla)
    #crea un grupo para almacenar las balas
    balas = Group()
    
    #color de fondo

    while True:
        #bucle de animación del juego
        #eventos y juegos por ejemplo mover el raton, etc
        fj.verificar_eventos(ai_configuraciones,pantalla,nave,balas)
        nave.update()
        balas.update()
        fj.actualizar_pantalla(ai_configuraciones,pantalla,nave,balas)
        
run_game()            

