import pygame
import Uni
import Cloud
import Powerups
import InputBox
import random
import Zont
from pymongo import MongoClient
from random import randrange

pygame.init()

pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 40)
myfont1 = pygame.font.SysFont('Comic Sans MS', 50)
myfont2 = pygame.font.SysFont('Comic Sans MS', 70)
pygame.font.get_fonts()

icon = pygame.image.load('right.png')
pygame.display.set_icon(icon)

win = pygame.display.set_mode((1280, 720))

menu_pic = pygame.image.load('menu1.png').convert_alpha()
gameover_pic = pygame.image.load('game_over.png').convert_alpha()
bg = pygame.image.load('fon1.jpg').convert_alpha()
bul = pygame.image.load('bullet.png').convert_alpha()
sh = pygame.image.load('small_zontik.png').convert_alpha()
heard = pygame.image.load('heard.png').convert_alpha()
dest_heard = pygame.image.load('heard1.png').convert_alpha()
ent_name = [pygame.image.load('fon2.png'), pygame.image.load('fon2.png'),
            pygame.image.load('fon2.png'), pygame.image.load('fon2.png'), pygame.image.load('fon3.png'),
            pygame.image.load('fon3.png'), pygame.image.load('fon3.png'), pygame.image.load('fon3.png'),
            pygame.image.load('fon4.png'), pygame.image.load('fon4.png'), pygame.image.load('fon4.png'),
            pygame.image.load('fon4.png')]
gameovers = [pygame.image.load('game_over2.png'), pygame.image.load('game_over2.png'), pygame.image.load('game_over2.png'),
             pygame.image.load('game_over2.png'), pygame.image.load('game_over3.png'), pygame.image.load('game_over3.png'),
             pygame.image.load('game_over3.png'), pygame.image.load('game_over3.png'), pygame.image.load('game_over4.png'),
             pygame.image.load('game_over4.png'), pygame.image.load('game_over4.png'), pygame.image.load('game_over4.png'),
             pygame.image.load('game_over5.png'), pygame.image.load('game_over5.png'), pygame.image.load('game_over5.png'),
             pygame.image.load('game_over5.png')]
pygame.display.set_caption("UniGame")

run = True
esc = False
type_screen = 0

text_score = myfont.render(f'Score : {Uni.Uni.record}', True, (23, 89, 212))
text_level = myfont.render(f'LEVEL {15}', True, (0, 0, 0))
record1 = myfont1.render(f'1', True, (77, 58, 186))
record2 = myfont1.render(f'2', True, (77, 58, 186))
record3 = myfont1.render(f'3', True, (77, 58, 186))
record4 = myfont1.render(f'4', True, (77, 58, 186))
record5 = myfont1.render(f'5', True, (77, 58, 186))
record6 = myfont1.render(f'6', True, (77, 58, 186))
record7 = myfont1.render(f'7', True, (77, 58, 186))
record8 = myfont1.render(f'8', True, (77, 58, 186))
record9 = myfont1.render(f'9', True, (77, 58, 186))
record10 = myfont1.render(f'10', True, (77, 58, 186))
allrecords = [record1, record2, record3, record4, record5, record6, record7, record8, record9, record10]

clock = pygame.time.Clock()
cloudGroup = pygame.sprite.Group()
powGroup = pygame.sprite.Group()
cd = 0
mark = False
count = True

Cloud.maxCloud = 5

username = ""
docs = []
unirec = []

client = MongoClient()
db = client.uni_database
records = db.records

uni = Uni.Uni(50, 460)
zont = Zont.Zont(uni)

index = 0
index1 = 0

input_box1 = InputBox.InputBox(640 - 150, 360 - 20, 140, 50)

def user():
    global type_screen
    global username
    global index

    input_box1.update()

    if index == 11:
        index = 1
    else:
        index += 1
    win.blit(ent_name[index], (0, 0))

    input_box1.draw(win)

    pygame.display.flip()

    if InputBox.flag:
        type_screen = 1
        InputBox.flag = False

    username = InputBox.info


