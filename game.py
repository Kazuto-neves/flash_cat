import pygame
from pygame.locals import *
from sys import exit
import os
from random import *
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
colidiuM = False
bullets = []
v=0
x=0
y=0
game_over = False

def game(Col,B,Time,T,Color,catMU,catMD,catML,catMR,Cws,Cwr,c,GO,Color2,TS,M1,M2,M3,M4,x,y,G,GOM1,GOM2,GOM3,GOM4,Col2):
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
        colM1 = pygame.sprite.spritecollide(M1, GOM1, False, pygame.sprite.collide_mask)
        colM2 = pygame.sprite.spritecollide(M2, GOM2, False, pygame.sprite.collide_mask)
        colM3 = pygame.sprite.spritecollide(M3, GOM3, False, pygame.sprite.collide_mask)
        colM4 = pygame.sprite.spritecollide(M4, GOM4, False, pygame.sprite.collide_mask)

        TS.draw(T)

        fire(Cws,Cwr,T,Color2,B,x,y)
        boom(Cws,Cwr,G,B,M1,M2,M3,M4)


#        if colM1 and Col2 == False:Col2 = True
#        if Col2 == True:
#            R=randrange(1, 2)
#            Col2=False
#            M1.esp(R)

#        if colM2 and Col2 == False:Col2 = True
#        if Col2 == True:
#            R=randrange(1, 2)
#            Col2=False
#            M2.esp(R)

#        if colM3 and Col2 == False:Col2 = True
#        if Col2 == True:
#            R=randrange(1, 2)
#            Col2=False
#            M3.esp(R)
        
#        if colM4 and Col2 == False:Col2 = True
#        if Col2 == True:
#            R=randrange(1, 2)
#            Col2=False
#            M4.esp(R)

        if colisoes and Col == False:
            Col = True
            Cwr = True
            print("colidiu")
        if Col == True:pass
        else:TS.update()

        pygame.display.flip()

def boom(Cws,Cwr,G,B,M1,M2,M3,M4):
    if not Cws and not Cwr and not G:
        for pop_balloon in B:
            if M1.x < pop_balloon[0]+90 < M1.y and M1.x < pop_balloon[1]+40 < M1.y+100:
                B.remove(pop_balloon)
                M1.pos(LARGURA)
            elif M2.x < pop_balloon[0]+90 < M2.y and M2.x < pop_balloon[1]+40 < M2.y+100:
                B.remove(pop_balloon)
                M2.pos(LARGURA)
            elif M3.x < pop_balloon[0]+90 < M3.y and M3.x < pop_balloon[1]+40 < M3.y+100:
                B.remove(pop_balloon)
                M3.pos(LARGURA)
            elif M4.x < pop_balloon[0]+90 < M4.y and M4.x < pop_balloon[1]+40 < M4.y+100:
                B.remove(pop_balloon)
                M4.pos(LARGURA - randrange(50, 200, 90) )
            elif M1.x < pop_balloon[0]+100 < M1.x+70 and M1.y < pop_balloon[1]+50 < M1.y+100:
                B.remove(pop_balloon)
                M1.pos(LARGURA)
            elif M2.x < pop_balloon[0]+100 < M2.x+70 and M2.y < pop_balloon[1]+50 < M2.y+100:
                B.remove(pop_balloon)
                M2.pos(LARGURA)
            elif M3.x < pop_balloon[0]+100 < M3.x+70 and M3.y < pop_balloon[1]+50 < M3.y+100:
                B.remove(pop_balloon)
                M3.pos(LARGURA)
            elif M4.x < pop_balloon[0]+100 < M4.x+70 and M4.y < pop_balloon[1]+50 < M4.y+100:
                B.remove(pop_balloon)
                M4.pos(LARGURA)

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
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.y = randrange(81, 100, 50)
        self.rect.x = LARGURA - randrange(30, 290, 90)
        self.x=self.rect.x
        self.y=self.rect.y


    def pos (self,x):
        self.crach=True
        self.rect.x=x

    def esp (self,x):
        if x == 0:self.rect.x+=20
        else: self.rect.y+=20


    def update(self):
        if self.rect.topright[0] < 0:
            self.rect.x = LARGURA
            self.rect.y = randrange(81, 285, 50)
        self.rect.x -= 10
        self.x=self.rect.x
        self.y=self.rect.y  
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

grupo_oM1 = pygame.sprite.Group()
grupo_oM1.add(mouse2,mouse3,mouse4)

grupo_oM2 = pygame.sprite.Group()
grupo_oM2.add(mouse1,mouse3,mouse4)

grupo_oM3 = pygame.sprite.Group()
grupo_oM3.add(mouse1,mouse2,mouse4)

grupo_oM4 = pygame.sprite.Group()
grupo_oM4.add(mouse1,mouse2,mouse3)

relogio = pygame.time.Clock()

def game_loop():
    global colidiu
    global bullets
    game(colidiu,bullets,relogio,tela,BRANCO,cat.MoveU,cat.MoveD,cat.MoveL,cat.MoveR,cat.wreck_start,cat.wrecked,cat,grupo_obstaculos,Amarelo,todas_as_sprites,mouse1,mouse2,mouse3,mouse4,x,y,game_over,grupo_oM1,grupo_oM2,grupo_oM3,grupo_oM4,colidiuM)
game_loop()