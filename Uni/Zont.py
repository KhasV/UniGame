import pygame

zont_pic = pygame.image.load('bigzontik1.png')


class Zont():
    def __init__(self, object):
        self.image = zont_pic
        self.rect = self.image.get_rect(center=(object.rect.x, 0))
        self.rect.x = object.rect.x - 50
        self.rect.y = object.rect.y - 100
        self.mask = pygame.mask.from_surface(self.image)

    def update(self, object):
        self.rect.x = object.rect.x - 0
        self.rect.y = object.rect.y - 50