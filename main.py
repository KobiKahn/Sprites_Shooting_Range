import pygame, sys
import random
pygame.init()

clock = pygame.time.Clock()

myfont = pygame.font.SysFont('ccoverbyteoffregular.otf', 100)
moneyfont = pygame.font.SysFont('ccoverbyteoffregular.otf', 40)

life = 3
score = 0

shop_open = False

currency = 0



###### GAME WORKING

class Crosshair(pygame.sprite.Sprite):

    def __init__(self, picture_path):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()


    def shoot_target(self):
        global score
        global currency

        score += 1
        currency += round((new_target.vel)/4)
        new_target.reset_target()

    def shoot_enemy(self):
        global currency
        global life

        life -= 1
        currency = round(currency/2)
        enemy.reset_target()
        new_target.reset_target()

    def update(self):
        self.rect.center = pygame.mouse.get_pos()



class Target(pygame.sprite.Sprite):

    def __init__(self, picture_path, pos_x, pos_y, screen_h, vel):
        super().__init__()
        self.screen_h = screen_h
        self.image = pygame.image.load(picture_path)
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]
        self.vel = vel


    def move(self):
        self.rect.x += self.vel

    def reset_target(self):
        global enemy_check

        toss = random.randint(0,1)
        enemy_counter = random.randint(0, 10)

        if toss == 0:
            self.vel += .5

        if enemy_counter == 4:
            enemy_check = True

        else:
            enemy_check = False
            self.rect.x = -30
            self.rect.y = random.randrange(20, self.screen_h - 50)




class Enemy(pygame.sprite.Sprite):
    def __init__(self, picture_path, screen_h):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = [0, random.randrange(0, screen_h - 10)]
        self.screen_h = screen_h
        self.vel = new_target.vel


    def move(self):

        self.vel = new_target.vel
        self.rect.x += self.vel

    def reset_target(self):
        self.rect.x = -30
        self.rect.y = random.randrange(20, self.screen_h - 50)





####### TITLE SCREEN AND BUTTONS

class s_Button(pygame.sprite.Sprite):
    def __init__(self, picture_path, pos_x, pos_y):
        self.pos_x = pos_x
        super().__init__()
        self.image = pygame.image.load(picture_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]

    def move(self):
        self.rect.x = 10000
    def back(self):
        self.rect.x = 400



class shop_Button(pygame.sprite.Sprite):
    def __init__(self, picture_path, pos_x, pos_y):
        self.pos_x = pos_x
        super().__init__()
        self.image = pygame.image.load(picture_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]
    def move(self):
        self.rect.x = 10000
    def back(self):
        self.rect.x = 400


class back_Button(pygame.sprite.Sprite):
    def __init__(self, picture_path, pos_x, pos_y):
        self.pos_x = pos_x
        super().__init__()
        self.image = pygame.image.load(picture_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]

    def move(self):
        self.rect.x = 100000
    def back(self):
        self.rect.x = 50


###SHOP METHODS AND UPGRADES

class crosshair_big_button(pygame.sprite.Sprite):
    def __init__(self, picture_path, pos_x, pos_y):
        super().__init__()
        self.pos_x = pos_x
        self.img = pygame.image.load(picture_path).convert_alpha()
        self.img = pygame.transform.scale(self.img, (100, 100))
        self.rect = self.img.get_rect()
        self.rect.center = [pos_x, pos_y]

    def when_clicked(self):
        Crosshair.image = pygame.transform.scale(Crosshair.image, (60, 60))

    def move(self):
        self.rect.x = 100000

    def back(self):
        self.rect.x = self.pos_x





#GAME_SCREEN
screen_w = 800
screen_h = 400
screen = pygame.display.set_mode((screen_w,screen_h))

pygame.display.set_caption('Shooting Game')

background = pygame.image.load('BG.png')
pygame.mouse.set_visible(False)


#CROSSHAIR
crosshair = Crosshair('Crosshair.png')
crosshair_group = pygame.sprite.Group()
crosshair_group.add(crosshair)


# TARGET
target_group = pygame.sprite.Group()
new_target = Target('Target.png', 0, random.randrange(0, screen_h - 10), screen_h, 5)
target_group.add(new_target)




