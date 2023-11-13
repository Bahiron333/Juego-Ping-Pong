import pygame
from pygame.locals import *
from pelota import *
from informacion import*
import sys
from sonido import*
from raqueta import *
from victoria import *
from derrota import *

ventanaHor=800#Ventana horizontal
ventanaVer=600#ventana vertical
white = (225,225,255)#color blanco
negro=(0,0,0,)#color negro


icono = pygame.image.load("img/icono.ico")
pygame.display.set_icon(icono)
pygame.init()
win = pygame.display.set_mode((ventanaHor,ventanaVer))
pygame.display.set_caption("Pong")
pelota= PelotaP('img/pelota.png')
fuente = pygame.font.Font(None,60)    
fondo1 = pygame.image.load('img/fondo1.png')#fondo de imagen un jugador
fondo2 = pygame.image.load('img/fondo2.png')
menu = pygame.image.load("img/menu.png")

simbolo_inicio = pygame.image.load("img/inicio.png")
simbolo_pausa = pygame.image.load("img/pausa.png")
simbolo_continuar = pygame.image.load("img/despausa.png")
simbolo_musica = pygame.image.load("img/musica.png")
simbolo_sin_musica = pygame.image.load("img/sin_musica.png")
simbolo_sonido = pygame.image.load("img/sonido.png")
simbolo_sin_sonido = pygame.image.load("img/sin_sonido.png")
simbolo_reinicio = pygame.image.load("img/reinicio.png")


sound_fondo = Sonido("sound/gameplay/fondo.wav",0.3)
sound_button = Sonido("sound/gameplay/boton_juego.wav",0.3)

