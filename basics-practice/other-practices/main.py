import pygame

# Inicializar los atributos etc de pygame
pygame.init()

# Set the height and width of the window screen as a tuple
screen = pygame.display.set_mode((800,600))     # w,h

##### Events: anything that is happening inside the game window

# Title and Icon
pygame.display.set_caption("Space Invadors")    # Cambiar el titulo de la ventana (en la esquina superior izquierda)
icon = pygame.image.load('icon-window.png')
pygame.display.set_icon(icon)

## How to add images into the game
# Jugador
jugador_img = pygame.image.load('player.png')
## posicion (coordenadas) donde estara la imagen segun las dimensiones del screen
jugadorX = 370
jugadorY = 480

def jugador():
    # syntax: destination_surface.blit(source_surface, (x,y))
    screen.blit(jugador_img,(jugadorX, jugadorY))   # blit means 'to draw'

# Game Loop
running = True
while running:
    # RGB: Red, Green, Blue
    screen.fill((0,0,50))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    # se hace el llamado despues del screen.fill porque ese es el 'lienzo' donde estara el jugador
    jugador()

    # Cada vez que se hagan cambios al game hay que actualizarlo
    pygame.display.update()     # !! importante
    ###
