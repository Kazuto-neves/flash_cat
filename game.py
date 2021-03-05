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

def tiro(m):
    if m == True:
        ti=pygame.mixer.Sound(os.path.join(diretorio_sons,'kill.ogg'))
        ti.play()

def Mtiro(m):
    if m == True:
        mt=pygame.mixer.Sound(os.path.join(diretorio_sons,'Mkill.mp3'))
        mt.play()

def explosion(m):
    if m == True:
       exp=pygame.mixer.Sound(os.path.join(diretorio_sons,'explosion.mp3'))
       exp.set_volume(0.02)
       exp.play()

def music(m,p,r,l):
    if m == True:
        pygame.mixer.music.load(os.path.join(diretorio_sons,'music.mp3'))
        pygame.mixer.music.play(-1)
    if p == True:pygame.mixer.music.pause()
    else:
        if r == True:pygame.mixer.music.unpause()
    if l == 93000000:pygame.mixer.music.rewind()

LARGURA = 640
ALTURA = 360
BRANCO = (255,255,255)
Vermelho = (255,0,0)
Amarelo = (255,255,0)
Preto =(0,0,0)
Verde=(0,128,0)
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
run = True
pts=0
m=False
Tm=False
Mega=0
w=0
h=0
M=False
p=False
r=False
l=0

#def Plot(CT,C):
#    texto("Controles:",CT,40,LARGURA/3,220)
#    texto("Mover com WASD ou as Cetas",C,30,LARGURA/3,260)
#    texto("Pausar use o P",C,30,LARGURA/3,300)


def control(CT,C):
    texto("Controles:",CT,40,LARGURA/3,220)
    texto("Mover com WASD ou as Cetas",C,30,LARGURA/3,250)
    texto("Pausar use o P",C,30,LARGURA/3,270)
    texto("Mudar o tema L",C,30,LARGURA/3,290)
    texto("SOM com TAB",C,30,LARGURA/3,310)
    texto("Especial com Q",C,30,LARGURA/3,330)


def menu_audio(x):
        if x == True:ss = pygame.image.load(os.path.join(diretorio_imagens, 'Ssom.png')).convert_alpha()
        else:ss = pygame.image.load(os.path.join(diretorio_imagens, 'Csom.png')).convert_alpha()
        tela.blit(ss, [4, 304,20,20])


def placar(pts,x):
    texto("Pontuação:"+str(pts),Preto,50,340,10)
    texto("Mega cheeses:",Preto,35,10,10)
    pygame.draw.rect(tela,BRANCO, [183,12,x,20])
    pygame.draw.rect(tela,Preto, [234, 12, 0, 20], 5)
    pygame.draw.rect(tela,Vermelho, [184, 12, 100, 20], 5)

def go(pts,S,Tm):
    tela.fill(bg(Tm))
    texto("Game Over",bc(Tm),100,LARGURA/5, ALTURA/14)
    texto("Pontuação:"+str(pts),bt(Tm),50,LARGURA/3, ALTURA/4)
    pygame.draw.rect(tela,bt(Tm), [140,140,150,50])
    texto("Continuar",fcb(Tm),30,155,145)
    texto("(ESPAÇO)",fcb(Tm),30,155,165)
    pygame.draw.rect(tela,bt(Tm), [350,140,150,50])
    texto("Sair",fcb(Tm),30,400,145)
    texto("(Esc)",fcb(Tm),30,400,165)
    control(bc(Tm),fc(Tm))
    tema(bt(Tm),bc(Tm),Tm)
    menu_audio(S)
    pygame.display.update()

def pause(pts,S,Tm):
    tela.fill(bg(Tm))
    texto("Pause",bc(Tm),100,LARGURA/3, ALTURA/14)
    texto("Pontuação:"+str(pts),bt(Tm),50,LARGURA/3, ALTURA/4)
    pygame.draw.rect(tela,bt(Tm), [140,140,150,50])
    texto("Continuar",fcb(Tm),30,155,145)
    texto("(ESPAÇO)",fcb(Tm),30,155,165)
    pygame.draw.rect(tela,bt(Tm), [350,140,150,50])
    texto("Re-começar",fcb(Tm),30,380,145)
    texto("(F5)",fcb(Tm),30,400,165)
    control(bc(Tm),fc(Tm))
    tema(bt(Tm),bc(Tm),Tm)
    menu_audio(S)
    pygame.display.update()

