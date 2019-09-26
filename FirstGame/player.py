import pygame

class Player:
    def __init__(self,surface, x,y,width,height):
        self.surface = surface
        self.health = 100
        self.x = x
        self.y = y
        self.surface_width = width
        self.surface_height = height
        self.animation_count = 0
        self.vel = 5
        self.recheight = 60
        self.recwidth = 40


    def draw(self):
        """
        :param surface:
        :return: None

        self.animation_count +=1
        self.img = self.imges[self.animation_count]
        if self.animation_count >=len(self.imgs):
            self.animation_count=0
        """
        pygame.draw.rect(self.surface, (255, 0, 0), (self.x, self.y, self.recwidth, self.recheight))
        self.movement()


    def movement(self):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and self.x > self.vel:
            self.x -= self.vel
        if keys[pygame.K_RIGHT] and self.x < self.surface_width - self.recwidth - self.vel:
            self.x += self.vel
        if keys[pygame.K_UP] and self.y > self.vel:
            self.y -= self.vel
        if keys[pygame.K_DOWN] and self.y < self.surface_height - self.recheight - self.vel:
            self.y += self.vel
