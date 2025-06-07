import pygame
from settings import *
from tile import Tile
from player import Player
from debug import debug

class Level:
    def __init__(self):
        #get the display surface
        self.display_surface = pygame.display.get_surface()

        #sprite group setup
        self.visible_sprites = YSortCameraGroup()
        self.obstacle_sprites = pygame.sprite.Group()

        #sprite setup
        self.create_map()

    def create_map(self):
        for row_index,row in enumerate(WORLD_MAP):
            for col_index,col in enumerate(row):
                x = col_index * TILESIZE
                y = row_index * TILESIZE
                if col == 'X':
                    Tile((x,y),[self.visible_sprites,self.obstacle_sprites])
                if col == 'p':
                    #We're creating the player and giving the obstacle sprites for the collisions
                    self.player = Player((x,y),[self.visible_sprites],self.obstacle_sprites)

    def run(self):
        #update and draw the game
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()
		#debug(self.player.direction)


#This class will be a camera that sorts the sprites by the Y coordinates
class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):

        #general setup
        super().__init__()
        self.display_surface = pygame.display.get_surface()
		#getting half of width and height to have Player in the middle of the screen
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()

    def custom_draw(self,player):
        #getting offset
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        for sprite in self.sprites():
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image,offset_pos)
