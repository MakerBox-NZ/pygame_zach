#!/usr/bin/env python3
# by zackles007
# thanks to Jess Weichler
# It's no Call of Duty, but it's somthing.
import pygame #load pygame keywords
import sys #let python use your file system
import os #help python identify your OS
import pygame.freetype #load fonts

'''OBJECTS'''
#put classes & functions here

def stats(score):
    #display text,1,color(rgb)
    text_score = myfont.render("Score: "+str(score), 1, (0,5,151))
    screen.blit(text_score, (4, 4))

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
            self.damage = 0 #player is hit
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

        def update(self, enemy_list, platform_list, crate_list, loot_list):
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
                self.momentumY -=29 #how high to jump

                self.collide_delta +=6
                self.jump_delta += 6

                #colisions
            enemy_hit_list = pygame.sprite.spritecollide(self, enemy_list, False)       
            '''for enemy in enemy_hit_list:
                self.score -= 1
                print(self.score)'''

            if self.damage == 0:
                 for enemy in enemy_hit_list:
                     if not self.rect.contains(enemy):
                         self.damage = self.rect.colliderect(enemy)
                         print(self.score)

            if self.damage == 1:
                idx = self.rect.collidelist(enemy_hit_list)
                if idx == -1:
                    self.damage = 0 #set damage back to 0
                    self.score -= 1 #subtract 1 hp

            loot_hit_list = pygame.sprite.spritecollide(self, loot_list, False)       
            for loot in loot_hit_list:
                self.score += 1
                loot_list.remove(loot)

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

            if self.rect.y > screenY and self.momentumY >= 0:
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
       #the grass
       block = Platform(0, 680, 240, 62,os.path.join('images','ground_grass.png'))
       platform_list.add(block) #after each block
      # block = Platform(94, 680, 119, 62,os.path.join('images','ground_grass.png'))
       #platform_list.add(block) #after each block
       block = Platform(188, 680, 240, 62,os.path.join('images','ground_grass.png'))
       platform_list.add(block) #after each block
       #block = Platform(282, 680, 119, 62,os.path.join('images','ground_grass.png'))
       #platform_list.add(block) #after each block
       block = Platform(350, 680, 240, 62,os.path.join('images','ground_grass.png'))
       platform_list.add(block) #after each block
       #block = Platform(420, 680, 119, 62,os.path.join('images','ground_grass.png'))
       platform_list.add(block) #after each block
       #block = Platform(480, 680, 119, 62,os.path.join('images','ground_grass.png'))
       platform_list.add(block) #after each block
       block = Platform(540, 680, 240, 62,os.path.join('images','ground_grass.png'))
       #platform_list.add(block) #after each block
       #block = Platform(600, 680, 119, 62,os.path.join('images','ground_grass.png'))
       platform_list.add(block) #after each block
       block = Platform(660, 680, 240, 62,os.path.join('images','ground_grass.png'))
       #platform_list.add(block) #after each block
       #block = Platform(720, 680, 119, 62,os.path.join('images','ground_grass.png'))
       platform_list.add(block) #after each block
       block = Platform(780, 680, 120, 62,os.path.join('images','ground_grass.png'))
       platform_list.add(block) #after each block
       #block = Platform(840, 680, 119, 62,os.path.join('images','ground_grass.png'))
       #platform_list.add(block) #after each block
       block = Platform(900, 680, 120, 62,os.path.join('images','ground_grass_rightslope.png'))
       platform_list.add(block) #after each block
       #the platforms
       block = Platform(1130, 530, 152, 300,os.path.join('images','platform_os_1.png'))
       platform_list.add(block) #after each block
       block = Platform(1350, 400, 152, 400,os.path.join('images','platform_os_1.png'))
       platform_list.add(block) #after each block

       return platform_list #at end of function level1

   def loot1():
       #where loot placement goes 
       loot_list = pygame.sprite.Group()
       loot = Platform(200, 600, 23, 24,os.path.join('images','loot.png'))
       loot_list.add(loot)
       loot = Platform(360, 600, 23, 24,os.path.join('images','loot.png'))
       loot_list.add(loot)
       loot = Platform(600, 600, 23, 24,os.path.join('images','loot.png'))
       loot_list.add(loot)
       return loot_list
                       
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

def crate_list():
       #solid crate list
       crate_list = pygame.sprite.Group()
       crate = Platform(260, 630, 58, 51,os.path.join('images','crate0.png'))
       crate_list.add(crate) #after each block

       return crate_list
            
'''SETUP'''
#code runs once
screenX = 960 #screen width
screenY = 720 #screen height
alpha = (0,0,0)
black = (1,1,1)
white = (255, 255, 255)

fps = 40 #frame rate
afps = 4 #animation cycles
clock = pygame.time.Clock()
pygame.init()
pygame.font.init() #start freetype

font_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "fonts",
"amazdoom.ttf")
font_size = 64
myfont = pygame.font.Font(font_path, font_size)

main = True

screen = pygame.display.set_mode([screenX,screenY])
backdrop = pygame.image.load(os.path.join('images','stage.png')).convert()
backdropRect = screen.get_rect()

platform_list = Platform.level1() #set stage to level 1
#crate_list = crate_list()
loot_list = Platform.loot1()

player = Player() #spawn player on screen 
player.rect.x = 0
player.rect.y = 300
movingsprites = pygame.sprite.Group()
movingsprites.add(player)
movesteps = 10 #how fast to move

forwardX = 400 #when to scroll
backwardX = 250 #when to scroll

#enemy code
enemy = Enemy(400, 620, 'enemy.png') #spawn enemy
enemy_list = pygame.sprite.Group() #create enemy group
enemy_list.add(enemy)  #add enemy to group

#loot code
'''loot = Loot(200, 600, 'loot.png') #spawn loot
loot_list = pygame.sprite.Group() #create loot group
loot_list.add(loot) #add loot to group'''

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

    #scroll world forward
    if player.rect.x >= forwardX:
        scroll = player.rect.x - forwardX
        player.rect.x = forwardX
        for platform in platform_list:
            platform.rect.x -= scroll
        for enemy in enemy_list:
            enemy.rect.x -= scroll
        for loot in loot_list:
            loot.rect.x -= scroll

    #scroll world backward
    if player.rect.x <= backwardX:
        scroll = backwardX - player.rect.x
        player.rect.x = backwardX
        for platform in platform_list:
            platform.rect.x += scroll
        for enemy in enemy_list:
            enemy.rect.x += scroll
        for loot in loot_list:
            loot.rect.x += scroll
                
    screen.blit(backdrop, backdropRect)
    platform_list.draw(screen) #draw platforms on screen
    #crate_list.draw(screen) #draw crates on screen
    player.gravity() #check gravity
    player.update(enemy_list, platform_list, crate_list, loot_list) #update player position
    movingsprites.draw(screen) #draw player

    enemy_list.draw(screen) #refresh enemies
    enemy.move() #move enemy sprite
    loot_list.draw(screen)

    stats(player.score) #draw text
    
    pygame.display.flip()
    clock.tick(fps)
    
    
                

