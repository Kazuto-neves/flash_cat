import pygame
from pygame.locals import *
from sys import exit
import os
from random import randrange
import time

pygame.init()
pygame.mixer.init()

diretorio_principal = os.path.dirname(__file__)
diretorio_imagens = os.path.join(diretorio_principal, 'image')
diretorio_sons = os.path.join(diretorio_principal, 'audio')

LARGURA = 640
ALTURA = 360
BRANCO = (255,255,255)
Vermelho = (255,0,0)
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption('Flash cat')
back = pygame.image.load(os.path.join(diretorio_imagens,'back.png')).convert_alpha()
sprite_sheet = pygame.image.load(os.path.join(diretorio_imagens, 'sprite.png')).convert_alpha()
colidiu = False
bullets = []
v=0

class Cat(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imagens_cat = []
        for i in range(8):
            img = sprite_sheet.subsurface((i * 508,0), (514,407))
            img = pygame.transform.scale(img, (int(28*3),int(20*3)))
            self.imagens_cat.append(img)
        
        self.index_lista = 0
        self.image = self.imagens_cat[self.index_lista]
        self.rect = self.image.get_rect()
        #self.rect.center = (100,180)
        self.mask = pygame.mask.from_surface(self.image)
        self.y= 250
        self.x= 20
        self.rect.topleft = (self.x, self.y) #368   416(centro y)
        self.moveu= False
        self.moved= False
        self.movel= False
        self.mover= False
        self.crash = False
        self.wreck_start = False
        self.wrecked = False

    def MoveU(self,n):
        if n == True:
            self.moveu = True
            self.moved = False
            self.movel = False
            self.mover = False
        else:self.moveu = False
    def MoveD(self,n):
        if n == True:
            self.moveu = False
            self.moved = True
            self.movel = False
            self.mover = False
        else:self.moved = False
    def MoveR(self,n):
        if n == True:
            self.moveu = False
            self.moved = False
            self.movel = False
            self.mover = True
        else:self.mover = False
    def MoveL(self,n):
        if n == True:
            self.moveu = False
            self.moved = False
            self.movel = True
            self.mover = False
        else:self.movel = False
    def Crash(self,n):
        self.crash = True

    def update(self):
        if self.moveu == True:
            if self.rect.y == 80:self.moveu = False
            else:self.rect.y-=10

        elif self.moved == True:
            if self.rect.y == 260:self.moved = False
            else:self.rect.y+=10

        elif self.mover == True:
            if self.rect.x == 550:self.mover = False
            else:self.rect.x+=10

        elif self.movel == True:
            if self.rect.x == 10:self.movel = False
            else:self.rect.x-=10

        #if self.crash == False:
        if self.index_lista > 7:self.index_lista = 0
        self.index_lista += 0.25
        self.image = self.imagens_cat[int(self.index_lista)]
        #else:
        #    self.index_lista = 8
        #    if self.index_lista > 10:self.index_lista = 8
        #    self.index_lista += 0.9
        #    self.image = self.imagens_cat[int(self.index_lista)]

class Cloud(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((10*512, 0), (514,407))
        self.image = pygame.transform.scale(self.image, (int(28*3),int(20*3)))
        self.rect = self.image.get_rect()
        self.rect.y = randrange(10, 50, 50)
        self.rect.x = LARGURA - randrange(50, 200, 90)
        

    def update(self):
        if self.rect.topright[0] < 0:
            self.rect.x = LARGURA
            self.rect.y = randrange(20, 70, 50)
        self.rect.x -= 10

class Mouse(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((11*520, 0), (514,407))
        self.image = pygame.transform.scale(self.image, (int(28*3),int(20*3)))
        self.rect = self.image.get_rect()
        self.rect.y = randrange(81, 100, 50)
        self.rect.x = LARGURA - randrange(30, 290, 90)
        self.crash = False

    def Crash (self):crash=True

    def update(self):
        if self.rect.topright[0] < 0:
            self.rect.x = LARGURA
            self.rect.y = randrange(81, 285, 50)
        self.rect.x -= 10
        if self.rect.y == 82:self.rect.y += 20
        elif self.rect.y == 284:self.rect.y -= 10


class Back(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imagens_back = []
        self.n=1
        self.v=640*self.n
        for i in range(2):
            bk = back.subsurface((i * self.v,0), (640,320))
            bk = pygame.transform.scale(bk, (int(640*2),int(360*2)))
            self.imagens_back.append(bk)
        self.index_lista = 0
        self.image = self.imagens_back[self.index_lista]
        self.rect = self.image.get_rect()
        self.rect.center = (0,0)

    def update(self):
        if self.index_lista > 1:self.index_lista = 0
        self.index_lista += 0.1
        self.image = self.imagens_back[int(self.index_lista)]


todas_as_sprites = pygame.sprite.Group()
cat = Cat()
back = Back()
todas_as_sprites.add(back)
todas_as_sprites.add(cat)

for i in range(3):
    cloud = Cloud()
    todas_as_sprites.add(cloud)

#for i in range(9):

mouse1 = Mouse()
mouse2 = Mouse()
mouse3 = Mouse()
mouse4 = Mouse()

todas_as_sprites.add(mouse1,mouse2,mouse3,mouse4)

grupo_obstaculos = pygame.sprite.Group()
grupo_obstaculos.add(mouse1,mouse2,mouse3,mouse4)

relogio = pygame.time.Clock()
def game_loop():
    global colidiu
    global bullets

    while True:
        relogio.tick(30)
        tela.fill(BRANCO)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_w or event.key == K_UP:cat.MoveU(True)
                if event.key == K_s or event.key == K_DOWN:cat.MoveD(True)
                if event.key == K_a or event.key == K_LEFT:cat.MoveL(True)
                if event.key == K_d or event.key == K_RIGHT:cat.MoveR(True)
                if event.key == pygame.K_SPACE:
                    if not cat.wreck_start:bullets.append([cat.x, cat.y])
            elif event.type == KEYUP:
                if event.key == K_w or event.key == K_UP:cat.MoveU(False)
                if event.key == K_s or event.key == K_DOWN:cat.MoveD(False)
                if event.key == K_a or event.key == K_LEFT:cat.MoveL(False)
                if event.key == K_d or event.key == K_RIGHT:cat.MoveR(False)

        colisoes = pygame.sprite.spritecollide(cat, grupo_obstaculos, False, pygame.sprite.collide_mask)

        todas_as_sprites.draw(tela)

        if not cat.wreck_start and not cat.wrecked:
            for draw_bullet in bullets:pygame.draw.rect(tela, Vermelho, (draw_bullet[0]+90, draw_bullet[1]+40, 10, 10))

            for move_bullet in range(len(bullets)):bullets[move_bullet][0] += 40

            for del_bullet in bullets:
                if del_bullet[0] >= 800:bullets.remove(del_bullet)

        if colisoes and colidiu == False:
            colidiu = True
            cat.wrecked = True
            print("colidiu")
            #cat.Crash()
            #mouse.Crash()
        if colidiu == True:pass
        else:todas_as_sprites.update()


        pygame.display.flip()

game_loop()