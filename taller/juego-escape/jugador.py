# Este archivo contiene la clase Jugador
import pygame

class Jugador:

    def __init__(self):
        # x e y son las posiciones iniciales del jugador
        self.x = 0
        self.y = 250
        # ancho y alto son las dimensiones del jugador
        self.ancho = 20
        self.alto = 20
        # que color sera
        self.color = (255,255,255)
        # cuantos FPS se movera
        self.velocidad = 5
        self.jugador_rect = pygame.Rect(self.x, self.y, self.ancho, self.alto)

    # acciones
    def dibujar(self, pantalla):
        #pygame.draw.line(pantalla, self.color, (0,100),(100,100), 5)
        #jugador = pygame.draw.rect(pantalla,self.color,(self.x, self.y, self.ancho, self.alto))
        # para imagenes
        # pantalla.blit(self.imagen, (self.x, self.y))
        pygame.draw.rect(pantalla,self.color,self.jugador_rect)
    
    def mover_izquierda(self):
        if self.jugador_rect.x > 0:
            self.jugador_rect.move_ip(-self.velocidad,0) 

    def mover_derecha(self):
        if self.jugador_rect.x < 600 - self.ancho:
            self.jugador_rect.move_ip(self.velocidad,0)

    def no_mover(self):
        self.jugador_rect.move_ip(0,0)
    
    def colision(self, obstaculos):
        return self.jugador_rect.colliderect(obstaculos)

jugador = Jugador()