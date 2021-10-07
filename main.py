import pygame, sys
import random
pygame.init()
clock = pygame.time.Clock()

myfont = pygame.font.SysFont('ccoverbyteoffregular.otf', 100)

life = 3
score = 0

class Crosshair(pygame.sprite.Sprite):

    def __init__(self, picture_path):
        global score
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.rect = self.image.get_rect()
        self.gunshot = pygame.mixer.Sound('GUNSHOT.mp3')
    def shoot(self):
        global score
        self.gunshot.play()
        if pygame.sprite.spritecollide(crosshair, target_group, False):
            score += 1
            new_target.reset_target()

    def update(self):
        self.rect.center = pygame.mouse.get_pos()


class Target(pygame.sprite.Sprite):

    def __init__(self, picture_path, pos_x, pos_y, screen_h, vel):
        super().__init__()
        self.screen_h = screen_h
        self.image = pygame.image.load(picture_path)
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]
        self.vel = vel
    def move(self):
        self.rect.x += self.vel
    def reset_target(self):
        toss = random.randint(0,1)
        if toss == 0:
            self.vel += .5
        self.rect.x = -20
        self.rect.y = random.randrange(20, self.screen_h - 50)

class s_Button(pygame.sprite.Sprite):
    def __init__(self, picture_path, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]
    def move(self):
        self.pos_x = 10000
    def back(self):
        self.pos_x = 400

class shop_Button(pygame.sprite.Sprite):
    def __init__(self, picture_path, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]
    def move(self):
        self.pos_x = 1000
    def back(self):
        self.pos_x = 400




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
target_group.add(new_target)

#HEART
heart1 = pygame.image.load('heart1.png')
heart2 = pygame.image.load('heart2.png')
heart3 = pygame.image.load('heart3.png')

#HUD
gameover = pygame.image.load('gameover.png')

#### TITLE SCREEN

# Start Button

start_img = 'play.png'
start_button = s_Button(start_img, 400, 100)
start_group = pygame.sprite.Group()
start_group.add(start_button)
start = False


# SHOP BUTTON

shop_img = 'shop.png'
shop_button = shop_Button(shop_img, 400, 300)
shop_group = pygame.sprite.Group()
shop_group.add(shop_button)




while True:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            crosshair.shoot()
        if start == False and event.type == pygame.MOUSEBUTTONDOWN and pygame.sprite.spritecollide(crosshair, start_group, False):
            start_button.move()
            shop_button.move()
            start = True
            life = 3

    score_text = myfont.render(f'{score}', True, (0, 0, 0))

    if new_target.rect.x > 825:
        life -= 1
        new_target.reset_target()




## DISPLAY

    pygame.display.flip()


    screen.blit(background, (0,0))

    if start == False:
        new_target.vel = 5
        score = 0
        start_button.back()
        shop_button.back()
        start_group.draw(screen)
        shop_group.draw(screen)

    if life < 1:
        screen.blit(gameover, (250, 100))
        start = False

    if life == 3:
        screen.blit(heart1, (750, 0))
    if life >= 2:
        screen.blit(heart2, (710, 0))
    if life >= 1:
        screen.blit(heart3, (680, 0))


    if start == True:
        screen.blit(score_text, (350, 50))
        new_target.move()
        target_group.draw(screen)
    crosshair_group.draw(screen)
    crosshair_group.update()



    clock.tick(60)




