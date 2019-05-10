import pygame
from random import randrange

powerup_img = [pygame.image.load('energy1.png'), pygame.image.load('shield.png'), pygame.image.load('blueheard.png')]


class Powerups(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.type = randrange(0, 3)
        self.image = powerup_img[self.type]
        self.rect = self.image.get_rect(center=(x, 0))
        self.rect.x = x
        self.rect.y = y
        self.radius = int(0.9 * (self.rect.centerx - self.rect.x))
        self.speed = 3
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > 720:
            self.kill()
        # pygame.draw.circle(self.image, (255, 0, 0), (self.rect.centerx - self.rect.x, 20), self.radius)