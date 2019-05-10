import pygame
import math

sun = pygame.image.load('sun.png')


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x1, y1, color, speed, x2, y2, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect(center=(x1, 0))
        self.rect.x = x1 #где появляется\сдвиг
        self.rect.y = y1
        self.x2 = x2 #куда летит
        self.y2 = y2
        self.radius = 9
        self.color = color
        self.speed = speed
        self.sina = (self.rect.y - self.y2) / math.sqrt(
            pow(self.rect.y - self.y2, 2) + pow(self.x2 - self.rect.x, 2))
        self.cosa = (self.x2 - self.rect.x) / math.sqrt(
            pow(self.rect.y - self.y2, 2) + pow(self.x2 - self.rect.x, 2))
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        if 0 < self.rect.x < 1280 and 0 < self.rect.y < 720:
            self.rect.x += self.cosa * self.speed
            self.rect.y -= self.sina * self.speed

        else:
            self.kill()