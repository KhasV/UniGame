import pygame
import Bullets
from random import randrange


cloudPic = [pygame.image.load('cloud_0.png'),
            pygame.image.load('cloud_0.png'), pygame.image.load('cloud_1.png'),
            pygame.image.load('cloud_2.png'), pygame.image.load('cloud_3.png'),
            pygame.image.load('cloud_3.png')]

maxCloud = 0
currentCloud = 0


class Cloud(pygame.sprite.Sprite):

    animCount = 0
    cloud_bullets = pygame.sprite.Group()
    cd = 0

    def __init__(self, x, y, type_move):
        pygame.sprite.Sprite.__init__(self)
        self.image = cloudPic[0]
        self.rect = self.image.get_rect(center=(x, 0))
        self.radius = 65
        self.rect.x = x
        self.rect.y = y
        self.type_move = type_move
        self.speed = randrange(3, 10)
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        global currentCloud

        if self.cd == 0:
            self.cd = 80
            self.cloud_bullets.add(Bullets.Bullet((self.rect.x + 150 // 2), (self.rect.y + 150 // 2),
                            (255, 255, 0), randrange(2, 9), (self.rect.x + 150 // 2), (self.rect.y + 300), 'drop.png'))
        self.cd -= 1
        if self.cd < 0:
            self.cd = 0

        if self.rect.x > 1280 or self.rect.x < 0 - 200:
            currentCloud -= 1
            self.kill()

        if self.type_move == 0:
            self.rect.x += self.speed

        if self.type_move == 1:
            self.rect.x -= self.speed

        self.picture()

    def picture(self):
        if self.animCount + 1 >= 30:
            self.animCount = 0

        self.image = cloudPic[self.animCount // 5]
        self.animCount += 1
