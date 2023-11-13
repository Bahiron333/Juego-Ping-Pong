import pygame
from pygame.locals import *
from sonido import*
import sys

ventanaHor=800#Ventana horizontal
ventanaVer=550#ventana vertical

class raqueta:
    def __init__(self):
        pygame.init()
        try:
            self.imagen=pygame.image.load("img/raqueta.png").convert_alpha()#imagen
        except:
            print("hola")
            sys.exit()
        self.ancho,self.alto = self.imagen.get_size()
        self.x=0
        self.y=ventanaVer/2-self.alto/2
        self.dir_y=0#direccion igual a 0
        self.sound_paleta = Sonido("sound/gameplay/rebote_paleta.wav",1.0)

    def set_sonido_raqueta(self,vol):
        self.sound_paleta.set_volumen(vol)

    def movimiento(self):
        self.y+=self.dir_y
        if self.y<=0:
            self.y = 0
        if self.y+self.alto>=ventanaVer:
            self.y=ventanaVer-self.alto
    
    def movimiento_maqui(self,pelota):
        if self.y>pelota.y-50 and self.y>=1:
            self.dir_y=-4.1
        elif self.y<pelota.y and self.y+self.alto<=ventanaVer-3:
            self.dir_y=+4.2
        else:
            self.dir_y=0
        self.y+=self.dir_y

    def golpear(self,pelota):

        if(
            pelota.x<self.x+self.ancho
            and pelota.x > self.x
            and pelota.y+pelota.alto>self.y
            and pelota.y<self.y+self.alto
        ):
            pelota.dir_x=-pelota.dir_x
            pelota.x=self.x+self.ancho

            self.sound_paleta.sound_play()
        
    def reinicio(self):
        self.y=ventanaVer/2-self.alto/2

    def golpear_maquina(self,pelota):
        

        if(
            pelota.x+self.ancho > self.x
            and pelota.x < self.x + self.ancho 
            and pelota.y+pelota.alto>self.y
            and pelota.y<self.y+self.alto
        ):
            pelota.dir_x=-pelota.dir_x
            pelota.x=self.x-self.ancho
            self.sound_paleta.sound_play()