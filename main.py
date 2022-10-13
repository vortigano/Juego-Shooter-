import pygame
from mapa import Mapa
from jugador import Jugador
from elementos import Avion1, Avion2, Misil1, Misil2, Nubes, Estrella
pygame.init()

medidaPantalla = (800,750)
pantalla = pygame.display.set_mode(medidaPantalla)
reloj = pygame.time.Clock()

vidaJugador = True
dia= True
colisiones=0
colision=False
mapa= Mapa()
mapa.setearMapa(dia)
jugador=Jugador()
nubes=Nubes()
misil1=Misil1()
misil2=Misil2()
#colisionR=ColisionRoja()
estrella=Estrella()
avion1= Avion1()
avion2=Avion2()

#definirPantallaInicio


while vidaJugador:
    mapa.dibujarMapa(pantalla)
    nubes.dibujarNubes(pantalla)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            vidaJugador = False

        if jugador.BanderaBala==False:
            jugador.coordYBala=635
            jugador.BanderaBala=True

    jugador.moverJugador(event, pantalla)
    jugador.dibujarJugador(pantalla)
    rectJ=jugador.image.get_rect(x=jugador.posX, y=jugador.posY)

    if jugador.puntos<80:                       #################################################---NIVEL1---
        rectA1=avion1.imagen.get_rect(x=avion1.coordX, y=avion1.coordY)
        avion1.dibujarAvion(pantalla,4.5,5)
        if rectJ.colliderect(rectA1):   #agregar colision balas
            pass
        
    
    if jugador.puntos>=80 and jugador.puntos<150:    ############################################---NIVEL2---
        rectM1=misil1.misil1[0].get_rect(x=misil1.coordX, y=misil1.coordY)
        rectM2=misil2.misil2[0].get_rect(x=misil2.coordX, y=misil2.coordY)
        misil1.dibujarMisil(pantalla)
        misil2.dibujarMisil(pantalla)
        if rectJ.colliderect(rectM1) or rectJ.colliderect(rectM2):
            pass


    if jugador.puntos>=150 and jugador.puntos<250:   ############################################---NIVEL3---
        rectA1=avion1.imagen.get_rect(x=avion1.coordX, y=avion1.coordY)
        rectA2=avion2.imagen.get_rect(x=avion2.coordX, y=avion2.coordY)
        avion1.dibujarAvion(pantalla,4.5,5)
        avion2.dibujarAvion(pantalla, 4.5,6)
        if rectJ.colliderect(rectA1) or rectJ.colliderect(rectA2):
            pass

    if jugador.puntos>=250 and jugador.puntos<450:   ############################################---NIVEL4---
        pass


    #estrella.caer(pantalla)
    #if colision==True:
    #    colision=False
    #    colisiones+=1
    #if colisiones ==3:
     #   vidaJugador=False

#definirPantallaFin

    pygame.display.flip()
    reloj.tick(60)

