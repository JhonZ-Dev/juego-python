import sys
import pygame

def verificar_eventos():
    """Responde a las pulsaciones y teclas"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def actualizar_pantalla(ai_configuraciones, pantalla, nave):
    """Actualiza las imagenes en la pantalla y pasa a la nueva ventana"""
    