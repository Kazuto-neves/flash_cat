import os
import dist
import pygame
import sprites as spr
import telas as t

diretorio_sons = os.path.join(dist.diretorio_principal, 'audio')

def tiro(m):
    if m == True:
        ti=pygame.mixer.Sound(os.path.join(diretorio_sons,'kill.ogg'))
        ti.play()

def Mtiro(m):
    if m == True:
        mt=pygame.mixer.Sound(os.path.join(diretorio_sons,'Mkill.ogg'))
        mt.play()

def explosion(m):
    if m == True:
       exp=pygame.mixer.Sound(os.path.join(diretorio_sons,'explosion.ogg'))
       exp.set_volume(0.02)
       exp.play()

def music(m):
    if m == True:
        pygame.mixer.music.load(os.path.join(diretorio_sons,'music.mp3'))
        pygame.mixer.music.play(-1)

def menu_audio(x):
        if x == False:ss = pygame.image.load(os.path.join(spr.diretorio_imagens, 'Ssom.png')).convert_alpha()
        else:ss = pygame.image.load(os.path.join(spr.diretorio_imagens, 'Csom.png')).convert_alpha()
        t.tela.blit(ss, [4, 304,20,20])

def runSong(x):
    if x == True:
        pygame.mixer.music.load(os.path.join(diretorio_sons,'music.mp3'))
        pygame.mixer.music.play(-1)