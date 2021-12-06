import pygame
import telas as t
import uteis as u
import cat as c
import Back as b
import mouse as m
import cloud as cl
import game as g

todas_as_sprites = pygame.sprite.Group()
cat = c.Cat()
back = b.Back()
todas_as_sprites.add(back)
todas_as_sprites.add(cat)

for i in range(3):
    cloud = cl.Cloud()
    todas_as_sprites.add(cloud)

mouse1 = m.Mouse()
mouse2 = m.Mouse()
mouse3 = m.Mouse()
mouse4 = m.Mouse()

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

def game_loop(lv,start):
    global colidiu
    global bullets
    LV=lv
    g.game(u.colidiu,u.bullets,relogio,t.tela,u.ColorW,c.cat.MoveU,c.cat.MoveD,c.cat.MoveL,c.cat.MoveR,cat.wreck_start,cat.wrecked,cat,grupo_obstaculos,u.ColorY,todas_as_sprites,mouse1,mouse2,mouse3,mouse4,u.x,u.y,u.game_over,grupo_oM1,grupo_oM2,grupo_oM3,grupo_oM4,u.colidiuM,u.LV,u.run,cloud,back,start,u.Tm,u.Mega,u.w,u.h,u.Mega_On,u.p,u.r,u.l,u.N,u.cont,u.Q,u.V,u.up,u.Vup)

t.Plot(u.m,u.Tm)

