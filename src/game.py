import pygame
import audio as a
import uteis as u
import telas as t
import Bullets as B
from pygame.locals import *
from sys import exit

pygame.init()
pygame.mixer.init()

def game(Col,bullets,Time,Screen,ColorW,catMU,catMD,catML,catMR,catINdetruct,catDestruido,cat,group_obst,ColorY,ALL_Spr,M1,M2,M3,M4,x,y,EndGame,group_obst_Mouse1,group_obst_Mouse2,group_obst_Mouse3,group_obst_Mouse4,colidiu_Mouse,LV,run,cloud,back,start_music,Tm,Mega_Bullets,w,h,Mega_On,p,runSong,Loop,N_Wave,CONT,Q_Boom,V_Boom,up,Vup):
    o=1
    M1.lv(LV)
    M2.lv(LV)
    M3.lv(LV)
    M4.lv(LV)
    a.music(start_music)
    runSong=False
    P=0
    while run:
        Loop+=1
        while EndGame:
            if o == 1:
                t.go(P,start_music,Tm)
                pygame.mixer.music.pause()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        u.quit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            u.reset(Col,cat,M1,M2,M3,M4,EndGame,catDestruido,P,start_music)
                        if event.key == pygame.K_TAB:
                            u.song(start_music)
                            pygame.display.update()
                        if event.key == pygame.K_l:
                            u.tema(Tm)
                            pygame.display.update()
                        if event.key == pygame.K_ESCAPE:
                            u.quit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        X = pygame.mouse.get_pos()[0]
                        Y = pygame.mouse.get_pos()[1]
                        if X > 140 and Y > 140 and X < 290 and Y < 190:
                            u.reset(Col,cat,M1,M2,M3,M4,EndGame,catDestruido,P,start_music)
                        if x > 2 and y > 302 and x < 46 and y < 352:
                            u.song(start_music)
                            print("mudei")
                            pygame.display.update()
                        if x > 10 and y > 10 and x < 60 and y < 60:
                            u.tema(Tm)
                            pygame.display.update()
                        if X > 350 and Y > 140 and X < 500 and Y < 190:
                            u.quit()
            elif o == 2:
                t.pause(P,start_music,Tm)
                pygame.mixer.music.pause()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        u.quit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            run = True
                            EndGame = False
                            o=1
                            if start_music == True and runSong == False:
                                a.runSong(True)
                                runSong=True
                            if start_music == True or runSong == True:pygame.mixer.music.unpause()
                            #fire(catINdetruct,catDestruido,Screen,ColorY,bullets,x,y)
                        if event.key == pygame.K_F5:
                            u.pause(Col,cat,M1,M2,M3,M4,EndGame,catDestruido,P,start_music)
                        if event.key == pygame.K_TAB:
                            a.runSong(True)
                            pygame.display.update()
                        if event.key == pygame.K_l:
                            u.tema(Tm)
                            pygame.display.update()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        X = pygame.mouse.get_pos()[0]
                        Y = pygame.mouse.get_pos()[1]
                        if X > 140 and Y > 140 and X < 290 and Y < 190:
                            run = True
                            EndGame = False
                            o=1
                            if start_music == True and runSong == False:
                                a.runSong(True)
                                runSong=True
                            if start_music == True or runSong == True:pygame.mixer.music.unpause()
                            #fire(catINdetruct,catDestruido,Screen,ColorY,bullets,x,y)
                        if X > 350 and Y > 140 and X < 500 and Y < 190:
                            u.pause(Col,cat,M1,M2,M3,M4,EndGame,catDestruido,P,start_music)
                        if x > 2 and y > 302 and x < 46 and y < 352:
                            a.runSong(True)
                            print("mudei")
                            pygame.display.update()
                        if x > 10 and y > 10 and x < 60 and y < 60:
                            u.tema(Tm)
                            pygame.display.update()
            else:
                t.Power_ups(P,start_music,Tm,Q_Boom,up,Vup)
                pygame.mixer.music.pause()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if Vup == up:
                        Vup=Vup*3 
                        if event.key == pygame.K_1:
                            run = True
                            EndGame = False
                            o=1
                            if Q_Boom<=3:Q_Boom+=1
                            if start_music == True and runSong == False:
                                a.runSong()
                                runSong=True
                            if start_music == True:pygame.mixer.music.unpause()
                            if start_music == True and runSong == True:pygame.mixer.music.unpause()
                        if event.key == pygame.K_2:
                            run = True
                            EndGame = False
                            o=1
                            V_Boom+=1
                            if start_music == True and runSong == False:
                                a.runSong()
                                runSong=True
                            if start_music == True:pygame.mixer.music.unpause()
                            if start_music == True and runSong == True:pygame.mixer.music.unpause()
                    else:
                        if event.key == pygame.K_SPACE:
                            run = True
                            EndGame = False
                            o=1
                            if start_music == True and runSong == False:
                                a.runSong()
                                runSong=True
                            if start_music == True:pygame.mixer.music.unpause()
                            if start_music == True and runSong == True:pygame.mixer.music.unpause()
                    if event.key == pygame.K_TAB:
                        u.song(start_music)
                        pygame.display.update()
                    if event.key == pygame.K_l:
                        u.tema(Tm)
                        pygame.display.update()
                        
                    if event.key == pygame.K_ESCAPE:pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x = pygame.mouse.get_pos()[0]
                    y = pygame.mouse.get_pos()[1]
                    if Vup == up:
                        Vup=Vup*3
                        if x > 140 and y > 140 and x < 290 and y < 190:
                            run = True
                            EndGame = False
                            o=1
                            if Q_Boom<=3:Q_Boom+=1
                            if start_music == True and runSong == False:
                                a.runSong()
                                runSong=True
                            if start_music == True:pygame.mixer.music.unpause()
                            if start_music == True and runSong == True:pygame.mixer.music.unpause()
                        if x > 350 and y > 140 and x < 500 and y < 190:
                            run = True
                            EndGame = False
                            o=1
                            V_Boom+=1
                            if start_music == True and runSong == False:
                                a.runSong()
                                runSong=True
                            if start_music == True:pygame.mixer.music.unpause()
                            if start_music == True and runSong == True:pygame.mixer.music.unpause()
                    else:
                        if x > 250 and y > 170 and x < 380 and y < 195:
                            run = True
                            EndGame = False
                            o=1
                            if start_music == True and runSong == False:
                                a.runSong()
                                runSong=True
                            if start_music == True:pygame.mixer.music.unpause()
                            if start_music == True and runSong == True:pygame.mixer.music.unpause()
                    if x > 2 and y > 302 and x < 46 and y < 352:
                        u.song(start_music)
                        print("mudei")
                        pygame.display.update()
                    if x > 10 and y > 10 and x < 60 and y < 60:
                        u.tema(Tm)
                        pygame.display.update()
                    if x > 510 and y > 0 and x < 640 and y < 25:pygame.quit()       
        Time.tick(30)
        Screen.fill(ColorW)
        ALL_Spr.draw(Screen)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_w or event.key == K_UP:catMU(True,start_music)
                if event.key == K_s or event.key == K_DOWN:catMD(True,start_music)
                if event.key == K_a or event.key == K_LEFT:catML(True,start_music)
                if event.key == K_d or event.key == K_RIGHT:catMR(True,start_music)
                if event.key == K_p:
                    EndGame=True
                    o=2
                if event.key == K_SPACE:
                    if not catINdetruct:bullets.append([cat.x, cat.y]) 
                    a.tiro(start_music)
                    if Mega_Bullets <=100:Mega_Bullets+=1
                    else:Mega_Bullets
                    w=(6.4*Mega_Bullets)/2
                    h=(3.6*Mega_Bullets)/2
                if event.key == K_q:
                    if Mega_Bullets>=50:
                        Mega_On=True
                        a.Mtiro(start_music)
                        Mega_Bullets=0
                if event.key == K_u:
                    EndGame=True
                    o=3
            elif event.type == KEYUP:
                if event.key == K_w or event.key == K_UP:catMU(False,start_music)
                if event.key == K_s or event.key == K_DOWN:catMD(False,start_music)
                if event.key == K_a or event.key == K_LEFT:catML(False,start_music)
                if event.key == K_d or event.key == K_RIGHT:catMR(False,start_music)
                if event.key == K_q:Mega_On=False

        colisoes = pygame.sprite.spritecollide(cat, group_obst, False, pygame.sprite.collide_mask)
        colM1 = pygame.sprite.spritecollide(M1, group_obst_Mouse1, False, pygame.sprite.collide_mask)
        colM2 = pygame.sprite.spritecollide(M2, group_obst_Mouse2, False, pygame.sprite.collide_mask)
        colM3 = pygame.sprite.spritecollide(M3, group_obst_Mouse3, False, pygame.sprite.collide_mask)
        colM4 = pygame.sprite.spritecollide(M4, group_obst_Mouse4, False, pygame.sprite.collide_mask)

        t.placar(P,Mega_Bullets,N_Wave,up,Vup)
        if M1.pt() > P:P+=M1.pt()
        elif M2.pt() > P:P+=M2.pt()
        elif M3.pt() > P:P+=M3.pt()
        elif M4.pt() > P:P+=M4.pt()
        B.fire(catINdetruct,catDestruido,Screen,ColorY,bullets,x,y,Mega_On,w,h,Q_Boom,V_Boom)
        B.boom(catINdetruct,catDestruido,EndGame,bullets,M1,M2,M3,M4,Mega_On,CONT)


