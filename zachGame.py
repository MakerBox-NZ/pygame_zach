#!/usr/bin/env python3
# by zackles007
# thanks to Jess Weichler
import pygame #load pygame keywords
import sys #let python use your file system
import os #help python identify your OS

'''OBJECTS'''
#put classes & functions here 

class Player(pygame.sprite.Sprite):
        #spawn a player
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.images = [ ]
            img = pygame.image.load(os.path.join('images','hero.png')).convert()
            self.images.append(img)
            self.image = self.images[0]
            self.rect = self.image.get_rect()
            self.image.convert_alpha() #optimise for alpha
            self.image.set_colorkey(alpha) #set alpha
            
 
'''SETUP'''
#code runs once
screenX = 480 #screen width
screenY = 360 #screen height
alpha = (0,0,0)
black = (1,1,1)
white = (255, 255, 255)

fps = 40 #frame rate
afps = 4 #animation cycles
clock = pygame.time.Clock()
pygame.init()

main = True

screen = pygame.display.set_mode([screenX,screenY])
backdrop = pygame.image.load(os.path.join('images','stage.png')).convert()
backdropRect = screen.get_rect()

player = Player() #spawn player on screen 
player.rect.x = 0
player.rect.y = 0
movingsprites = pygame.sprite.Group()
movingsprites.add(player)


'''MAIN LOOP''' 
#code runs many times 

while main == True:
    for event in pygame.event.get():
        if event.type == pygame.KEYUP:
            if event.key == ord('q'):
                pygame.quit()
                sys.exit()
                main = False

            if event.key == ord('a'):
                print('left stop')
            if event.key == ord('d'):
                print('right stop')
            if event.key == ord('w'):
                print('up stop')
            if event.key == ord('s'):
                print('down stop')
        
        if event.type == pygame.KEYDOWN:
            if event.key == ord('a'):
                print('left')
            if event.key == ord('d'):
                print('right')
            if event.key == ord('w'):
                print('up')
            if event.key == ord('s'):
                print('down')
                
    screen.blit(backdrop, backdropRect)
    movingsprites.draw(screen) #draw player
    pygame.display.flip()
    clock.tick(fps)
    
    
                

