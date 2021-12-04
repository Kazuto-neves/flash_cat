import pygame
import sprites as spr
from random import *
import uteis as u

class Mouse(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.s=11
        self.image = spr.sprite_sheet.subsurface((self.s*520, 0), (514,407))
        self.image = pygame.transform.scale(self.image, (int(28*3),int(20*3)))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.y = randrange(81, 100, 50)
        self.rect.x = u.LARGURA - randrange(30, 290, 90)
        self.x=self.rect.x
        self.y=self.rect.y
        self.v=10
        self.cont=0
        self.w=1
        self.p=0


    def pos (self,x,y):
        self.crach=True
        self.s=12
        self.rect.x=x
        self.rect.y =y

    def esp (self,x):
        if x == 0:self.rect.x+=20
        else: self.rect.y+=20

    def lv (self,x):
        if x == 1:self.v=10
        elif x == 2:self.v=15
        elif x == 3:self.v=20

    def crash(self):
        self.p+=1
        self.cont+=1

    def pt (self):return self.p

    def reset(self):
        self.p=0
        self.cont=0


    def update(self):
        if self.cont < 500:
            if self.rect.topright[0] < 0:
                self.rect.x = u.LARGURA
                self.rect.y = randrange(81, 285, 50)
                self.cont+=1
        elif self.cont == 50:
            self.cont =0
            self.v+=(self.v/2)
        self.rect.x -= self.v
        self.x=self.rect.x
        self.y=self.rect.y  
        if self.rect.y == 82:self.rect.y += 20
        elif self.rect.y == 284:self.rect.y -= 10