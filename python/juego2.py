import pygame
from random import randint
pygame.init()
ventana = pygame.display.set_mode((640,480))
pygame.display.set_caption("Ejemplo 3")
ball = pygame.image.load("pics/ball.png")
ballrect = ball.get_rect()
speed = [4,4]
ballrect.move_ip(0,0)
# Crea el objeto bate, y obtengo su rectángulo
bate = pygame.image.load("pics/bate.png")
baterect = bate.get_rect()
# Pongo el bate en la parte inferior de la pantalla
baterect.move_ip(240,450)
fuente = pygame.font.Font(None, 36)
fuente2 = pygame.font.Font(None, 36)
jugando = True
while jugando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jugando = False
    # Compruebo si se ha pulsado alguna tecla
    keys = pygame.key.get_pressed() 
    if keys[pygame.K_LEFT]:
        baterect = baterect.move(-3,0)
    if keys[pygame.K_RIGHT]:
        baterect = baterect.move(3,0)
    if keys[pygame.K_UP]:
        baterect = baterect.move(0,-3)
    if keys[pygame.K_DOWN]:
        baterect = baterect.move(0,3)
    # Compruebo si hay colisión
    if baterect.colliderect(ballrect):
        speed[1] = -speed[1]
 
    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > ventana.get_width():
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > ventana.get_height():
        speed[1] = -speed[1]
 
    if ballrect.bottom >= ventana.get_height():
        speed = [0,0]
        texto = fuente.render("Game Over", True, (125,125,125))
        texto_rect = texto.get_rect()
        texto_x = ventana.get_width() / 2 - texto_rect.width / 2
        texto_y = ventana.get_height() / 2 - texto_rect.height / 2
        ventana.blit(texto, [texto_x, texto_y])
    else:
        ventana.fill((252, 243, 207))
        ventana.blit(ball, ballrect)
        # Dibujo el bate
        ventana.blit(bate, baterect)

    
    pygame.display.flip()
    pygame.time.Clock().tick(60)
pygame.quit()