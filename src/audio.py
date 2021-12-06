import os
import dist
import pygame

pygame.init()
print("Audio OK")

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

def runSong(x):
    if x == True:
        pygame.mixer.music.load(os.path.join(diretorio_sons,'music.mp3'))
        pygame.mixer.music.play(-1)