def texto(msg, cor, t,x,y):
    fonte = pygame.font.SysFont(None, t)
    texto1 = fonte.render(msg, True, cor)
    tela.blit(texto1, [x, y])

def bg(bg):
    if bg == True:return (Preto)
    else:return (BRANCO)

def fc(fc):
    if fc == True:return (BRANCO)
    else:return (Preto)

def bc(bc):
    if bc == True:return (Amarelo)
    else:return (Vermelho)

def bt(bt):
    if bt == True:return (Verde)
    else:return (Preto)

def fcb(fcb):
    if fcb == True:return (Amarelo)
    else:return (BRANCO)

def img(tl):
    if tl == True:sl = pygame.image.load(os.path.join(diretorio_imagens, 'sol.png')).convert_alpha()
    else:sl = pygame.image.load(os.path.join(diretorio_imagens, 'lua.png')).convert_alpha()
    tela.blit(sl, [19, 19])

def tema(bt,bc,T):
        pygame.draw.rect(tela,bt, [12,12,44,44], border_radius=15)
        pygame.draw.rect(tela,bc, [10, 10, 50, 50], 5, border_radius=15)
        img(T)

def main (s,Tm):
    inicio = True
    while inicio:
        tela.fill(bg(Tm))
        texto("Flash Cat",bc(Tm),60,LARGURA/3, ALTURA/14)
        pygame.draw.rect(tela,bt(Tm), [250,70,130,25])
        texto("Medio(1)",fcb(Tm),30,275,75)
        pygame.draw.rect(tela,bt(Tm), [250,120,130,25])
        texto("Dificil(2)",fcb(Tm),30,275,125)
        pygame.draw.rect(tela,bt(Tm), [250,170,130,25])
        texto("Insano(3)",fcb(Tm),30,275,175)
        pygame.draw.rect(tela,Vermelho, [510,0,130,25])
        texto("Sair(esc)",BRANCO,30,535,5)
        tema(bt(Tm),bc(Tm),Tm)
        menu_audio(s)
        control(bc(Tm),fc(Tm))
        pygame.display.update()
        for event in pygame.event.get():
                if event.type == pygame.QUIT:pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        inicio = False
                        n=1
                        game_loop(n,s)
                    if event.key == pygame.K_2:
                        inicio = False
                        n=2
                        game_loop(n,s)
                    if event.key == pygame.K_3:
                        inicio = False
                        n=3
                        game_loop(n,s)
                    if event.key == pygame.K_TAB:
                        if s== True:s=False
                        else:s=True
                        pygame.display.update()
                    if event.key == pygame.K_l:
                        if Tm==False:Tm=True
                        else:Tm=False
                        pygame.display.update()
                        
                    if event.key == pygame.K_ESCAPE:pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x = pygame.mouse.get_pos()[0]
                    y = pygame.mouse.get_pos()[1]
                    if x > 250 and y > 70 and x < 380 and y < 95:
                        inicio = False
                        n=1
                        game_loop(n,s)
                    if x > 250 and y > 120 and x < 380 and y < 145:
                        inicio = False
                        n=2
                        game_loop(n,s)
                    if x > 250 and y > 170 and x < 380 and y < 195:
                        inicio = False
                        n=3
                        game_loop(n,s)
                    if x > 2 and y > 302 and x < 46 and y < 352:
                        if s== True:s=False
                        else:s=True
                        print("mudei")
                        pygame.display.update()
                    if x > 10 and y > 10 and x < 60 and y < 60:
                        if Tm==False:Tm=True
                        else:Tm=False
                        pygame.display.update()
                    if x > 510 and y > 0 and x < 640 and y < 25:pygame.quit()


