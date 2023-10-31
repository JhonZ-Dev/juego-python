import sys
import pygame
from alien import Alien
from bala import Bala
def verificar_eventos_keydown(event,ai_configuraciones, pantalla, nave,balas):
    """Responde a los pulsaciones de teclas"""
    if event.key == pygame.K_RIGHT:
        nave.moving_rigth=True
    elif event.key == pygame.K_LEFT:
        nave.moving_left = True
    elif event.key == pygame.K_SPACE:
        fuego_bala(ai_configuraciones,pantalla,nave,balas)
    elif event.key == pygame.K_q:
        sys.exit()
        
            
        
        
        
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
            

def actualizar_pantalla(ai_configuraciones, pantalla, nave,aliens,balas):
    """Actualiza las imagenes en la pantalla y pasa a la nueva ventana"""
    pantalla.fill(ai_configuraciones.bg_color)  #aqui se establece el fondo de la pantalla durante cada pasada por el bucle 
    #vuelve a dibujar todas las balas detras de la nave y los extraterrrestres
    for bala in balas.sprites():
        bala.draw_bala()
    nave.blitme()
    aliens.draw(pantalla)
    pygame.display.flip() #haga visible una pantalla mas reciente


def update_balas(ai_configuraciones,pantalla,nave,aliens,balas):
    """actualiza la posicion de la basla y elimna las antihguas"""
    #actualiza las posiciones de las balas
    balas.update()
    for bala in balas.copy():
        if bala.rect.bottom <= 0:
            balas.remove(bala)
    check_bala_alien_colisiones(ai_configuraciones,pantalla,nave,aliens,balas)
    

def check_bala_alien_colisiones(ai_configuraciones,pantalla,nave,aliens,balas):
    """Responde a las colisiones entre balas y aliens"""
    #elimina cualquier bala y alien que hayan colisionado
    collisions = pygame.sprite.groupcollide(balas, aliens, True, True)
    if len(aliens)==0:
        #elimina las balas existentes y crea una nueva flota
        balas.empty()
        crear_flota(ai_configuraciones,pantalla,nave,aliens)

def fuego_bala(ai_configuraciones,pantalla, nave, balas):
    """Dispara una vala si aun no ha alncanzado el limite"""
    #crea una nueva bala y la agrega
    if len(balas) < ai_configuraciones.balas_allowed:
        nueva_bala = Bala(ai_configuraciones,pantalla,nave)
        balas.add(nueva_bala)

def get_number_aliens_x(ai_configuraciones, alien_width):
    """DETERMINAR EL NUMERO DE ALIENS QUE CABEN EN UNA FILA"""
    available_space_x = ai_configuraciones.screen_width -2 * alien_width
    numbers_aliens_x=int( available_space_x /(2*alien_width))
    return numbers_aliens_x

def get_numbers_rows(ai_configuraciones,nave_height,alien_height):
    """determina el numero de alienigenas por el numero de filas de aliens que se ajustan en la pantalla"""
    available_space_y = (ai_configuraciones.screen_height - (3*alien_height)-nave_height)
    numbers_rows = int(available_space_y/(2*alien_height))
    return numbers_rows


def crear_alien(ai_configuraciones, pantalla, aliens,alien_number,row_number):
    """pass"""
     #crea un alieny lo coloca en la fila
    alien = Alien(ai_configuraciones,pantalla)
    alien_width = alien.rect.width
    alien.x= alien_width+2*alien_width*alien_number
    alien.rect.x=alien.x
    alien.rect.y=alien.rect.height+2*alien.rect.height*row_number
    aliens.add(alien)
    
    

def crear_flota(ai_configuraciones,pantalla,nave,aliens):
    """Crea una floata de aliens"""
    #crea un alien y encuentra el numero de alien  seguido
    #El espcio entre cada alie es igual a un ancho del alien
    alien = Alien(ai_configuraciones,pantalla)
    #alien_width =alien.rect.width
    numbers_aliens_x=get_number_aliens_x(ai_configuraciones, alien.rect.width)
    numbers_rows = get_numbers_rows(ai_configuraciones, nave.rect.height, alien.rect.height)
    
    #crea la flota de aliens
    for row_number in range (numbers_rows):
        for alien_number in range(numbers_aliens_x):
            crear_alien(ai_configuraciones,pantalla,aliens,alien_number,row_number)

def check_fleet_edges(ai_configuraciones,aliens):
    """Responde apropiadamente si algun alienigena alcanza un borde"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_configuraciones,aliens)
            break

def change_fleet_direction(ai_configuraciones,aliens):
    """Hace que toda la flota descienda y cambie de direccion"""
    for alien in aliens.sprites():
        alien.rect.y += ai_configuraciones.fleet_drop_speed
        ai_configuraciones.fleet_direction *= -1            

def update_aliens(ai_configuraciones,aliens):
    """actualiza las posiciones de todos los aliens"""
    check_fleet_edges(ai_configuraciones,aliens)
    aliens.update()
    
    
    #busca colisiones de aliens con nave
    if pygame.sprite.spritecollideany(nave,aliens):
        print("Nave golpeada")
       
    