import pygame, sys
import random
pygame.init()
clock = pygame.time.Clock()

counter = 0
life = 3

class Crosshair(pygame.sprite.Sprite):
    global counter
    def __init__(self, picture_path):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.rect = self.image.get_rect()
        self.gunshot = pygame.mixer.Sound('GUNSHOT.mp3')
    def shoot(self):
        self.gunshot.play()
        if pygame.sprite.spritecollide(crosshair, target_group, False):
            new_target.reset_target()
    def update(self):
        self.rect.center = pygame.mouse.get_pos()


class Target(pygame.sprite.Sprite):
    def __init__(self, picture_path, pos_x, pos_y, screen_h):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]
    def move(self):

        self.rect.x += 5
    def reset_target(self):
        self.rect.x = -20
        self.rect.y = random.randrange(0, screen_h - 10)



#GAME_SCREEN
screen_w = 800
screen_h = 400
screen = pygame.display.set_mode((screen_w,screen_h))

background = pygame.image.load('BG.png')
pygame.mouse.set_visible(False)


#CROSSHAIR
crosshair = Crosshair('Crosshair.png')
crosshair_group = pygame.sprite.Group()
crosshair_group.add(crosshair)


# TARGET
target_group = pygame.sprite.Group()
new_target = Target('Target.png', 0, random.randrange(0, screen_h - 10), screen_h)
target_group.add(new_target)

#HEART
heart1 = pygame.image.load('heart1.png')
heart2 = pygame.image.load('heart2.png')
heart3 = pygame.image.load('heart3.png')

#HUD
gameover = pygame.image.load('gameover.png')
start_button = pygame.image.load('start.png')

start = False

while True:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            crosshair.shoot()
        if start == False and pygame.MOUSEBUTTONDOWN and



    if life == 0:
        print('GAME OVER')


    if new_target.rect.x > 825:
        life -= 1
        new_target.reset_target()



    pygame.display.flip()

    new_target.move()
    screen.blit(background, (0,0))
    if life == 3:
        screen.blit(heart1, (750, 0))
    if life >= 2:
        screen.blit(heart2, (710, 0))
    if life >= 1:
        screen.blit(heart3, (680, 0))
    if start == True:
        target_group.draw(screen)
        crosshair_group.draw(screen)
        crosshair_group.update()
    clock.tick(60)