def game(Col,B,Time,T,Color,catMU,catMD,catML,catMR,Cws,Cwr,c,GO,Color2,TS,M1,M2,M3,M4,x,y,G,GOM1,GOM2,GOM3,GOM4,Col2,LV,R,P,CD,BK,s,Tm,f,w,h,M,p,r,L):
    o=1
    M1.lv(LV)
    M2.lv(LV)
    M3.lv(LV)
    M4.lv(LV)
    music(s,p,r,l)
    while R:
        L+=1 
        while G:
            if o == 1:
                go(P,s,Tm)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        R = False
                        G = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            R = True
                            G = False
                            c.y= 250
                            c.x= 20
                            M1.rect.y = randrange(81, 100, 50)
                            M1.rect.x = LARGURA - randrange(30, 290, 90)
                            M2.rect.y = randrange(81, 100, 50)
                            M2.rect.x = LARGURA - randrange(30, 290, 90)
                            M3.rect.y = randrange(81, 100, 50)
                            M3.rect.x = LARGURA - randrange(30, 290, 90)
                            M4.rect.y = randrange(81, 100, 50)
                            M4.rect.x = LARGURA - randrange(30, 290, 90)
                            Col=False
                            Cwr=False
                            P=0
                            f=0
                            w=0
                            h=0
                            M=False
                            r=False
                            p=False
                            L=0
                            #fire(Cws,Cwr,T,Color2,B,x,y)
                        if event.key == pygame.K_TAB:
                            if s== True:s=False
                            else:s=True
                            pygame.display.update()
                        if event.key == pygame.K_l:
                            if Tm==False:Tm=True
                            else:Tm=False
                            pygame.display.update()
                        if event.key == pygame.K_ESCAPE:
                            R = False
                            G = False
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        X = pygame.mouse.get_pos()[0]
                        Y = pygame.mouse.get_pos()[1]
                        if X > 140 and Y > 140 and X < 290 and Y < 190:
                            R = True
                            G = False
                            c.y= 250
                            c.x= 20
                            M1.rect.y = randrange(81, 100, 50)
                            M1.rect.x = LARGURA - randrange(30, 290, 90)
                            M2.rect.y = randrange(81, 100, 50)
                            M2.rect.x = LARGURA - randrange(30, 290, 90)
                            M3.rect.y = randrange(81, 100, 50)
                            M3.rect.x = LARGURA - randrange(30, 290, 90)
                            M4.rect.y = randrange(81, 100, 50)
                            M4.rect.x = LARGURA - randrange(30, 290, 90)
                            Col=False
                            Cwr=False
                            P=0
                            f=0
                            w=0
                            h=0
                            M=False
                            r=False
                            p=False
                            L=0
                            #fire(Cws,Cwr,T,Color2,B,x,y)
                        if x > 2 and y > 302 and x < 46 and y < 352:
                            if s== True:s=False
                            else:s=True
                            print("mudei")
                            pygame.display.update()
                        if x > 10 and y > 10 and x < 60 and y < 60:
                            if Tm==False:Tm=True
                            else:Tm=False
                            pygame.display.update()
                        if X > 350 and Y > 140 and X < 500 and Y < 190:
                            R = False
                            G = False
            else:
                pause(P,s,Tm)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        R = False
                        G = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            R = True
                            G = False
                            o=1
                            #fire(Cws,Cwr,T,Color2,B,x,y)
                        if event.key == pygame.K_F5:
                            R = True
                            G = False
                            c.y= 250
                            c.x= 20
                            M1.rect.y = randrange(81, 100, 50)
                            M1.rect.x = LARGURA - randrange(30, 290, 90)
                            M2.rect.y = randrange(81, 100, 50)
                            M2.rect.x = LARGURA - randrange(30, 290, 90)
                            M3.rect.y = randrange(81, 100, 50)
                            M3.rect.x = LARGURA - randrange(30, 290, 90)
                            M4.rect.y = randrange(81, 100, 50)
                            M4.rect.x = LARGURA - randrange(30, 290, 90)
                            Col=False
                            Cwr=False
                            P=0
                            o=1
                            r=False
                            p=False
                            L=0
                        if event.key == pygame.K_TAB:
                            if s== True:s=False
                            else:s=True
                            pygame.display.update()
                        if event.key == pygame.K_l:
                            if Tm==False:Tm=True
                            else:Tm=False
                            pygame.display.update()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        X = pygame.mouse.get_pos()[0]
                        Y = pygame.mouse.get_pos()[1]
                        if X > 140 and Y > 140 and X < 290 and Y < 190:
                            R = True
                            G = False
                            o=1
                            #fire(Cws,Cwr,T,Color2,B,x,y)
                        if X > 350 and Y > 140 and X < 500 and Y < 190:
                            R = True
                            G = False
                            c.y= 250
                            c.x= 20
                            M1.rect.y = randrange(81, 100, 50)
                            M1.rect.x = LARGURA - randrange(30, 290, 90)
                            M2.rect.y = randrange(81, 100, 50)
                            M2.rect.x = LARGURA - randrange(30, 290, 90)
                            M3.rect.y = randrange(81, 100, 50)
                            M3.rect.x = LARGURA - randrange(30, 290, 90)
                            M4.rect.y = randrange(81, 100, 50)
                            M4.rect.x = LARGURA - randrange(30, 290, 90)
                            Col=False
                            Cwr=False
                            P=0
                            o=1
                            r=False
                            p=False
                            L=0
                        if x > 2 and y > 302 and x < 46 and y < 352:
                            if s== True:s=False
                            else:s=True
                            print("mudei")
                            pygame.display.update()
                        if x > 10 and y > 10 and x < 60 and y < 60:
                            if Tm==False:Tm=True
                            else:Tm=False
                            pygame.display.update()
        Time.tick(30)
        T.fill(Color)
        TS.draw(T)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_w or event.key == K_UP:catMU(True,s)
                if event.key == K_s or event.key == K_DOWN:catMD(True,s)
                if event.key == K_a or event.key == K_LEFT:catML(True,s)
                if event.key == K_d or event.key == K_RIGHT:catMR(True,s)
                if event.key == K_p:
                    G=True
                    o=2
                if event.key == K_SPACE:
                    if not Cws:B.append([c.x, c.y]) 
                    tiro(s)
                    if f <=100:f+=1
                    else:f
                    w=(6.4*f)/2
                    h=(3.6*f)/2
                if event.key == K_q:
                    if f>=50:
                        M=True
                        Mtiro(s)
                        f=0
            elif event.type == KEYUP:
                if event.key == K_w or event.key == K_UP:catMU(False,s)
                if event.key == K_s or event.key == K_DOWN:catMD(False,s)
                if event.key == K_a or event.key == K_LEFT:catML(False,s)
                if event.key == K_d or event.key == K_RIGHT:catMR(False,s)
                if event.key == K_q:M=False

        colisoes = pygame.sprite.spritecollide(c, GO, False, pygame.sprite.collide_mask)
        colM1 = pygame.sprite.spritecollide(M1, GOM1, False, pygame.sprite.collide_mask)
        colM2 = pygame.sprite.spritecollide(M2, GOM2, False, pygame.sprite.collide_mask)
        colM3 = pygame.sprite.spritecollide(M3, GOM3, False, pygame.sprite.collide_mask)
        colM4 = pygame.sprite.spritecollide(M4, GOM4, False, pygame.sprite.collide_mask)

        placar(P,f)
        P+=1
        fire(Cws,Cwr,T,Color2,B,x,y,M,w,h)
        boom(Cws,Cwr,G,B,M1,M2,M3,M4,P,s)


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
        if Col == True:G=True
        else:TS.update()

        pygame.display.flip()

