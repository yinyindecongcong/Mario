import pygame as pg
import config as c, resource

class Pole_ball(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image_sheet = resource.GFX['tile_set']
        self.image = self.get_image(228, 120, 8, 8)
        self.rect = self.image.get_rect()
        self.rect.centerx, self.rect.bottom = x, y

    def get_image(self, x, y, width, height):
        image = pg.Surface((width, height))
        image.blit(self.image_sheet, (0,0), (x, y, width, height))
        image.set_colorkey(c.BLACK)
        rect = image.get_rect()
        return pg.transform.scale(image, (int(rect.width * c.BRICK_SIZE_MULTIPLIER),
                                          int(rect.height * c.BRICK_SIZE_MULTIPLIER)))

class Flag(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image_sheet = resource.GFX['item_objects']
        self.image = self.get_image(128, 32, 16, 16)
        self.rect = self.image.get_rect()
        self.rect.right, self.rect.y = x, y
        self.state = c.STILL

    def get_image(self, x, y, width, height):
        image = pg.Surface((width, height))
        image.blit(self.image_sheet, (0,0), (x, y, width, height))
        image.set_colorkey(c.BLACK)
        rect = image.get_rect()
        return pg.transform.scale(image, (int(rect.width * c.BRICK_SIZE_MULTIPLIER),
                                          int(rect.height * c.BRICK_SIZE_MULTIPLIER)))

    def update(self):
        if self.state == c.MOVE:
            self.rect.y += 5
            if self.rect.bottom >= 485:
                self.state = c.BOTTOM_OF_POLE

class Pole(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pg.Surface((1, 1))
        self.image.fill((140, 214, 0))
        self.image = pg.transform.scale(self.image, (5, 397))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
