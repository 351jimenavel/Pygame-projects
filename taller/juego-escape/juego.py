# Este archivo contiene la clase Juego
import pygame
from jugador import Jugador

class Juego:

    def __init__(self):
        pygame.init()
        self.ancho_screen = 600
        self.alto_screen = 360
        self.screen = pygame.display.set_mode((self.ancho_screen, self.alto_screen))
        pygame.display.set_caption('Escaping Game')
        self.icon = pygame.image.load('recursos/escape.png')
        pygame.display.set_icon(self.icon)
        self.fondo = pygame.image.load('recursos/fondo.jpg')
        self.jugador = Jugador()
        self.reloj = pygame.time.Clock()
    
    def ejecutar(self):

        running = True
        while running:

            self.screen.fill((0,0,50))


            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    running = False

            teclas = pygame.key.get_pressed()
            if teclas[pygame.K_LEFT]:
                self.jugador.mover_izquierda()
            elif teclas[pygame.K_RIGHT]:
                self.jugador.mover_derecha()
                # if evento.type == pygame.KEYDOWN:
                #     if evento.key == pygame.K_LEFT:
                #         self.jugador.mover_izquierda()
                #     if evento.key == pygame.K_RIGHT:
                #         self.jugador.mover_derecha()

                # if evento.type == pygame.KEYUP:
                #     if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                #         self.jugador.no_mover()

            self.screen.blit(self.fondo, (0,0))
            self.jugador.dibujar(self.screen)

            pygame.display.update()
            self.reloj.tick(60)
