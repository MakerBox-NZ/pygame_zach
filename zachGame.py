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

            #gravity variables
            self.collide_delta = 0
            self.jump_delta = 6

            self.score = 0 #set score
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

        def update(self, enemy_list, platform_list):
            #update sprite position
            currentX = self.rect.x
            nextX = currentX + self.momentumX
            self.rect.x = nextX

            currentY = self.rect.y
            nextY = currentY + self.momentumY
            self.rect.y = nextY

            #gravity
            if self.collide_delta < 6 and self.jump_delta < 6:
                self.jump_delta = 6*2
                self.momentumY -=33 #how high to jump

                self.collide_delta +=6
                self.jump_delta += 6

                #colisions
            enemy_hit_list = pygame.sprite.spritecollide(self, enemy_list, False)       
            for enemy in enemy_hit_list:
                self.score -= 1
                print(self.score)

            block_hit_list = pygame.sprite.spritecollide(self, platform_list, False)
            if self.momentumX > 0:
                 for block in block_hit_list:
                     self.rect.y = currentY
                     self.rect.x = currentX+9
                     self.momentumY = 0
                     self.collide_delta = 0 #stop jumping

            if self.momentumY > 0:
                 for block in block_hit_list:
                     self.rect.y = currentY
                     self.momentumY = 0
                     self.collide_delta = 0 #stop jumping

          

        def jump (self, platform_list):
             self.jump_delta = 0


        def gravity(self):
            self.momentumY += 2 #how fast player falls

            if self.rect.y > 360 and self.momentumY >= 0:
                self.momentumY = 0
                self.rect.y = screenY-20

class Platform(pygame.sprite.Sprite):
   #x location, y location, img width, img height, img file)
   def __init__(self,xloc,yloc,imgw, imgh, img):
       pygame.sprite.Sprite.__init__(self)
       self.image = pygame.Surface([imgw, imgh])
       self.image.convert_alpha()
       self.image.set_colorkey(alpha)
       self.blockpic = pygame.image.load(img).convert()
       self.rect = self.image.get_rect()
       self.rect.y = yloc
       self.rect.x = xloc

       #paint image into blocks
       self.image.blit(self.blockpic,(0,0),(0,0,imgw,imgh))


   def level1():
       #create level 1
       platform_list = pygame.sprite.Group()
       block = Platform(260, 270, 58, 51,os.path.join('images','crate0.png'))
       platform_list.add(block) #after each block
       block = Platform(0, 320, 94, 49,os.path.join('images','ground_grass.png'))
       platform_list.add(block) #after each block
       block = Platform(94, 320, 94, 49,os.path.join('images','ground_grass.png'))
       platform_list.add(block) #after each block
       block = Platform(188, 320, 94, 49,os.path.join('images','ground_grass.png'))
       platform_list.add(block) #after each block
       block = Platform(282, 320, 70, 49,os.path.join('images','ground_grass.png'))
       platform_list.add(block) #after each block

       return platform_list #at end of function level1

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

platform_list = Platform.level1() #set stage to level 1

player = Player() #spawn player on screen 
player.rect.x = 0
player.rect.y = 120
movingsprites = pygame.sprite.Group()
movingsprites.add(player)
movesteps = 10 #how fast to move

#enemy code
enemy = Enemy(100,270, 'enemy.png') #spawn enemy
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
                player.jump(platform_list)
                print('jump')
            if event.key == ord('s') or event.key == pygame.K_DOWN:
                print('duck')
                
    screen.blit(backdrop, backdropRect)
    platform_list.draw(screen) #draw platforms on screen
    player.gravity() #check gravity
    player.update(enemy_list, platform_list) #update player position
    movingsprites.draw(screen) #draw player

    enemy_list.draw(screen) #refresh enemies
    enemy.move() #move enemy sprite
    
    pygame.display.flip()
    clock.tick(fps)
    
    
                

