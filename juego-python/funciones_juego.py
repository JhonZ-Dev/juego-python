import sys
import pygame
from bala import Bala
def verificar_eventos_keydown(event,ai_configuraciones, pantalla, nave,balas):
    """Responde a los pulsaciones de teclas"""
    if event.key == pygame.K_RIGHT:
        nave.moving_rigth=True
    elif event.key == pygame.K_LEFT:
        nave.moving_left = True
    elif event.key == pygame.K_SPACE:
        fuego_bala(ai_configuraciones,pantalla,nave,balas)
        
            
        
        
        
def verificar_eventos_keyup(event,nave):
    """Responde a los pulsaciones de teclas"""
    if event.key == pygame.K_RIGHT:
        nave.moving_rigth=False
    elif event.key == pygame.K_LEFT:
        nave.moving_left = False
        
        
def verificar_eventos(ai_configuraciones,pantalla,nave,balas):
    """Responde a las pulsaciones y teclas"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            verificar_eventos_keydown(event,ai_configuraciones,pantalla,nave,balas)
            
                    
        elif event.type == pygame.KEYUP:
            verificar_eventos_keyup(event,nave)
            

def actualizar_pantalla(ai_configuraciones, pantalla, nave,balas):
    """Actualiza las imagenes en la pantalla y pasa a la nueva ventana"""
    pantalla.fill(ai_configuraciones.bg_color)  #aqui se establece el fondo de la pantalla durante cada pasada por el bucle 
    #vuelve a dibujar todas las balas detras de la nave y los extraterrrestres
    for bala in balas.sprites():
        bala.draw_bala()
    nave.blitme()
    pygame.display.flip() #haga visible una pantalla mas reciente


def update_balas(balas):
    """actualiza la posicion de la basla y elimna las antihguas"""
    #actualiza las posiciones de las balas
    balas.update()
    for bala in balas.copy():
        if bala.rect.bottom <= 0:
            balas.remove(bala)

def fuego_bala(ai_configuraciones,pantalla, nave, balas):
    """Dispara una vala si aun no ha alncanzado el limite"""
    #crea una nueva bala y la agrega
    if len(balas) < ai_configuraciones.balas_allowed:
        nueva_bala = Bala(ai_configuraciones,pantalla,nave)
        balas.add(nueva_bala)
    