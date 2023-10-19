import sys
import pygame

def verificar_eventos():
    """Responde a las pulsaciones y teclas"""
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()