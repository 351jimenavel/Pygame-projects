import pygame

# 1. Inicializar los atributos etc de pygame
pygame.init()

# 2. Set the height and width of the window screen as a tuple
screen = pygame.display.set_mode((800,600))     # w,h

##### Events: anything that is happening inside the game window

# 3. Title and Icon
pygame.display.set_caption("Space Invader")    # Cambiar el titulo de la ventana (en la esquina superior izquierda)
icon = pygame.image.load('icon-window.png')
pygame.display.set_icon(icon)

## 5. How to add images into the game
# Jugador
jugador_img = pygame.image.load('player.png')
## posicion (coordenadas) donde estara la imagen segun las dimensiones del screen
jugadorX = 370
jugadorY = 480

# variables para los cambios de posicion
jugadorX_cambio = 0
jugadorY_cambio = 0

# 6. Movement of an object
def jugador(x,y):
    # syntax: destination_surface.blit(source_surface, (x,y))
    screen.blit(jugador_img,(x, y))   # blit means 'to draw'


# 4. Game Loop
running = True
while running:
    # RGB: Red, Green, Blue
    screen.fill((0,0,50))

    '''
    Movimiento manual
    jugadorX += 0.1
    jugadorX -= 0.1
    jugadorY += 0.1
    jugadorY -= 0.1
    '''

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # 7. Keyboard input controls and key pressed event
        # if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                jugadorX_cambio = -0.2
            if event.key == pygame.K_RIGHT:
                jugadorX_cambio = 0.2
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                jugadorX_cambio = 0

    ## Sumar el cambio a la posicion actual del jugador
    jugadorX += jugadorX_cambio

    # 8. Adding boundaries
    if jugadorX <= 0:
        jugadorX = 0
    elif jugadorX >= 736:       # 736 porque la imagen tiene 64px
        jugadorX = 736

    jugador(jugadorX,jugadorY)          # se hace el llamado despues del screen.fill porque ese es el 'lienzo' donde estara el jugador

    # Cada vez que se hagan cambios al game hay que actualizarlo
    pygame.display.update()     # !! importante
    ###