def boom(Cws,Cwr,G,B,M1,M2,M3,M4,P,M):
    if not Cws and not Cwr and not G:
        for pop_balloon in B:
            if M1.x < pop_balloon[0]+90 < M1.y and M1.x < pop_balloon[1]+40 < M1.y+100:
                B.remove(pop_balloon)
                M1.pos(LARGURA,randrange(81, 285, 50),P)
                explosion(M)
            elif M2.x < pop_balloon[0]+90 < M2.y and M2.x < pop_balloon[1]+40 < M2.y+100:
                B.remove(pop_balloon)
                M2.pos(LARGURA,randrange(81, 285, 50),P)
                explosion(M)
            elif M3.x < pop_balloon[0]+90 < M3.y and M3.x < pop_balloon[1]+40 < M3.y+100:
                B.remove(pop_balloon)
                M3.pos(LARGURA,randrange(81, 285, 50),P)
            elif M4.x < pop_balloon[0]+90 < M4.y and M4.x < pop_balloon[1]+40 < M4.y+100:
                B.remove(pop_balloon)
                M4.pos(LARGURA,randrange(81, 285, 50),P)
                explosion(M)
            elif M1.x < pop_balloon[0]+100 < M1.x+70 and M1.y < pop_balloon[1]+50 < M1.y+100:
                B.remove(pop_balloon)
                M1.pos(LARGURA,randrange(81, 285, 50),P)
                explosion(M)
            elif M2.x < pop_balloon[0]+100 < M2.x+70 and M2.y < pop_balloon[1]+50 < M2.y+100:
                B.remove(pop_balloon)
                M2.pos(LARGURA,randrange(81, 285, 50),P)
                explosion(M)
            elif M3.x < pop_balloon[0]+100 < M3.x+70 and M3.y < pop_balloon[1]+50 < M3.y+100:
                B.remove(pop_balloon)
                M3.pos(LARGURA,randrange(81, 285, 50),P)
                explosion(M)
            elif M4.x < pop_balloon[0]+100 < M4.x+70 and M4.y < pop_balloon[1]+50 < M4.y+100:
                B.remove(pop_balloon)
                M4.pos(LARGURA,randrange(81, 285, 50),P)
                explosion(M)

