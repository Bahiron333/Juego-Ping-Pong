import pygame
from pygame.locals import *
import random
from sonido import *
import sys

ventanaHor=800#Ventana horizontal
ventanaVer=550#ventana vertical

class PelotaP:
    def __init__(self,fichero_imagen):
        self.imagen = pygame.image.load(fichero_imagen).convert_alpha()#imagen pelota
        self.ancho,self.alto=self.imagen.get_size()#tamaño pelota
        self.x=ventanaHor/2-self.ancho/2#posicionar y en el centro
        self.y=ventanaVer/2-self.alto/2#posicionar x en el centro
        self.dir_x=random.choice([-6,6])#direccion pelota eje x
        self.dir_y=random.choice([-6,6])#direccion pelota eje y
        self.puntuacion = 0#puntuacion humano
        self.puntuacion_maqui = 0#puntuacion maquina
        self.sonido_pelota = Sonido("sound/gameplay/rebote.wav",0.5)
        self.volumen = 0.5
        self.resultado = ""
        self.final_juego=False

    def movimiento(self):
        self.x+=self.dir_x
        self.y+=self.dir_y

    def get_final(self):
        return self.final_juego
    
    def set_final(self,fin):
        self.final_juego = fin

    def reinicio(self):
        self.x=ventanaHor/2-self.ancho/2
        self.y=ventanaVer/2-self.alto/2
        self.dir_x=self.dir_x
        self.dir_y=random.choice([-5,5])
    
    def set_sonido_pelota(self,vol):
        self.volumen=vol
        self.sonido_pelota.set_volumen(self.volumen)

    def limpiar(self):
        self.puntuacion=0
        self.puntuacion_maqui=0
        self.reinicio()

    def get_resultado(self):
        return self.resultado
    
    def get_nombre_ganador(self):
        try:
            return self.nombre_ganador
        except:
            pygame.quit()
            sys.exit()
        
    
    def rebotar(self):
        if self.x<= -self.ancho:
            self.sonido_pelota.set_ruta("sound/gameplay/punto.wav")
            self.sonido_pelota.set_volumen(self.volumen)
            self.sonido_pelota.sound_play()
            self.reinicio()
            self.puntuacion_maqui+=1
            #Ganador
            if self.puntuacion_maqui >= 10:
                self.final_juego=True
                self.nombre_ganador = "maquina"
            else:
                self.final_juego=False
            return True
        if self.x>= ventanaHor:
            self.sonido_pelota.set_ruta("sound/gameplay/punto.wav")
            self.sonido_pelota.set_volumen(self.volumen)
            self.sonido_pelota.sound_play()
            self.reinicio()
            self.puntuacion+=1
            #Ganador
            if self.puntuacion >= 10:
               self.final_juego=True
               self.nombre_ganador="jugador"
            else:
                self.final_juego=False
            return True
        if self.y<=0:
            self.sonido_pelota.set_ruta("sound/gameplay/rebote.wav")
            self.sonido_pelota.set_volumen(self.volumen)
            self.sonido_pelota.sound_play()
            self.dir_y=-self.dir_y

            return False
        if self.y+self.alto>=ventanaVer:
            self.sonido_pelota.set_ruta("sound/gameplay/rebote.wav")
            self.sonido_pelota.set_volumen(self.volumen)
            self.sonido_pelota.sound_play()
            self.dir_y=-self.dir_y

            return False
