import os
import dist
import pygame

pygame.init()

diretorio_imagens = os.path.join(dist.diretorio_principal, 'image')

sprite_sheet = pygame.image.load(os.path.join(diretorio_imagens, 'sprite.png')).convert_alpha()