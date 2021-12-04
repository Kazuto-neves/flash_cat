from random import *
import audio as a

LARGURA = 640
ALTURA = 360
BRANCO = (255,255,255)
Vermelho = (255,0,0)
Amarelo = (255,255,0)
Preto =(0,0,0)
Verde=(0,128,0)
colidiu = False
colidiuM = False
bullets = []
v=0
x=0
y=0
game_over = False
pts=0
m=False
Tm=False
Mega_Bullets=0
w=0
h=0
Mega_On=False
p=False
runSong=False
run=True
Loop=0
N_Wave=1
CONT=0
Q=1
V=20
UP=300
u=0

def reset(Col,cat,M1,M2,M3,M4,EndGame,catDestruido,P,start_music):
    run=True
    EndGame = False
    cat.y= 250
    cat.x= 20
    cat.rect.x=20
    cat.rect.y=250
    M1.rect.y = randrange(81, 100, 50)
    M1.rect.x = LARGURA - randrange(30, 290, 90)
    M2.rect.y = randrange(81, 100, 50)
    M2.rect.x = LARGURA - randrange(30, 290, 90)
    M3.rect.y = randrange(81, 100, 50)
    M3.rect.x = LARGURA - randrange(30, 290, 90)
    M4.rect.y = randrange(81, 100, 50)
    M4.rect.x = LARGURA - randrange(30, 290, 90)
    Col=False
    catDestruido=False
    Mega_Bullets=0
    w=0
    h=0
    Mega_On
    runSong=False
    p=False
    Loop=0
    M1.reset()
    M2.reset()
    M3.reset()
    M4.reset()
    N_Wave
    P=0
    CONT=0
    if start_music == True:
        a.runSong(True)
        runSong=True

def pause(Col,cat,M1,M2,M3,M4,EndGame,catDestruido,P,start_music):
    run = True
    EndGame = False
    cat.y= 250
    cat.x= 20
    cat.rect.x=20
    cat.rect.y=250
    M1.rect.y = randrange(81, 100, 50)
    M1.rect.x = LARGURA - randrange(30, 290, 90)
    M2.rect.y = randrange(81, 100, 50)
    M2.rect.x = LARGURA - randrange(30, 290, 90)
    M3.rect.y = randrange(81, 100, 50)
    M3.rect.x = LARGURA - randrange(30, 290, 90)
    M4.rect.y = randrange(81, 100, 50)
    M4.rect.x = LARGURA - randrange(30, 290, 90)
    Col=False
    catDestruido=False
    Mega_Bullets=0
    w=0
    h=0
    Mega_On=False
    runSong=False
    p=False
    Loop=0
    M1.reset()
    M2.reset()
    M3.reset()
    M4.reset()
    N_Wave=1
    CONT=0
    o=1
    runSong=False
    P=0
    if start_music == True and runSong == False:
        a.runSong(True)
        runSong == True


def song(start_music):
    if start_music == True:
        start_music=False
        runSong=False
    else:start_music=True

def tema(Tm):
    if Tm==False:Tm=True
    else:Tm=False

def quit():
    run = False
    EndGame = False