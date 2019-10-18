import pygame
import os

class Player:
    def __init__(self,surface, x,y,width,height):
        self.surface = surface
        self.health = 100
        self.x = x
        self.y = y
        self.surface_width = width
        self.surface_height = height
        self.vel = 15
        self.recheight = 100
        self.recwidth = 60
        self.middleOfroom = 594
        self.jumpCount = 10
        self.isJump = False
        self.left = False
        self.right = False
        self.walkCount = 0

        self.standing = pygame.image.load(os.path.join("images/rwalk","rwalk1.png"))
        self.walkLeft = []
        self.walkRight = []

        for i in range(1,22):
            add_str = str(i)
            self.walkLeft.append(pygame.image.load(os.path.join("images/lwalk", "lwalk"+add_str+".png")))
            self.walkRight.append(pygame.image.load(os.path.join("images/rwalk", "rwalk"+add_str+".png")))



    def draw(self):

        if self.walkCount >= 21:
            self.walkCount=0
        if self.left:
            self.surface.blit(self.walkLeft[self.walkCount], (self.x, self.y))
            self.walkCount+=1
        elif self.right:
            self.surface.blit(self.walkRight[self.walkCount], (self.x, self.y))
            self.walkCount += 1
        else:
            self.surface.blit(self.standing, (self.x, self.y))

        pygame.display.update()


        #pygame.draw.rect(self.surface, (255, 0, 0), (self.x, self.y, self.recwidth, self.recheight)) #temp Player Rectangle
        pygame.draw.rect(self.surface, (0, 255, 0), (self.x-20, self.y-40, self.health, 20)) # health Bar

        self.movement()


    def movement(self):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and self.x > self.vel:
            self.x -= self.vel
            self.left = True
            self.right = False

        elif keys[pygame.K_RIGHT] and self.x < self.surface_width - self.recwidth - self.vel:
            self.x += self.vel
            self.left = False
            self.right = True
        else:
            self.left = False
            self.right = False
            self.walkCount = 0



        if not self.isJump:

            if keys[pygame.K_UP] and self.y > self.vel and self.y > self.middleOfroom - self.recheight/2:
                self.y -= self.vel

            if keys[pygame.K_DOWN] and self.y < self.surface_height - self.recheight - self.vel:
                self.y += self.vel

            if keys[pygame.K_SPACE]:
                self.isJump = True
                self.left = False
                self.right = False
                self.walkCount = 0

        else:
            if self.jumpCount >= -10:
                neg = 1

                if self.jumpCount < 0:
                    neg = -1

                self.y -= (self.jumpCount **2)/2 * neg
                self.jumpCount -= 1

            else:
                self.isJump = False
                self.jumpCount = 10


    def smallHit(self):
        self.health -=1
    def bigHit(self):
        self.health -=5