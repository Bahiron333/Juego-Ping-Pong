import pygame
import pygame.locals 
import sys
import sonido

venHor = 800
venVer = 600

def main_derrota():
    
    pygame.init()

    sonido_victoria = sonido.Sonido("sound/gameplay/derrota.wav",0.5)
    sonido_boton1 = sonido.Sonido("sound/start/boton_mouse.wav",0.7)
    contador_sonido = 1

    main_image = pygame.image.load("img/derrota.png")
    icono = pygame.image.load("img/icono.ico")
    pygame.display.set_icon(icono)
    pygame.display.set_caption("Pong")
    windows_infor = pygame.display.set_mode((800,600))
    windows_infor.blit(main_image,(0,0))

    font_letrero_continuar = pygame.font.SysFont('arial',40,bold=True)
    letrero_continuar = font_letrero_continuar.render("Ok",True,(0,0,0))
   
    boton = pygame.Rect(83,265,90,90)
    windows_infor.blit(letrero_continuar,(86,268))
    informacion = True

    while informacion:

        if contador_sonido <= 1:
            sonido_victoria.sound_play()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if boton.collidepoint(event.pos):
                    sonido_victoria.sound_stop()
                    sonido_boton1.set_ruta("sound/start/boton.wav")
                    sonido_boton1.sound_play() 
                    informacion=False
                    return False
            
        x,y = pygame.mouse.get_pos()#Odtenemos las coordenadas del mouse

        if boton.x <= x <= boton.x + 90 and boton.y <=y <= boton.y+90:
            pygame.draw.rect(windows_infor,(255,255,255),boton)
            letrero_continuar = font_letrero_continuar.render("OK",True,(0,0,0))
        else:
            pygame.draw.rect(windows_infor,(0,0,0),boton)
            letrero_continuar = font_letrero_continuar.render("OK",True,(255,255,255))

        windows_infor.blit(letrero_continuar,(100,285))
        contador_sonido+=1
        pygame.display.update()
