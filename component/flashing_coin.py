import pygame as pg
import config as c, resource

class Coin():
    '''
    flushing coin to blink, showing on top of screen;
    switch images based on time interval to achieve the blinking effect
    '''
    def __init__(self, x, y):
        self.image_sheet = resource.GFX['item_objects']
        self.images = []
        self.create_images(self.images)
        self.image = self.images[0]
        self.image_index = 0
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
        self.time = 0

    def create_images(self, images):
        images.append(self.get_image(1, 160, 5, 8))
        images.append(self.get_image(9, 160, 5, 8))
        images.append(self.get_image(17, 160, 5, 8))

    def get_image(self, x, y, width, height):
        image = pg.Surface([width, height])
        image.blit(self.image_sheet, (0, 0), (x, y, width, height)) #draw img onto image
        image.set_colorkey(c.BLACK) #创建的surface对象背景色为黑色
        image = pg.transform.scale(image, (int(width * 2.69), int(height * 2.69)))
        return image

    def update(self, current_time):
        if self.image_index == 0:
            if current_time - self.time > 375:
                self.image_index = 1
                self.time = current_time
        elif current_time - self.time > 125:
            self.image_index = (self.image_index + 1) % 3
            self.time = current_time
        self.image = self.images[self.image_index]
