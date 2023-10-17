import sys #salir del jeugo
import pygame #crear el juego
from configuraciones import Configuraciones
from nave import Nave


def run_game():
    pygame.init()
    ai_configuraciones = Configuraciones()
    pantalla = pygame.display.set_mode((ai_configuraciones.screen_width,ai_configuraciones.screen_height)) #crear ventana de visualización
    pygame.display.set_caption("Invasion alienigena");
    
    #color de fondo

    while True:
        #bucle de animación del juego
        #eventos y juegos por ejemplo mover el raton, etc
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        pantalla.fill(ai_configuraciones.bg_color)  #aqui se establece el fondo de la pantalla durante cada pasada por el bucle 
        pygame.display.flip() #haga visible una pantalla mas reciente
        
run_game()            

