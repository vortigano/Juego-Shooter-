import pygame
from accesoDatos import AccesoDatos


class Jugador():
    def __init__(self):
        self.accesoDatos=AccesoDatos()
        self.posX=340
        self.posY=625
        self.banderaVida=True
        self.puntos=0
        self.nivel=1
        self.bala=pygame.image.load("img/bala.png")
        self.bala.set_colorkey([255,255,255])
        self.coordYBala=635
        self.BanderaBala=True
        self.BanderaImpacto=True
        self.inicial=True
        self.coordXBalaInicial=self.posX
        self.disparo=False
        
        self.tecla_disparo=False
        
        
    def setearJugador(self,nombre,seleccion):
        self.nombre=nombre 
        self.seleccion=seleccion
        self.caracteristicas=self.accesoDatos.buscarAvion(seleccion)
        self.velocidadMovimiento=self.caracteristicas[2]
        self.velocidadDisparo=self.caracteristicas[3]
        self.potenciaDisparo=self.caracteristicas[4]
        self.vida=self.caracteristicas[5]
        if self.seleccion==1:
            self.image=pygame.image.load("img/Pampa.png").convert()
        if self.seleccion==2:
            self.image=pygame.image.load("img/Tango.png").convert()
        if self.seleccion==3:
            self.image=pygame.image.load("img/Puma.png").convert()

        self.image.set_colorkey([16,25,57])

    def dibujarJugador(self, pantalla):
        pantalla.blit(self.image, [self.posX, self.posY])

    def moverJugador(self, event, pantalla):

        if self.coordYBala<-1:
            self.BanderaBala=False
            
        # alternativa para evitar bloqueo de teclado y que se pierdan pulsaciones
        if self.tecla_disparo == False and pygame.key.get_pressed()[pygame.K_SPACE] == True and self.disparo==False:
            self.tecla_disparo = True
            self.disparo=True
            self.coordXBalaInicial=self.posX+48
        if self.tecla_disparo == True and pygame.key.get_pressed()[pygame.K_SPACE] == False:
            self.tecla_disparo = False
            
        if pygame.key.get_pressed()[pygame.K_LEFT] == True and self.posX > 10:
            self.posX+=-self.velocidadMovimiento
        if pygame.key.get_pressed()[pygame.K_RIGHT] == True and self.posX < 662:
            self.posX+=self.velocidadMovimiento
        
        if self.disparo:
            if self.coordYBala>-1:
                self.coordYBala-=self.velocidadDisparo
                pantalla.blit(self.bala, (self.coordXBalaInicial, self.coordYBala)) 
            if self.coordYBala<0:
                self.disparo=False

    