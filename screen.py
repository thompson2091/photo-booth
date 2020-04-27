import pygame as pg
from pygame.locals import *
import time
import PhotoBooth
import os

# init photo booth
booth 	= PhotoBooth.PhotoBooth()

pg.display.init()
pg.display.set_caption("Lillian's Birthday Photo Booth!")
pg.font.init()
h 				= 2560#1366#1280#640
w 				= 1600#1024#720#480
red 			= (200,0,0)
green 			= (0,200,0)
bright_red 		= (255,0,0)
bright_green 	= (0,255,0)
white 			= (255,255,255)
black 			= (0,0,0)
blue 			= (135,206,250)
pink 			= (255,192,203)
hot_pink 		= (255,20,147)
hot_blue 		= (0,0,255)

_display = pg.display.set_mode((h,w))
_display.fill(pg.Color(0,0,0))


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def prince(booth):
    if os.path.exists('wav/fart.wav'):
        os.system('%s %s' % ('afplay','wav/fart.wav'))

def princess(booth):
    booth.start(False)

def Buttonify(Picture, coords, surface):
    image = pg.image.load(Picture)
    imagerect = image.get_rect()
    imagerect.topright = coords
    surface.blit(image,imagerect)
    return (image,imagerect)

# main message
_display.fill(white)

largeText = pg.font.Font('freesansbold.ttf',30)
TextSurf, TextRect = text_objects("Press the Button to Begin", largeText)
TextRect.center = ((w/1.5),(h/7))
_display.blit(TextSurf, TextRect)


largeText = pg.font.Font('freesansbold.ttf',30)
TextSurf, TextRect = text_objects("Pictures Available at Printer", largeText)
TextRect.center = ((w/1.5),(h/2.5))
_display.blit(TextSurf, TextRect)


Image 	= Buttonify('button.png',(1200,500),_display)

while True:
    playing     = False
    for i in pg.event.get():

    	if i.type == pg.KEYDOWN:
            if (i.key == pg.K_ESCAPE) or (i.type == pg.QUIT):
            	pg.quit()

        if i.type == QUIT:
            pg.quit()

        mouse = pg.mouse.get_pos()
        click = pg.mouse.get_pressed()

        if 1200+500 > mouse[0] > 500 and 1200+500 > mouse[1] > 500:
            if (click[0] == 1 or i.type == pg.MOUSEBUTTONDOWN) and not playing:
                playing     = True

        # lets play
        if playing:
            princess(booth)
            playing     = False


        pg.display.update()
        time.sleep(.05)

    pg.display.flip()  
