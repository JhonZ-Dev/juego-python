
import pygame #crear el juego
from configuraciones import Configuraciones
from nave import Nave
import funciones_juego as fj

def run_game():
    pygame.init()
    ai_configuraciones = Configuraciones()
    pantalla = pygame.display.set_mode((ai_configuraciones.screen_width,ai_configuraciones.screen_height)) #crear ventana de visualización
    pygame.display.set_caption("Invasion alienigena");
    
    #crea la nave
    nave = Nave(pantalla)
    
    #color de fondo

    while True:
        #bucle de animación del juego
        #eventos y juegos por ejemplo mover el raton, etc
        fj.verificar_eventos(nave)
        fj.actualizar_pantalla(ai_configuraciones,pantalla,nave)
        
run_game()            

