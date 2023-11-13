import pygame
import pygame.locals 
import sonido



def main_informacion_jugador(tipo):
    
    pygame.init()
    posicion_texto = (0,0)
    posicion_boton = (0,0)
    tamano_boton = (0,0)
    sonido_boton = sonido.Sonido("sound/start/boton.wav",0.5)

    if tipo ==1:
        main_image = pygame.image.load("img/informacion.png")
        posicion_texto = (290,450)
        posicion_boton = (270,430)
        tamano_boton = (250,80)
        
    elif tipo==2:
        main_image = pygame.image.load("img/informacion_jugadores.png")
        posicion_texto = (500,393)
        posicion_boton = (478,373)
        tamano_boton = (250,80)

    icono = pygame.image.load("img\icono.ico")
    pygame.display.set_icon(icono)
    pygame.display.set_caption("Pong")
    windows_infor = pygame.display.set_mode((800,600))
    windows_infor.blit(main_image,(0,0))

    font_letrero_continuar = pygame.font.Font(None,60)
    letrero_continuar = font_letrero_continuar.render("Continuar",True,(0,0,0))
    boton = pygame.Rect(posicion_boton,tamano_boton)
    windows_infor.blit(letrero_continuar,(posicion_texto))

    informacion = True
    while informacion:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if boton.collidepoint(event.pos):
                    sonido_boton.sound_play() 
                    informacion=False
                    return True
            
        x,y = pygame.mouse.get_pos()#Odtenemos las coordenadas del mouse
        boton_x, boton_y = tamano_boton
        if boton.x <= x <= boton.x + boton_x and boton.y <=y <= boton.y+boton_y:
            pygame.draw.rect(windows_infor,("lightcyan"),boton)
            letrero_continuar = font_letrero_continuar.render("Continuar",True,("lightskyblue"))
        else:
            pygame.draw.rect(windows_infor,("lightskyblue"),boton)
            letrero_continuar = font_letrero_continuar.render("Continuar",True,(255,255,255))

        windows_infor.blit(letrero_continuar,posicion_texto)
        pygame.display.update()


