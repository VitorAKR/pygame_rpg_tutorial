import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self,pos,groups,obstacle_sprites):
        super().__init__(groups)
        self.image = pygame.image.load('./graphics/test/player.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0,-26)

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

        self.hitbox.x += self.direction.x * speed
        #check for horizontal collisions
        self.collision('horizontal')
        self.hitbox.y += self.direction.y * speed
        #check for vertical collisions
        self.collision('vertical')
        #changing collisions for hitbox, but rectangle must follow the hitbox
        self.rect.center = self.hitbox.center

    #Collisions detectition:
    #1.Apply horizontal movement
    #2.Check horizontal (x) collisions
    #3.Apply vertical movement
    #4.Check vertical (y) collisions
    def collision(self, direction):
        if direction == 'horizontal':
            for sprite in self.obstacle_sprites:
                #Checking the hitbox of the sprite with the hitbox of the player 
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.x > 0: #player is moving to right
                        self.hitbox.right = sprite.hitbox.left
                    if self.direction.x < 0: #player is moving to left
                        self.hitbox.left = sprite.hitbox.right

        if direction == 'vertical':
            for sprite in self.obstacle_sprites:
                #Checking the hitbox of the sprite with the hitbox of the player 
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.y > 0: #player is moving down
                        self.hitbox.bottom = sprite.hitbox.top
                    if self.direction.y < 0: #player is moving up
                        self.hitbox.top = sprite.hitbox.bottom

    def update(self):
        self.input()
        self.move(self.speed)
