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
Amarelo = (255,255,0)
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption('Flash cat')
back = pygame.image.load(os.path.join(diretorio_imagens,'back.png')).convert_alpha()
sprite_sheet = pygame.image.load(os.path.join(diretorio_imagens, 'sprite.png')).convert_alpha()
colidiu = False
bullets = []
v=0
x=0
y=0

def game(Col,B,Time,T,Color,catMU,catMD,catML,catMR,Cws,Cwr,c,GO,Color2,TS,M1,M2,M3,M4,X,Y):
    while True:
        Time.tick(30)
        T.fill(Color)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_w or event.key == K_UP:catMU(True)
                if event.key == K_s or event.key == K_DOWN:catMD(True)
                if event.key == K_a or event.key == K_LEFT:catML(True)
                if event.key == K_d or event.key == K_RIGHT:catMR(True)
                if event.key == pygame.K_SPACE:
                    if not Cws:B.append([c.x, c.y])
            elif event.type == KEYUP:
                if event.key == K_w or event.key == K_UP:catMU(False)
                if event.key == K_s or event.key == K_DOWN:catMD(False)
                if event.key == K_a or event.key == K_LEFT:catML(False)
                if event.key == K_d or event.key == K_RIGHT:catMR(False)

        colisoes = pygame.sprite.spritecollide(c, GO, False, pygame.sprite.collide_mask)

        if M1.rect.x == X and M1.rect.y == Y:
            print("acertou1")
            M1.rect.y += 10
        
        if M2.rect.x == X and M2.rect.y == Y:
            print("acertou2")
            M2.rect.y += 10

        if M3.rect.x == X and M3.rect.y == Y:
            print("acertou3")
            M3.rect.y += 10

        if M4.rect.x == X and M4.rect.y == Y:
            print("acertou4")
            M4.rect.y += 10

        TS.draw(T)

        fire(Cws,Cwr,T,Color2,B,x,y)

        if colisoes and Col == False:
            Col = True
            Cwr = True
            print("colidiu")
        if Col == True:pass
        else:TS.update()

        pygame.display.flip()

def fire(Cws,Cwr,T,color,B,x,y):
    if not Cws and not Cwr:
        for draw_bullet in B:
            pygame.draw.rect(T, color, (draw_bullet[0]+90, draw_bullet[1]+20, 10, 10))
            y=draw_bullet[1]
        for move_bullet in range(len(B)):
            B[move_bullet][0] += 40
            x=move_bullet
        for del_bullet in B:
                if del_bullet[0] >= 640:B.remove(del_bullet)

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
        self.mask = pygame.mask.from_surface(self.image)
        self.y= 250
        self.x= 20
        self.rect.topleft = (self.x, self.y)
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
            else:
                self.rect.y-=10
                self.y = self.rect.y

        elif self.moved == True:
            if self.rect.y == 260:self.moved = False
            else:
                self.rect.y+=10
                self.y = self.rect.y

        elif self.mover == True:
            if self.rect.x == 550:self.mover = False
            else:
                self.rect.x+=10
                self.x = self.rect.x

        elif self.movel == True:
            if self.rect.x == 10:self.movel = False
            else:
                self.rect.x-=10
                self.x = self.rect.x

        if self.index_lista > 7:self.index_lista = 0
        self.index_lista += 0.25
        self.image = self.imagens_cat[int(self.index_lista)]

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

    def pos (self):return [self.rect.x,self.rect.y]

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
    game(colidiu,bullets,relogio,tela,BRANCO,cat.MoveU,cat.MoveD,cat.MoveL,cat.MoveR,cat.wreck_start,cat.wrecked,cat,grupo_obstaculos,Amarelo,todas_as_sprites,mouse1,mouse2,mouse3,mouse4,x,y)
game_loop()