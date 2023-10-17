import sys #salir del jeugo
import pygame #crear el juego


def run_game():
    pygame.init()
    pantalla = pygame.display.set_mode((800,600)) #crear ventana de visualización
    pygame.display.set_caption("Invasion alienigena");
    
    #color de fondo
    bg_color =(243, 156, 18)
    while True:
        #bucle de animación del juego
        #eventos y juegos por ejemplo mover el raton, etc
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        pantalla.fill(bg_color)  #aqui se establece el fondo de la pantalla durante cada pasada por el bucle 
        pygame.display.flip() #haga visible una pantalla mas reciente
        
run_game()            

