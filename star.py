import pygame
from pygame.sprite import Sprite

class Star(Sprite):
    def __init__(self, sky):
        super().__init__()
        self.screen = sky.screen
        # self.screen_rect = self.screen.get_rect()

        self.image = pygame.image.load("images/star1.jpg")
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
