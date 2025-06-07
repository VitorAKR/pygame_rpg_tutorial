import pygame
from settings import *

class Tile(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load('./graphics/test/rock.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        #creating a short box inside the rectangle that has -5px on top and bottom, but preserves center position
        self.hitbox = self.rect.inflate(0,-10)
