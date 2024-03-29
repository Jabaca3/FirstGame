import pygame
import os
from FirstGameGit.FirstGame.player import Player

"""
Joseph Baca
Started: 9/26/2019
Last Updated: 10/18/2019

"""

class Game:
    def __init__(self):
        self.x = 50
        self.y = 50
        self.width = 1920
        self.height = 1080
        self.animation_count = 0
        self.health = 1
        self.move_count = 0
        self.move_dis = 0
        self.img = None
        self.surface = pygame.display.set_mode((self.width, self.height))
        self.player = Player(self.surface, 114, 699, self.width, self.height)
        self.bg = pygame.image.load(os.path.join("images","office.png"))
        #self.bg = pygame.transform.scale(self.bg, (self.width, self.height))
        self.clicks = [] #remove


    def run(self):
        run = True
        clock = pygame.time.Clock()

        while run:
            clock.tick(120)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                pos = pygame.mouse.get_pos()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.clicks.append(pos)
                    print(pos)

            self.draw()
            self.surface.fill((0, 0, 0))
        pygame.quit()


    def draw(self):
        self.surface.blit(self.bg, (0,0))
        self.player.draw()
        for p in self.clicks:
            pygame.draw.circle(self.surface, (255,0,0), (p[0], p[1]), 5, 0)
        pygame.display.update()

    def collide_roof_floor(self, X, Y):
        return False

game = Game()
game.run()