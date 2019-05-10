import pygame

sdgs = [pygame.image.load('sdg1.png').convert_alpha(),
        pygame.image.load('sdg2.png').convert_alpha(), pygame.image.load('sdg3.png').convert_alpha(),
        pygame.image.load('sdg4.png').convert_alpha(), pygame.image.load('sdg5.png').convert_alpha(),
        pygame.image.load('sdg6.png').convert_alpha(), pygame.image.load('sdg7.png').convert_alpha(),
        pygame.image.load('sdg8.png').convert_alpha(), pygame.image.load('sdg9.png').convert_alpha(),
        pygame.image.load('sdg10.png').convert_alpha(), pygame.image.load('sdg11.png').convert_alpha(),
        pygame.image.load('sdg12.png').convert_alpha(), pygame.image.load('sdg13.png').convert_alpha(),
        pygame.image.load('sdg14.png').convert_alpha(), pygame.image.load('sdg15.png').convert_alpha(),
        pygame.image.load('sdg16.png').convert_alpha(), pygame.image.load('sdg17.png').convert_alpha()]


class SDGs(pygame.sprite.Sprite):

    speed = 5

    def __init__(self, x, sdg_type):
        self.sdg_type = sdg_type
        self.rect = self.image.get_rect(center=(x, 0))
        self.rect.x = x
        self.image = sdgs[sdg_type]

    def update(self):
        if self.rect.y > 720:
            self.kill()

        self.rect.y += self.speed