def fire(Cws,Cwr,T,color,B,x,y,M,w,h):
    if not Cws and not Cwr:
        if M == False:
            for draw_bullet in B:
                pygame.draw.rect(T, color, (draw_bullet[0]+90, draw_bullet[1]+20, 10, 10))
                y=draw_bullet[1]
            for move_bullet in range(len(B)):
                B[move_bullet][0] += 20
                x=move_bullet
            for del_bullet in B:
                if del_bullet[0] >= 640:B.remove(del_bullet)
        else:
            for draw_bullet in B:
                pygame.draw.rect(T, color, (draw_bullet[0]+90, draw_bullet[1]+20, w, h))
                y=draw_bullet[1]
            for move_bullet in range(len(B)):
                B[move_bullet][0] += 0.1
                x=move_bullet
            for del_bullet in B:
                if del_bullet[0] >= 640:B.remove(del_bullet)

class Cat(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.mo = pygame.mixer.Sound(os.path.join(diretorio_sons, 'Movement.mp3'))
        self.mo.set_volume(1)
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

    def MoveU(self,n,s):
        if n == True:
            if s == True:self.mo.play()
            self.moveu = True
            self.moved = False
            self.movel = False
            self.mover = False
        else:self.moveu = False
    def MoveD(self,n,s):
        if n == True:
            if s == True:self.mo.play()
            self.moveu = False
            self.moved = True
            self.movel = False
            self.mover = False
        else:self.moved = False
    def MoveR(self,n,s):
        if n == True:
            if s == True:self.mo.play()
            self.moveu = False
            self.moved = False
            self.movel = False
            self.mover = True
        else:self.mover = False
    def MoveL(self,n,s):
        if n == True:
            if s == True:self.mo.play()
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
        self.s=11
        self.image = sprite_sheet.subsurface((self.s*520, 0), (514,407))
        self.image = pygame.transform.scale(self.image, (int(28*3),int(20*3)))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.y = randrange(81, 100, 50)
        self.rect.x = LARGURA - randrange(30, 290, 90)
        self.x=self.rect.x
        self.y=self.rect.y
        self.v=10


    def pos (self,x,y,P):
        self.crach=True
        self.s=12
        self.rect.x=x
        self.rect.y =y
        P+=1000

    def esp (self,x):
        if x == 0:self.rect.x+=20
        else: self.rect.y+=20

    def lv (self,x):
        if x == 1:self.v=10
        elif x == 2:self.v=15
        elif x == 3:self.v=20



    def update(self):
        if self.rect.topright[0] < 0:
            self.rect.x = LARGURA
            self.rect.y = randrange(81, 285, 50)
        self.rect.x -= self.v
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

def game_loop(n,s):
    global colidiu
    global bullets
    LV=n
    game(colidiu,bullets,relogio,tela,BRANCO,cat.MoveU,cat.MoveD,cat.MoveL,cat.MoveR,cat.wreck_start,cat.wrecked,cat,grupo_obstaculos,Amarelo,todas_as_sprites,mouse1,mouse2,mouse3,mouse4,x,y,game_over,grupo_oM1,grupo_oM2,grupo_oM3,grupo_oM4,colidiuM,LV,run,pts,cloud,back,s,Tm,Mega,w,h,M,p,r,l)


main(m,Tm)