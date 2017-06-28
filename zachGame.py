#!/usr/bin/env python3
# by zackles007
# thanks to Jess Weichler
# It's no Call of Duty, but it's somthing.
import pygame #load pygame keywords
import sys #let python use your file system
import os #help python identify your OS

'''OBJECTS'''
#put classes & functions here 

class Player(pygame.sprite.Sprite):
        #spawn a player
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.momentumX = 0 #move along X
            self.momentumY = 0 #move along Y
            self.images = [ ]
            img = pygame.image.load(os.path.join('images','hero.png')).convert()
            self.images.append(img)
            self.image = self.images[0]
            self.rect = self.image.get_rect()
            self.image.convert_alpha() #optimise for alpha
            self.image.set_colorkey(alpha) #set alpha
        def control(self, x, y):
            #control player movement
            self.momentumX += x
            self.momentumY += y

        def update(self):
            #update sprite position
            currentX = self.rect.x
            nextX = currentX + self.momentumX
            self.rect.x = nextX

            currentY = self.rect.y
            nextY = currentY + self.momentumY
            self.rect.y = nextY

class Enemy(pygame.sprite.Sprite):
    #spawn an enemy
    def __init__(self,x,y,img): 
       pygame.sprite.Sprite.__init__(self)
       self.image = pygame.image.load(os.path.join('images', img))
       self.image.convert_alpha()
       self.image.set_colorkey(alpha)
       self.rect = self.image.get_rect()
       self.rect.x = x
       self.rect.y = y
       self.counter = 0 #counter variable
    def move(self):
        #enemy movement
        if self.counter >= 0 and self.counter <= 30:
            self.rect.x += 2
        elif self.counter >= 30 and self.counter <=60:
            self.rect.x -= 2
        else:
            self.counter = 0
            print('reset')

        self.counter += 1
            
'''SETUP'''
#code runs once
screenX = 480 #screen width
screenY = 360 #screen height
alpha = (0,255,0)
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
player.rect.y = 120
movingsprites = pygame.sprite.Group()
movingsprites.add(player)
movesteps = 10 #how fast to move

#enemy code
enemy = Enemy(100,50, 'enemy.png') #apawn enemy
enemy_list = pygame.sprite.Group() #create enemy group
enemy_list.add(enemy)  #add enemy to group

'''MAIN LOOP''' 
#code runs many times 

while main == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                main = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_BACKSPACE:
                pygame.quit()
                sys.exit()
                main = False

        

            if event.key == ord('a') or event.key == pygame.K_LEFT:
                print('left stop')
                player.control(movesteps, 0)
            if event.key == ord('d') or event.key == pygame.K_RIGHT:
                print('right stop')
                player.control(-movesteps, 0)
            if event.key == ord('w') or event.key == pygame.K_UP:
                print('jump stop')
            if event.key == ord('s') or event.key == pygame.K_DOWN:
                print('duck stop')
        
        if event.type == pygame.KEYDOWN:
            if event.key == ord('a') or event.key == pygame.K_LEFT:
                print('left')
                player.control(-movesteps, 0)
            if event.key == ord('d') or event.key == pygame.K_RIGHT: 
                print('right')
                player.control(movesteps, 0)
            if event.key == ord('w') or event.key == pygame.K_UP:
                print('jump')
            if event.key == ord('s') or event.key == pygame.K_DOWN:
                print('duck')
                
    screen.blit(backdrop, backdropRect)
    player.update() #update player position
    movingsprites.draw(screen) #draw player

    enemy_list.draw(screen) #refresh enemies
    enemy.move() #move enemy sprite
    
    pygame.display.flip()
    clock.tick(fps)
    
    
                

