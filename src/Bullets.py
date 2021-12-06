import pygame
from random import *
import audio as a
import uteis as u

pygame.init()

def fire(catINdetruct,catDestruido,Screen,ColorY,bullets,x,y,Mega_On,w,h,Q_Boom,V_Boom):
    if not catINdetruct and not catDestruido:
        if Mega_On == False:
            for draw_bullet in bullets:
                if Q_Boom==1:pygame.draw.rect(Screen, ColorY, (draw_bullet[0]+90, draw_bullet[1]+20, 10, 10))
                elif Q_Boom==2:
                    pygame.draw.rect(Screen, ColorY, (draw_bullet[0]+90, draw_bullet[1]+20, 10, 10))
                    pygame.draw.rect(Screen, ColorY, (draw_bullet[0]+90, draw_bullet[1], 10, 10))
                else:
                    pygame.draw.rect(Screen, ColorY, (draw_bullet[0]+90, draw_bullet[1]+20, 10, 10))
                    pygame.draw.rect(Screen, ColorY, (draw_bullet[0]+90, draw_bullet[1], 10, 10))
                    pygame.draw.rect(Screen, ColorY, (draw_bullet[0]+90, draw_bullet[1]-20, 10, 10))
                y=draw_bullet[1]
            for move_bullet in range(len(bullets)):
                bullets[move_bullet][0] += (V_Boom+20)
                x=move_bullet
            for del_bullet in bullets:
                if del_bullet[0] >= 640:bullets.remove(del_bullet)
        else:
            for draw_bullet in bullets:
                pygame.draw.rect(Screen, ColorY, (draw_bullet[0]+90, draw_bullet[1]+20, w, h))
                y=draw_bullet[1]
            for move_bullet in range(len(bullets)):
                bullets[move_bullet][0] += (V_Boom+0.1)
                x=move_bullet
            for del_bullet in bullets:
                if del_bullet[0] >= 640:bullets.remove(del_bullet)

def boom(catINdetruct,catDestruido,EndGame,bullets,M1,M2,M3,M4,Mega_On,CONT):
    if not catINdetruct and not catDestruido and not EndGame:
        for cats in bullets:
            if M1.x < cats[0]+90 < M1.y and M1.x < cats[1]+40 < M1.y+100:
                bullets.remove(cats)
                M1.pos(u.LARGURA,randrange(81, 285, 50))
                M1.crash()
                CONT+=1
                a.explosion(Mega_On)
            elif M2.x < cats[0]+90 < M2.y and M2.x < cats[1]+40 < M2.y+100:
                bullets.remove(cats)
                M2.pos(u.LARGURA,randrange(81, 285, 50))
                M2.crash()
                CONT+=1
                a.explosion(Mega_On)
            elif M3.x < cats[0]+90 < M3.y and M3.x < cats[1]+40 < M3.y+100:
                bullets.remove(cats)
                M3.pos(u.LARGURA,randrange(81, 285, 50))
                M3.crash()
                CONT+=1
                a.explosion(Mega_On)
            elif M4.x < cats[0]+90 < M4.y and M4.x < cats[1]+40 < M4.y+100:
                bullets.remove(cats)
                M4.pos(u.LARGURA,randrange(81, 285, 50))
                M4.crash()
                CONT+=1
                a.explosion(Mega_On)
            elif M1.x < cats[0]+100 < M1.x+70 and M1.y < cats[1]+50 < M1.y+100:
                bullets.remove(cats)
                M1.pos(u.LARGURA,randrange(81, 285, 50))
                M1.crash()
                CONT+=1
                a.explosion(Mega_On)
            elif M2.x < cats[0]+100 < M2.x+70 and M2.y < cats[1]+50 < M2.y+100:
                bullets.remove(cats)
                M2.pos(u.LARGURA,randrange(81, 285, 50))
                M2.crash()
                CONT+=1
                a.explosion(Mega_On)
            elif M3.x < cats[0]+100 < M3.x+70 and M3.y < cats[1]+50 < M3.y+100:
                bullets.remove(cats)
                M3.pos(u.LARGURA,randrange(81, 285, 50))
                M3.crash()
                CONT+=1
                a.explosion(Mega_On)
            elif M4.x < cats[0]+100 < M4.x+70 and M4.y < cats[1]+50 < M4.y+100:
                bullets.remove(cats)
                M4.pos(u.LARGURA,randrange(81, 285, 50))
                M4.crash()
                CONT+=1
                a.explosion(Mega_On)