# ENEMY
enemy_group = pygame.sprite.Group()
enemy = Enemy('Enemy_target.png', screen_h)
enemy_group.add(enemy)

enemy_check = False

#HEART
heart1 = pygame.image.load('heart1.png')
heart2 = pygame.image.load('heart2.png')
heart3 = pygame.image.load('heart3.png')





#### TITLE SCREEN

# Start Button

start_img = 'play_button.png'
start_button = s_Button(start_img, 400, 100)
start_group = pygame.sprite.Group()
start_group.add(start_button)
start = False


# SHOP BUTTON

shop_img = 'shop_button.png'
shop_button = shop_Button(shop_img, 400, 300)
shop_group = pygame.sprite.Group()
shop_group.add(shop_button)

#### BACK FROM SHOP BUTTON

back_img = 'Back_button.png'
back_button = back_Button(back_img, 50, 50)
back_group = pygame.sprite.Group()
back_group.add(back_button)


###### CURRENCY

bullet_img = 'bullet_money.png'
bullet = pygame.image.load(bullet_img).convert_alpha()
bullet = pygame.transform.scale(bullet, (80,80))



########## SHOP IMAGES AND BUTTONS
big_upgrade_img = 'Big_Crosshair_img.png'

crosshair_big_upgrade = crosshair_big_button(big_upgrade_img, 200, 100)
crosshair_big_group = pygame.sprite.Group()
crosshair_big_group.add(crosshair_big_upgrade)

### GUNSHOT

gunshot = pygame.mixer.Sound('GUNSHOT.mp3')

while True:
    pos = pygame.mouse.get_pos()
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:

            gunshot.play()

            ############ COLLISION WITH TARGETS
            if start:
                if pygame.sprite.spritecollide(crosshair, target_group, False):
                    print('HIT_TARGET')
                    crosshair.shoot_target()

                elif pygame.sprite.spritecollide(crosshair, enemy_group, False):
                    print('HIT_ENEMY')
                    crosshair.shoot_enemy()

############ COLLISION WITH MENU BUTTONS

            if start == False:
                if start_button.rect.collidepoint(pos):
                    start_button.move()
                    shop_button.move()
                    start = True
                    shop_open = False
                    life = 3

                elif shop_button.rect.collidepoint(pos):
                    shop_open = True
                    start_button.move()
                    shop_button.move()
                    back_button.back()

                elif back_button.rect.collidepoint(pos):
                    shop_open = False
                    back_button.move()
                    shop_button.back()
                    start_button.back()



    ### SET SCORE AND CURRENCY

    score_text = myfont.render(f'{score}', True, (0, 0, 0))

    currency_text = moneyfont.render(f'{currency}', True, (255, 215, 0))


    screen.blit(background, (0,0))


    ##### RESET HOME SCREEN

    if start == False:

        new_target.vel = 5
        score = 0

        ############ CHECK IF START IS OPEN OR NOT

        if shop_open == False:
            start_button.back()
            shop_button.back()
            start_group.draw(screen)
            shop_group.draw(screen)


        if shop_open == True:
            back_group.draw(screen)




    elif start:

        ############## RESET TARGET IF ITS OFF THE MAP
        if new_target.rect.x > 825:
            life -= 1
            enemy.reset_target()
            new_target.reset_target()

        elif enemy.rect.x > 825:
            enemy.reset_target()
            new_target.reset_target()

        ####### SHOWS SCORE
        screen.blit(score_text, (350, 50))

        ############# DISPLAYS LIFE HEARTS
        if life == 3:
            screen.blit(heart1, (750, 0))
        if life >= 2:
            screen.blit(heart2, (710, 0))
        if life >= 1:
            screen.blit(heart3, (680, 0))

        ############# STOPS GAME IF LIFE IS DONE
        if life < 1:
            start = False


        ####### DECIDE WHETHER TO MOVE ENEMY OR PLAYER

        if enemy_check:
            enemy.move()
            enemy_group.draw(screen)

        else:
            new_target.move()
            target_group.draw(screen)



    ##### MONEY
    screen.blit(bullet, (580, -10))
    screen.blit(currency_text, (570, 5))



    #### CROSSHAIR
    crosshair_group.draw(screen)
    crosshair_group.update()

    pygame.display.flip()

    clock.tick(60)




