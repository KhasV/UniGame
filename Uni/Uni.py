import pygame
import Bullets

walkRight = [pygame.image.load('right.png'),
             pygame.image.load('right.png'), pygame.image.load('right.png'),
             pygame.image.load('right.png'), pygame.image.load('right.png'),
             pygame.image.load('right.png')]

walkLeft = [pygame.image.load('left.png'),
            pygame.image.load('left.png'), pygame.image.load('left.png'),
            pygame.image.load('left.png'), pygame.image.load('left.png'),
            pygame.image.load('left.png')]

playerStand = pygame.image.load('stand.png')

bullet_count = 100
time = 0
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 40)

text_bullets = myfont.render(f' : {bullet_count}', True, (242, 167, 68))


POWERTIME = 10000


class Uni(pygame.sprite.Sprite):

    sun_bullets = pygame.sprite.Group()
    speed = 10
    isJump = False
    jumpCount = 10
    left = False
    right = False
    animCount = 0
    cd = 5
    hp = 5
    record = 0

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = playerStand
        self.rect = self.image.get_rect(center=(50, 0))
        self.radius = 57
        self.rect.x = x
        self.rect.y = y
        self.start_x = x
        self.start_y = y
        self.power = 0
        self.power_time = pygame.time.get_ticks()
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        global bullet_count
        global text_bullets
        global time

        if self.power >= 1 and pygame.time.get_ticks() - self.power_time > POWERTIME:
            self.power -= self.power
            self.power_time = pygame.time.get_ticks()

        if self.power >= 1:
            time = 10 - ((pygame.time.get_ticks() + 100 - self.power_time) // 1000)

        keys = pygame.key.get_pressed()
        pos = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if click[0] == 1 and self.cd == 0:
            self.cd = 7
            if bullet_count > 0:
                self.sun_bullets.add(Bullets.Bullet((self.rect.x + 170 // 2), (self.rect.y + 210 // 2),
                                                       (255, 255, 0), 20, pos[0], pos[1], 'sun.png'))
                bullet_count -= 1
                text_bullets = myfont.render(f' : {bullet_count}', True, (242, 167, 68))

        self.cd -= 1
        if self.cd < 0:
            self.cd = 0

        if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and self.rect.x > -100:
            self.rect.x -= self.speed
            self.left = True
            self.right = False
        elif (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and self.rect.x < 1280 - 200 + 100:
            self.rect.x += self.speed
            self.right = True
            self.left = False
        else:
            self.left = False
            self.right = False
            self.animCount = 0
        if not self.isJump:
            if keys[pygame.K_UP] or keys[pygame.K_w] or keys[pygame.K_SPACE]:
                self.isJump = True
        else:
            if self.jumpCount >= - 10:
                if self.jumpCount < 0:
                    self.rect.y += (self.jumpCount ** 2) // 2
                else:
                    self.rect.y -= (self.jumpCount ** 2) // 2
                self.jumpCount -= 1
            else:
                self.isJump = False
                self.jumpCount = 10
        self.picture()

    def picture(self):
        if self.animCount + 1 >= 30:
            self.animCount = 0

        if self.left:
            self.image = walkLeft[self.animCount // 5]
            self.animCount += 1
        elif self.right:
            self.image = walkRight[self.animCount // 5]
            self.animCount += 1
        else:
            self.image = playerStand

    def powerup(self):
        self.power += 1
        self.power_time = pygame.time.get_ticks()
