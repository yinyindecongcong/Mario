import pygame as pg

class Checkpoint(pg.sprite.Sprite):
    '''invisible check point to check if elements like enemies should appear'''
    def __init__(self, x, name, y = 0, width = 10, height = 600):
        super().__init__()
        self.image = pg.Surface((width, height))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
        self.name = name