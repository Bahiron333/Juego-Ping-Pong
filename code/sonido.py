import pygame

class Sonido:

    def __init__(self,ruta,volumen):

        #inicio/////////////////////////////////////////////////////////////////
        #musica de inicio
        self.sound = pygame.mixer.Sound(ruta)
        self.sound.set_volume(volumen)


    #Controla el sonido de inicio
    def sound_play(self):
        self.sound.play()

    def set_ruta(self,ruta):
        self.sound = pygame.mixer.Sound(ruta)
    
    def set_volumen(self,volumen):
        self.sound.set_volume(volumen)
        
    def sound_stop(self):
        self.sound.stop()
