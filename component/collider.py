import pygame as pg

class Collider(pg.sprite.Sprite):
    '''invisible sprite that could be collided, like pipe, ground, etc'''
    def __init__(self, x, y, width, height, name = 'Collider'):
        super().__init__()
        self.name = name
        self.image = pg.Surface((width, height))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
        self.state = None