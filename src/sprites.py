import os
import pygame
import Image as I

pygame.init()
print("Sprites OK")

sprite_sheet = pygame.image.load(os.path.join(I.diretorio_imagens, 'sprite.png')).convert_alpha()