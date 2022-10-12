import pygame, random

class Avion1():
    def __init__(self):
        self.coordX=random.randrange(0,220)
        self.coordY=-50
        self.cuadro=0
        self.imagen=pygame.image.load("img/Enemigo1.png")
        self.direct=4
        self.imagenBala=pygame.image.load("img/bala.png")
        self.coordXBala1=random.randrange(120,450)
        self.coordXBala2=random.randrange(460,700)
        self.coordYBala1=self.coordY
        self.coordYBala2=self.coordY
        self.banderaDireccion=True

    def dibujarAvion(self, pantalla,velX,velY):
        if self.banderaDireccion:
            if self.coordY<850:
                self.coordX+=velX
                self.coordY+=velY

            else:
                self.coordY=-30
                self.banderaDireccion=False
                self.coordX=random.randrange(375,750)

            pantalla.blit(self.imagen, (self.coordX, self.coordY))
        
        else:
            if self.coordY<850:
                self.coordX-=velX
                self.coordY+=velY

            else:
                self.coordY=-30
                self.banderaDireccion=True
                self.coordX=random.randrange(0,325)

            pantalla.blit(self.imagen, (self.coordX, self.coordY))


class Avion2():
    def __init__(self):
        self.coordX=random.randrange(500,780)
        self.coordY=-250
        self.cuadro=0
        self.imagen=pygame.image.load("img/Enemigo2.png")
        self.direct=-2

    def dibujarAvion(self, pantalla,velX,velY):
        if self.coordY<850:
            self.coordX-=velX
            self.coordY+=velY

        else:
            self.coordY=-250
            self.coordX=random.randrange(500,780)

        pantalla.blit(self.imagen, (self.coordX, self.coordY))
        
class Misil1():
    def __init__(self):
        self.coordX=random.randrange(750)
        self.coordY=-50
        self.cuadro=0
        self.misil1=[]
        self.misil1.append(pygame.image.load("img/misilA1.png"))
        self.misil1.append(pygame.image.load("img/misilA2.png"))
        self.direct=6
        self.puntaX=self.coordX+23
        self.puntaY=self.coordY+185       

    def dibujarMisil(self, pantalla):
        if self.coordY<850:

            if self.coordX >750:
                self.direct=-6
            if self.coordX < 50:
                self.direct=6

            if self.coordY%2==0:
                self.coordY+=6.5
                self.cuadro=0
                self.coordX+=self.direct
            else:
                self.coordY+=6.5
                self.cuadro=1
                self.coordX+=self.direct

        else:
            self.coordY=-50
            self.coordX=random.randrange(750)

        pantalla.blit(self.misil1[self.cuadro], (self.coordX, self.coordY))

class Misil2():
    def __init__(self):
        self.coordX=random.randrange(750)
        self.coordY=-220
        self.cuadro=0
        self.misil2=[]
        self.misil2.append(pygame.image.load('img/misilB1.png'))
        self.misil2.append(pygame.image.load('img/misilB2.png'))
        self.direct=6


    def dibujarMisil(self, pantalla):

        if self.coordY<850:

            if self.coordX >750:
                self.direct=-6
            if self.coordX < 50:
                self.direct=6

            if self.coordY%2==0:
                self.coordY+=5.5
                self.cuadro=1
                self.coordX+=self.direct
             
            else:
                self.coordY+=5.5
                self.cuadro=0
                self.coordX+=self.direct
        else:
            self.coordY=-220
            self.coordX=random.randrange(750)
                

        pantalla.blit(self.misil2[self.cuadro], (self.coordX, self.coordY))

class Nubes():
    def __init__(self):
        self.listaNubes=[]
        self.listaNubes.append(pygame.image.load('img/nube1.png'))
        self.listaNubes.append(pygame.image.load('img/nube2.png'))
        self.listaNubes.append(pygame.image.load('img/nube3.png'))
        self.coordX1=random.randrange(700)
        self.coordY1=-70
        self.coordX2=random.randrange(700)
        self.coordY2=-320
        self.coordX3=random.randrange(700)
        self.coordY3=-500
    
    def dibujarNubes(self, pantalla):
                
        if self.coordY1<850:
            pantalla.blit(self.listaNubes[2], (self.coordX1, self.coordY1))
            self.coordY1+=1.3
        else:
            self.coordY1=-70
        if self.coordY2<850:
            pantalla.blit(self.listaNubes[1], (self.coordX2, self.coordY2))
            self.coordY2+=1.3
        else:
            self.coordY2=-320
        if self.coordY3 <850:
            pantalla.blit(self.listaNubes[0], (self.coordX3, self.coordY3))      
            self.coordY3+=1.3
        else:
            self.coordY3=-500

class Estrella():
    def __init__(self):
        self.estrella=pygame.image.load('img/estrella.png').convert()
        self.estrella.set_colorkey([0,0,0])
        self.rect=self.estrella.get_rect()
        self.coordY=-50
        self.coordX=random.randrange(350)
    
    def caer(self, pantalla):
        self.coordY+=4
        self.coordX+=1
        pantalla.blit(self.estrella, (self.coordX, self.coordY))

class Vida():
    def __init__(self):
        self.vida=pygame.image.load('img/vida.png')

class ColisionRoja():
    def __init__(self):
        self.Y=600
        self.cuadro=0
        self.listaImg=[]
        self.Img0=pygame.image.load('img/Explosion1.png').convert()
        self.Img0.set_colorkey([255,255,255])
        self.Img1=pygame.image.load('img/Explosion2.png').convert()
        self.Img1.set_colorkey([255,255,255])
        self.Img2=pygame.image.load('img/Explosion1.png').convert()
        self.Img2.set_colorkey([255,255,255])
        self.listaImg.append(self.Img0)
        self.listaImg.append(self.Img1)
        self.listaImg.append(self.Img2)

    def explotarR(self, pantalla, coordX):
        print("inicio")
        for j in range(2):
            for i in range (8):
                if i<3:
                    pantalla.blit(self.listaImg[2], (coordX, self.Y))
                elif i<6:
                    pantalla.blit(self.listaImg[1], (coordX, self.Y))
                else:
                    pantalla.blit(self.listaImg[0], (coordX, self.Y))
                print("fin")
        print("fuera del for")