#        if colM1 and colidiu_Mouse == False:colidiu_Mouse = True
#        if colidiu_Mouse == True:
#            run=randrange(1, 2)
#            colidiu_Mouse=False
#            M1.esp(run)

#        if colM2 and colidiu_Mouse == False:colidiu_Mouse = True
#        if colidiu_Mouse == True:
#            run=randrange(1, 2)
#            colidiu_Mouse=False
#            M2.esp(run)

#        if colM3 and colidiu_Mouse == False:colidiu_Mouse = True
#        if colidiu_Mouse == True:
#            run=randrange(1, 2)
#            colidiu_Mouse=False
#            M3.esp(run)
        
#        if colM4 and colidiu_Mouse == False:colidiu_Mouse = True
#        if colidiu_Mouse == True:
#            run=randrange(1, 2)
#            colidiu_Mouse=False
#            M4.esp(run)
        if colisoes and Col == False:
            Col = True
            catDestruido = True
        if Col == True:EndGame=True
        else:
            if CONT < 500:
                CONT+=1
                ALL_Spr.update()
            else:
                ALL_Spr.update()
                up+=100
                N_Wave+=1
                CONT=0

        pygame.display.flip()

"""todas_as_sprites = pygame.sprite.Group()
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
    game(u.colidiu,u.bullets,relogio,t.tela,u.ColorW,c.cat.MoveU,c.cat.MoveD,c.cat.MoveL,c.cat.MoveR,cat.wreck_start,cat.wrecked,cat,grupo_obstaculos,u.ColorY,todas_as_sprites,mouse1,mouse2,mouse3,mouse4,u.x,u.y,u.game_over,grupo_oM1,grupo_oM2,grupo_oM3,grupo_oM4,u.colidiuM,u.LV,u.run,cloud,back,start,u.Tm,u.Mega,u.w,u.h,u.Mega_On,u.p,u.r,u.l,u.N,u.cont,u.Q,u.V,u.up,u.Vup)

t.Plot(u.m,u.Tm)"""