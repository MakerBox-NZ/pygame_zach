#!/usr/bin/env python3
# by zackles007
# thanks to Jess Weichler

import pygame #load pygame keywords
import sys #let python use your file system
import os #help python identify your OS

'''OBJECTS'''
#put classes & functions here



'''SETUP'''
#code runs once
screenX = 960 #screen width
screenY = 720 #screen height

fps = 40 #frame rate
afps = 4 #animation cycles
clock = pygame.time.Clock()
pygame.init()

main = True

screen = pygame.display.set_mode([screenX,screenY])
backdrop = pygame.image.load(os.path.join('images','stage.png')).convert()
backdropRect = screen.get_rect()

'''MAIN LOOP'''
#code runs many times

while main == True:
    for event in pygame.event.get():
        if event.type == pygame.KEYUP:
            if event.key == ord('q'):
                pygame.quit()
                sys.exit()
                main = False
    screen.blit(backdrop, backdropRect)

    pygame.display.flip()
    clock.tick(fps)
    
    
                