def new_game():
    global uni
    global text_score
    global cloudGroup
    global powGroup

    uni = Uni.Uni(50, 460)
    Uni.Uni.record = 0
    text_score = myfont.render(f'Score : {Uni.Uni.record}', True, (23, 89, 212))
    Uni.Uni.hp = 5
    Uni.bullet_count = 100
    Uni.text_bullets = myfont.render(f' : {Uni.bullet_count}', True, (242, 167, 68))
    Uni.Uni.cd = 5
    cloudGroup = pygame.sprite.Group()
    Cloud.currentCloud = 0
    Cloud.Cloud.cloud_bullets = pygame.sprite.Group()
    Uni.Uni.sun_bullets = pygame.sprite.Group()
    powGroup = pygame.sprite.Group()
    input_box1.text = ''


def game_over():
    global type_screen
    global username
    global count
    global docs
    global unirec
    global allrecords
    global index1

    if count:

        unirec = []
        for record in records.find().sort("Score"):
            unirec = unirec + [record]

        docs = []
        for i in range(min(15, records.count())):
            docs = docs + [unirec[records.count() - 1 - i]]

        for i in range(10):
            key1 = 'Name'
            key2 = 'Score'
            allrecords[i] = myfont1.render(f'{i + 1}. {docs[i][key1]} --> {docs[i][key2]}', True, (77, 100, 186))

        records.delete_many({})
        for doc in docs:
            key1 = 'Name'
            key2 = 'Score'
            newd = {
                        "Name": doc[key1],
                        "Score": doc[key2],
                    }
            records.insert_one(newd)

        count = False

    pos = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    text_end_score = myfont2.render(f'Score : {Uni.Uni.record}', True, (23, 89, 212))

    if 700 <= pos[0] <= 700 + 430 and 508 <= pos[1] <= 508 + 125 and click[0] == 1:
        type_screen = 0
        count = True

    if index1 == 15:
        index1 = 0
    else:
        index1 += 1
    win.blit(gameovers[index1], (0, 0))
    win.blit(text_end_score, (522, 5))
    for i in range(10):
        win.blit(allrecords[i], (145, 270 + i * 38))
    pygame.display.update()



def menu():
    global type_screen
    global run
    global esc
    global mark

    if esc:
        if mark:
            if Uni.Uni.hp == 0:
                new_game()
            type_screen = 1
            mark = False

    pos = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if 825 <= pos[0] <= 825 + 370 and 80 <= pos[1] <= 80 + 80 and click[0] == 1:
        new_game()
        type_screen = 3

    if 825 <= pos[0] <= 825 + 370 and 180 <= pos[1] <= 180 + 80 and click[0] == 1:
        run = False

    win.blit(menu_pic, (0, 0))
    pygame.display.update()


def draw_powbar(surf, x, y, pct):
    if pct < 0:
        pct = 0
    BarLenghts = 100
    BarHeigth = 20
    fill = (pct / 10) * BarLenghts
    out_rect = pygame.Rect(x, y, BarLenghts, BarHeigth)
    fill_rect = pygame.Rect(x, y, fill, BarHeigth)
    pygame.draw.rect(surf, (0, 255, 0), fill_rect)
    pygame.draw.rect(surf, (255, 255, 255), out_rect, 2)


def draw_window():

    win.blit(bg, (0, 0))
    win.blit(bul, (163, 3))
    win.blit(sh, (283, -3))

    if Uni.Uni.hp >= 0:
        win.blit(dest_heard, (1240, 5))
        win.blit(dest_heard, (1208, 5))
        win.blit(dest_heard, (1176, 5))
        win.blit(dest_heard, (1144, 5))
        win.blit(dest_heard, (1112, 5))

    if Uni.Uni.hp >= 1:
        win.blit(heard, (1240, 5))
        if Uni.Uni.hp >= 2:
            win.blit(heard, (1208, 5))
            if Uni.Uni.hp >= 3:
                win.blit(heard, (1176, 5))
                if Uni.Uni.hp >= 4:
                    win.blit(heard, (1144, 5))
                    if Uni.Uni.hp == 5:
                        win.blit(heard, (1112, 5))

    win.blit(uni.image, uni.rect)
    if uni.power != 0:
        win.blit(zont.image, zont.rect)
    powGroup.draw(win)
    cloudGroup.draw(win)
    Uni.Uni.sun_bullets.draw(win)
    Cloud.Cloud.cloud_bullets.draw(win)
    win.blit(text_score, (10, 5))
    win.blit(Uni.text_bullets, (185, 5))
    draw_powbar(win, 335, 9, Uni.time)
    # win.blit(text_level, (580, 5))

    powGroup.update()
    uni.update()
    zont.update(uni)
    cloudGroup.update()
    Uni.Uni.sun_bullets.update()
    Cloud.Cloud.cloud_bullets.update()
    pygame.display.update()


