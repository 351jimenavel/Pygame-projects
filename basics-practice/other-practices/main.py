import pygame

# Inicializar los atributos etc de pygame
pygame.init()

# Set the height and width of the window screen as a tuple
screen = pygame.display.set_mode((800,600))

##### Events: anything that is happening inside the game window

# Title and Icon
pygame.display.set_caption("Space Invadors")    # Cambiar el titulo de la ventana (en la esquina superior izquierda)
icon = pygame.image.load('icon-window.png')
pygame.display.set_icon(icon)

# Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # RGB: Red, Green, Blue
    screen.fill((0,0,50))
    # Cada vez que se hagan cambios al game hay que actualizarlo
    pygame.display.update()     # !! importante