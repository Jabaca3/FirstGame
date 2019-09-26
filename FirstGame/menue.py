import pygame
import os
from FirstGameGit.FirstGame.player import Player

"""
Joseph Baca
9/26
Testing FirstGame commit
"""

class Game:
    def __init__(self):
        self.x = 50
        self.y = 50
        self.width = 1000
        self.height = 700
        self.animation_count = 0
        self.health = 1
        self.move_count = 0
        self.move_dis = 0
        self.img = None
        self.surface = pygame.display.set_mode((self.width, self.height))
        self.player = Player(self.surface, 50, 50, self.width, self.height)
        self.bg = pygame.image.load(os.path.join("images","bg.png"))
        self.bg = pygame.transform.scale(self.bg, (self.width, self.height))
        self.clicks = [] #remove


    def run(self):
        run = True
        clock = pygame.time.Clock()

        while run:
            clock.tick(60)
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