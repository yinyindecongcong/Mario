import pygame as pg
import config as c, resource

class Castle_flag(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image_sheet = resource.GFX['item_objects']
        self.image = self.get_image(129, 2, 14, 14)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x,y
        self.state = 'rise'
        self.y_v = -2
        self.end_height = y

    def get_image(self, x, y, width, height):
        image = pg.Surface((width, height))
        image.blit(self.image_sheet, (0,0), (x, y, width, height))
        image.set_colorkey(c.BLACK)
        rect = image.get_rect()
        return pg.transform.scale(image, (int(rect.width * 2.5), int(rect.height * 2.5)))

    def update(self):
        if self.state == 'rise':
            self.rect.y += self.y_v
            if self.rect.bottom <= self.end_height:
                self.state = 'end'