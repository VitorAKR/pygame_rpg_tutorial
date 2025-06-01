import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self,pos,groups,obstacle_sprites):
        super().__init__(groups)
        self.image = pygame.image.load('./graphics/test/player.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)

		#use a vector to set moves to our player based on keys entries and multiplies with some of speed
        self.direction = pygame.math.Vector2()
        self.speed = 5

        self.obstacle_sprites = obstacle_sprites

    def input(self):
        #get all the keys pressed
        keys = pygame.key.get_pressed()

        #setting Y direction
        if keys[pygame.K_UP]:
            self.direction.y = -1
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
        else:
            self.direction.y = 0

        #setting X direction
        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0

    def move(self,speed):
        #normalizing the speed applied in 2 directions (trigonometry), by changing the lenght of a vector(magnitude) to 1
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        self.rect.x += self.direction.x * speed
        #check for horizontal collisions
        self.collision('horizontal')
        self.rect.y += self.direction.y * speed
        #check for vertical collisions
        self.collision('vertical')
		#self.rect.center += self.direction * speed

    #Collisions detectition:
    #1.Apply horizontal movement
    #2.Check horizontal (x) collisions
    #3.Apply vertical movement
    #4.Check vertical (y) collisions
    def collision(self, direction):
        if direction == 'horizontal':
            for sprite in self.obstacle_sprites:
                #Checking the rectangle of the sprite with the rectangle of the player 
                if sprite.rect.colliderect(self.rect):
                    if self.direction.x > 0: #player is moving to right
                        self.rect.right = sprite.rect.left
                    if self.direction.x < 0: #player is moving to left
                        self.rect.left = sprite.rect.right

        if direction == 'vertical':
            for sprite in self.obstacle_sprites:
                #Checking the rectangle of the sprite with the rectangle of the player 
                if sprite.rect.colliderect(self.rect):
                    if self.direction.y > 0: #player is moving down
                        self.rect.bottom = sprite.rect.top
                    if self.direction.y < 0: #player is moving up
                        self.rect.top = sprite.rect.bottom

    def update(self):
        self.input()
        self.move(self.speed)
