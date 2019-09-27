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
        self.vel = 15
        self.recheight = 100
        self.recwidth = 60
        self.middleOfroom = 594
        self.jumpCount = 10
        self.isJump = False


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
        pygame.draw.rect(self.surface, (0, 255, 0), (self.x-20, self.y-40, self.health, 20))

        self.movement()


    def movement(self):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and self.x > self.vel:
            self.x -= self.vel
        if keys[pygame.K_RIGHT] and self.x < self.surface_width - self.recwidth - self.vel:
            self.x += self.vel

        if not self.isJump:

            if keys[pygame.K_UP] and self.y > self.vel and self.y > self.middleOfroom - self.recheight/2:
                self.y -= self.vel

            if keys[pygame.K_DOWN] and self.y < self.surface_height - self.recheight - self.vel:
                self.y += self.vel

            if keys[pygame.K_SPACE]:
                self.isJump = True

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