import pygame
from pygame.sprite import Sprite
class Star(Sprite):
    def __init__(self,star_dashboard):
        super().__init__()
        self.screen=star_dashboard.screen
        self.image=pygame.image.load('python/python_work/alien_invasion/images/alien.bmp')
        self.rect=self.image.get_rect()

        self.rect.x=self.rect.width
        self.rect.y=self.rect.height
        