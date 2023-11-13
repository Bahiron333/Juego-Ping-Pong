import pygame
from pygame.locals import *
import sys
from sonido import*
from juego import *

ancho=800
largo=600



main_image= pygame.image.load("img/fondoPrincipal.png")

def start_main():
    
    pygame.init()
    icono = pygame.image.load("img/icono.ico")
    pygame.display.set_icon(icono)
    pygame.display.set_caption("Pong")
    windows = pygame.display.set_mode((800,600))
    windows.blit(main_image,(0,0))

    font=pygame.font.SysFont(None,40,bold=True)
    letrero_boton1 = font.render('1 Jugador',True,'white')
    letrero_boton2 = font.render('2 Jugadores',True,'white')
    button_1 = pygame.Rect(50,400,280,60)#ubicacion y tamaño del boton
    button_2 = pygame.Rect(50,480,280,60)

    #------------------------------------------------#
    #boton de un solo juador
    windows.blit(letrero_boton1,(button_1.x+60,button_1.y+15))
    
    #Boton de dos jugadores
    windows.blit(letrero_boton2,(button_2.x+60,button_2.y+15))
    #------------------------------------------------#


    #Sonidos
    sonido_inicio = Sonido("sound/start/musica_inicio.wav",0.5)
    sonido_boton1 = Sonido("sound/start/boton_mouse.wav",0.5)
    sonido_boton2 = Sonido("sound/start/boton_mouse.wav",0.5)

    contador_boton1 = 1
    contador_boton2 = 1

    sonido_inicio.sound_play()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_1.collidepoint(event.pos):
                    sonido_inicio.sound_stop()
                    sonido_boton1.set_ruta("sound/start/boton.wav")
                    sonido_boton1.sound_play() 
                    if main_jugador(True,1):
                      pygame.display.update()
                      start_main()
                    else:
                       pygame.display.quit()
                    return True
                if button_2.collidepoint(event.pos):
                    sonido_inicio.sound_stop()
                    sonido_boton2.set_ruta("sound/start/boton.wav")
                    sonido_boton2.sound_play() 
                    if main_jugador(True,2):
                        pygame.display.update()
                        start_main()
                    else:
                        pygame.display.quit()
                    return True
                
        #Funcionalidad de cambio de color para el boton "de un jugador"
        a,b = pygame.mouse.get_pos()
        if button_1.x <= a <= button_1.x +280 and button_1.y <= b <= button_1.y +60:
            pygame.draw.rect(windows,("lightcyan"), button_1)#dibujamos el boton  
            letrero_boton1 = font.render('1 Jugador',True,'lightskyblue')
            if contador_boton1 == 1:
                sonido_boton1.sound_play()
                contador_boton1+=1
        else:
            pygame.draw.rect(windows,("lightskyblue"),button_1)
            letrero_boton1 = font.render('1 Jugador',True,'white')
            sonido_boton1.sound_stop()
            contador_boton1=1

        #Funcionalidad de cambio de color para el boton "dos jugadores"
        if button_2.x <= a <= button_2.x +280 and button_2.y <= b <= button_2.y +60:
            pygame.draw.rect(windows,("lightcyan"), button_2)#dibujamos el boton
            letrero_boton2 = font.render('2 Jugadores',True,'lightskyblue') 
            if contador_boton2 == 1:
                sonido_boton2.sound_play()
                contador_boton2+=1
        else:
            pygame.draw.rect(windows,("lightskyblue"),button_2)
            letrero_boton2 = font.render('2 Jugadores',True,'white')
            sonido_boton2.sound_stop()
            contador_boton2=1

        windows.blit(letrero_boton1,(button_1.x+60,button_1.y+15))
        windows.blit(letrero_boton2,(button_2.x+60,button_2.y+15))

        pygame.display.update()


start_main()