def main_jugador(start,tipo_juego):
        
        if tipo_juego==1:
            main_informacion_jugador(tipo_juego)
        elif tipo_juego == 2:
            main_informacion_jugador(tipo_juego)

        inicio=False
        raqueta_1= raqueta()
        raqueta_1.x=20
        raqueta_2 = raqueta()
        raqueta_2.x=ventanaHor-20-raqueta_2.ancho
        raqueta_maqui = raqueta()
        raqueta_maqui.x=ventanaHor-20-raqueta_maqui.ancho

        jugando = start
        
        contador = 1

        #Es verdadero cuando la pausa, la musica, el sonido estan encendidos y falso cuando esten apagados o pausados
        pausa = True
        musica_fondo=True
        sonido_fondo= True
        volver_start=False

        sound_fondo.sound_play()
        sound_button.sound_play()

        while(jugando):


            #Sesion de menu#############################################
           
            win.blit(simbolo_musica,(678,12))
            win.fill(white)
            win.blit(menu,(0,0))

            #////////////////////////////opciones////////////////////////

            boton_inicio = pygame.Rect(500,2,45,45)
            boton_pausa = pygame.Rect(560,2,45,45)
            boton_reinicio = pygame.Rect(610,2,45,45)
            boton_musica = pygame.Rect(670,2,45,45)
            boton_sonido = pygame.Rect(720,2,45,45)

            color_boton(boton_inicio,win)
            color_boton(boton_pausa,win)
            color_boton(boton_reinicio,win)
            color_boton(boton_musica,win)
            color_boton(boton_sonido,win)

            win.blit(simbolo_inicio,(508,8))
            win.blit(simbolo_reinicio,(620,13))
            #condicionales para determinar cual simbolo va en el boton

            if pausa:#para el de pausar
                win.blit(simbolo_pausa,(575,15))
            else:
                win.blit(simbolo_continuar,(575,15))

            if musica_fondo:#para la musica
                win.blit(simbolo_musica,(678,12))
            else:
                win.blit(simbolo_sin_musica,(678,12))

            if sonido_fondo:#para el sonido
                 win.blit(simbolo_sonido,(728,11))
            else:
                 win.blit(simbolo_sin_sonido,(728,11))

            #//////////////////////////////////////////////////////////////////////
            #Sesion de juego//////////////////////////////////////////////////////

            #bucle juego

            if pausa:
                 
                pelota.movimiento()
                #Si algun jugador gano un punto que el contador vuelva a 1
                if pelota.rebotar():
                    contador=1
                    raqueta_1.reinicio()
                    raqueta_maqui.reinicio()
                    raqueta_2.reinicio()

                if tipo_juego == 1:
                    raqueta_1.movimiento()
                    raqueta_maqui.movimiento_maqui(pelota)
                    raqueta_1.golpear(pelota)
                    raqueta_maqui.golpear_maquina(pelota)
                    win.blit(fondo1,(0,50))
                    win.blit(raqueta_1.imagen,(raqueta_1.x,raqueta_1.y+50))
                    win.blit(raqueta_maqui.imagen,(raqueta_maqui.x,raqueta_maqui.y+50))
                

                elif tipo_juego == 2:
                    raqueta_1.movimiento()
                    raqueta_2.movimiento()
                    raqueta_1.golpear(pelota)
                    raqueta_2.golpear_maquina(pelota)
                    win.blit(fondo2,(0,50))
                    win.blit(raqueta_1.imagen,(raqueta_1.x,raqueta_1.y+50))
                    win.blit(raqueta_2.imagen,(raqueta_2.x,raqueta_2.y+50))

                win.blit(pelota.imagen,(pelota.x,pelota.y+50))

                #Mostrar puntuacion
                text=f"{pelota.puntuacion}    {pelota.puntuacion_maqui}"
                letre=fuente.render(text,True,negro)
                tablero = pygame.Rect(322,1,150,48)
                pygame.draw.rect(win,'#FFFFFF',tablero)
                win.blit(letre,(350,10))

                if pelota.get_final():
                    reiniciar_juego(raqueta_1,raqueta_2,raqueta_maqui,musica_fondo,sonido_fondo)
                    jugando=False
                    inicio=True

            else:
                imagen_pausa = pygame.image.load("img/JuegoPausado.png")                
                win.blit(imagen_pausa,(0,50))
                     
            #Sesion de eventos///////////////////////////////////////////////////////////////

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    jugando=False
                    sys.exit()
                    pygame.display.quit()

                    #Juego de 1
                if tipo_juego == 1:
                    if event.type == pygame.KEYDOWN:
                            if event.key==pygame.K_w or event.key==pygame.K_UP:
                                raqueta_1.dir_y=-4
                            if event.key==pygame.K_s or event.key == pygame.K_DOWN:
                                raqueta_1.dir_y=4
                    if event.type == pygame.KEYUP:
                        if event.key==pygame.K_w or event.key==pygame.K_UP:
                                raqueta_1.dir_y=0
                        if event.key==pygame.K_s or event.key==pygame.K_DOWN:
                                raqueta_1.dir_y=0
                    #juego de dos
                elif tipo_juego == 2:
                        #jugador 1 movimientos
                        if event.type == pygame.KEYDOWN:
                            if event.key==pygame.K_w :
                                raqueta_1.dir_y=-4
                            if event.key==pygame.K_s:
                                raqueta_1.dir_y=4
                        if event.type == pygame.KEYUP:
                            if event.key==pygame.K_w:
                                    raqueta_1.dir_y=0
                            if event.key==pygame.K_s:
                                    raqueta_1.dir_y=0
                        #jugador dos movimientos
                        if event.type == QUIT:
                            jugando=False
                        if event.type == pygame.KEYDOWN:
                            if event.key==pygame.K_UP:
                                raqueta_2.dir_y=-4
                            if event.key == pygame.K_DOWN:
                                raqueta_2.dir_y=4
                        if event.type == pygame.KEYUP:
                            if event.key==pygame.K_UP:
                                    raqueta_2.dir_y=0
                            if event.key==pygame.K_DOWN:
                                    raqueta_2.dir_y=0
                         
                if event.type == pygame.MOUSEBUTTONUP:
                    if boton_inicio.collidepoint(event.pos):
                        reiniciar_juego(raqueta_1,raqueta_2,raqueta_maqui,musica_fondo,sonido_fondo)
                        volver_start=True
                        jugando=False
                        inicio=True
                    if boton_reinicio.collidepoint(event.pos):
                         reiniciar_juego(raqueta_1,raqueta_2,raqueta_maqui,musica_fondo,sonido_fondo)
                         if tipo_juego == 1:
                            main_informacion_jugador(tipo_juego)
                         elif tipo_juego == 2:
                            main_informacion_jugador(tipo_juego)
                         pygame.display.update()

                         jugando=True
                    if boton_pausa.collidepoint(event.pos):
                        sound_button.sound_play()
                        if pausa:
                            win.blit(simbolo_continuar,(575,15))
                            contador=1
                            pausa = False
                        else:
                            win.blit(simbolo_pausa,(575,15))
                            pausa=True
                    if boton_musica.collidepoint(event.pos):
                        sound_button.sound_play()
                        if musica_fondo:       
                            win.blit(simbolo_sin_musica,(678,12))
                            sound_fondo.set_volumen(0.0)
                            musica_fondo = False
                        else:
                            win.blit(simbolo_musica,(678,12))
                            sound_fondo.set_volumen(0.5)
                            musica_fondo = True  

                    if boton_sonido.collidepoint(event.pos):
                        sound_button.sound_play()
                        if sonido_fondo:
                            win.blit(simbolo_sin_sonido,(728,11))
                            raqueta_1.sound_paleta.set_volumen(0.0)
                            raqueta_maqui.sound_paleta.set_volumen(0.0)
                            pelota.set_sonido_pelota(0.0)
                            sound_button.set_volumen(0.0)
                            sonido_fondo=False
                        else:
                            win.blit(simbolo_sonido,(728,11))
                            raqueta_1.set_sonido_raqueta(1.0)
                            raqueta_maqui.set_sonido_raqueta(1.0)
                            pelota.set_sonido_pelota(0.5)
                            sound_button.set_volumen(0.5)
                            sonido_fondo=True  
                                        
            if contador <= 100:
              pygame.time.Clock().tick(60+contador)
            
            contador += 1
            pygame.display.update()
        sound_fondo.sound_stop()
        sound_fondo.set_volumen(0.5)
        sound_button.sound_stop()
        sound_fondo.set_volumen(0.5)
        if volver_start != True:
            ganador(pelota.get_nombre_ganador(),tipo_juego)
            pelota.set_final(False)
        return inicio


 

