import sys
import pygame

def verificar_eventos(nave):
    """Responde a las pulsaciones y teclas"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                nave.moving_rigth=True
            elif event.type == pygame.K_LEFT:
                nave.moving_left == True
                    
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                nave.moving_rigth = False
            elif event.key == pygame.K_LEFT:
                nave.moving_left = False  

def actualizar_pantalla(ai_configuraciones, pantalla, nave):
    """Actualiza las imagenes en la pantalla y pasa a la nueva ventana"""
    pantalla.fill(ai_configuraciones.bg_color)  #aqui se establece el fondo de la pantalla durante cada pasada por el bucle 
    nave.blitme()
    pygame.display.flip() #haga visible una pantalla mas reciente