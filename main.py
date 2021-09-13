import pygame, sys
import random
pygame.init()
clock = pygame.time.Clock()

class Crosshair(pygame.sprite.Sprite):
    def __init__(self, picture_path):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.rect = self.image.get_rect()
        self.gunshot = pygame.mixer.Sound('GUNSHOT.mp3')
    def shoot(self):
        self.gunshot.play()
        pygame.sprite.spritecollide(crosshair, target_group, True)

    def update(self):
        self.rect.center = pygame.mouse.get_pos()

class Target(pygame.sprite.Sprite):
    def __init__(self, picture_path, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]






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
for target in range(20):
    new_target = Target('Target.png', random.randrange(0, screen_w), random.randrange(0, screen_h))
    target_group.add(new_target)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            crosshair.shoot()



    pygame.display.flip()
    screen.blit(background, (0,0))
    target_group.draw(screen)
    crosshair_group.draw(screen)
    crosshair_group.update()
    clock.tick(60)