def color_boton(boton,ventana):
     #Funcionalidad de cambio de color para el boton "de un jugador"
    a,b = pygame.mouse.get_pos()
    if boton.x <= a <= boton.x +49 and boton.y <= b <= boton.y +49:
            pygame.draw.rect(ventana,("lightcyan"), boton)#dibujamos el boton  
    else:
            pygame.draw.rect(ventana,("#F0F8FF"),boton)


def reiniciar_juego(raq1,raq2,raq_maq,music,sound):

    if sound:
        sound_button.set_volumen(0.5)
        sound_button.sound_play()
    else:
        sound_button.set_volumen(0.0)
        sound_button.sound_stop()
    if music:
        sound_fondo.set_volumen(0.5)
        sound_fondo.sound_play()
    else:
        sound_button.set_volumen(0.0)
        sound_button.sound_stop()
    raq1.reinicio()
    raq2.reinicio()
    raq_maq.reinicio()
    pelota.limpiar()

def ganador(nombre,tipo_juego):
    
    if tipo_juego == 1:
        if nombre == "jugador":
            main_victoria(1)
        elif nombre == "maquina":
            main_derrota()
    if tipo_juego == 2:
        if nombre == "jugador":#victoria jugador 1
            main_victoria(2)
        elif nombre == "maquina":
            main_victoria(3)#victoria jugador 2

