import pygame
import os
import sprites as spr

back = pygame.image.load(os.path.join(spr.diretorio_imagens,'back.png')).convert_alpha()

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