def play():
    global cd
    global text_score
    global type_screen
    global mark
    global esc

    if esc:
        type_screen = 0
        mark = True

    move_type = 0

    def unidata():
        global data
        data = {
                    "Name": username,
                    "Score": Uni.Uni.record,
                }
        records.insert_one(data)

    hits = pygame.sprite.spritecollide(uni, powGroup, True, pygame.sprite.collide_mask)
    for hit in hits:
        if hit.type == 0:
            count = randrange(10, 31)
            Uni.bullet_count += count
            Uni.text_bullets = myfont.render(f' : {Uni.bullet_count}', True, (242, 167, 68))
        elif hit.type == 1:
            uni.powerup()
        elif hit.type == 2:
            if Uni.Uni.hp < 5:
                Uni.Uni.hp += 1

    dest_cloud = pygame.sprite.groupcollide(cloudGroup, Uni.Uni.sun_bullets, True, True, pygame.sprite.collide_mask)
    Cloud.currentCloud -= len(dest_cloud)
    Uni.Uni.record += len(dest_cloud)
    text_score = myfont.render(f'Score : {Uni.Uni.record}', True, (23, 89, 212))
    for n in dest_cloud:
        if random.random() > 0.85:
            powGroup.add(Powerups.Powerups(n.rect.x, n.rect.y))

    if len(pygame.sprite.groupcollide(Cloud.Cloud.cloud_bullets, Uni.Uni.sun_bullets, True, True,
                                      pygame.sprite.collide_circle)):
        pass

    if len(pygame.sprite.spritecollide(uni, Cloud.Cloud.cloud_bullets, True, pygame.sprite.collide_mask)):
        if uni.power == 0:
            if Uni.Uni.hp > 0:
                Uni.Uni.hp -= 1
                if Uni.Uni.hp == 0:
                    type_screen = 2
                    unidata()
                    return
    if uni.power != 0:
        if len(pygame.sprite.spritecollide(zont, Cloud.Cloud.cloud_bullets, True, pygame.sprite.collide_mask)):
            if uni.power == 0:
                pass

        kek = pygame.sprite.spritecollide(zont, cloudGroup, True, pygame.sprite.collide_mask)
        if len(kek):
            Cloud.currentCloud -= len(kek)
            Uni.Uni.record += len(kek)
            text_score = myfont.render(f'Score : {Uni.Uni.record}', True, (23, 89, 212))
            for n in kek:
                if random.random() > 0.7:
                    powGroup.add(Powerups.Powerups(n.rect.x, n.rect.y))

    cloud_dest = pygame.sprite.spritecollide(uni, cloudGroup, True, pygame.sprite.collide_mask)
    if len(cloud_dest):
        if uni.power == 0:
            if Uni.Uni.hp > 0:
                Uni.Uni.hp -= 1
                if Uni.Uni.hp == 0:
                    type_screen = 2
                    unidata()
                    return
        Cloud.currentCloud -= len(cloud_dest)
        Uni.Uni.record += len(cloud_dest)
        text_score = myfont.render(f'Score : {Uni.Uni.record}', True, (23, 89, 212))
        for n in cloud_dest:
            if random.random() > 0.7:
                powGroup.add(Powerups.Powerups(n.rect.x, n.rect.y))

    side_type = randrange(1, 3)

    if side_type == 1:
        cl_x = 1280
        move_type = 1
    elif side_type == 2:
        cl_x = 0 - 200
        move_type = 0

    cl_y = randrange(25, 211)

    if cd == 0:
        cd = 20
        if randrange(2) % 2 == 0 and Cloud.currentCloud < Cloud.maxCloud:
            Cloud.currentCloud += 1
            cloudGroup.add(Cloud.Cloud(cl_x, cl_y, move_type))
    cd -= 1

    draw_window()


while run:
    clock.tick(30)
    esc = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                esc = True
        input_box1.handle_event(event)

    if type_screen == 0:
        menu()
    elif type_screen == 1:
        play()
    elif type_screen == 2:
        game_over()
    elif type_screen == 3:
        user()

pygame.quit()
