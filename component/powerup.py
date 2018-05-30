import pygame as pg
import config as c, resource

class Powerup(pg.sprite.Sprite):
    def __init__(self, centerx, y, name):
        '''base class for powerup like mushroom\flower\star'''
        super().__init__()
        self.image_sheet = resource.GFX['item_objects']
        self.frames = []
        self.setup_frames()
        self.frame_index = 0
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.centerx, self.rect.y = centerx, y - 5
        self.name = name
        self.state = c.UP #moving up
        self.facing_right = True
        self.box_height = y
        self.x_v, self.y_v = 3, 0
        self.gravity = 1
        self.max_y_v = 8

    def get_image(self, x, y, width, height):
        image = pg.Surface((width, height))
        image.blit(self.image_sheet, (0,0), (x, y, width, height))
        image.set_colorkey(c.BLACK)
        rect = image.get_rect()
        return pg.transform.scale(image, (int(rect.width * 2.5), int(rect.height * 2.5)))

    def update(self, game_info):
        pass

    def moving_up(self):
        self.rect.y -= 0.15
        if self.rect.bottom <= self.box_height:
            self.rect.bottom = self.box_height
            self.state = c.SLIDE

    def slide(self):
        self.x_v = 3 if self.facing_right else -3

    def falling(self):
        self.y_v = min(self.y_v + self.gravity, self.max_y_v)

class Mushroom(Powerup):
    def __init__(self, centerx, y, name):
        super().__init__(centerx, y, name)

    def setup_frames(self):
        self.frames.append(self.get_image(0, 0, 16, 16))

    def update(self, game_info):
        if self.state == c.UP:
            self.moving_up()
        elif self.state == c.SLIDE:
            self.slide()
        elif self.state == c.FALL:
            self.falling()

class LifeMushroom(Mushroom):
    def __init__(self, centerx, y, name):
        super().__init__(centerx, y, name)

    def setup_frames(self):
        self.frames.append(self.get_image(16, 0, 16, 16))

class FireFlower(Powerup):
    def __init__(self, centerx, y, name):
        super().__init__(centerx, y, name)
        self.current_time = 0
        self.timer = 0

    def setup_frames(self):
        self.frames.append(self.get_image(0, 32, 16, 16))
        self.frames.append(self.get_image(16, 32, 16, 16))
        self.frames.append(self.get_image(32, 32, 16, 16))
        self.frames.append(self.get_image(48, 32, 16, 16))

    def update(self, game_info):
        self.current_time = game_info[c.CURRENT_TIME]
        if self.state == c.UP:
            self.moving_up()
        self.animation()

    def animation(self):
        if self.current_time - self.timer > 50:
            self.timer = self.current_time
            self.frame_index = (self.frame_index + 1) % 4
            self.image = self.frames[self.frame_index]

class Star(Powerup):
    def __init__(self, centerx, y, name):
        super().__init__(centerx, y, name)
        self.current_time = 0
        self.timer = 0

    def setup_frames(self):
        self.frames.append(self.get_image(1, 48, 15, 16))
        self.frames.append(self.get_image(17, 48, 15, 16))
        self.frames.append(self.get_image(33, 48, 15, 16))
        self.frames.append(self.get_image(49, 48, 15, 16))

    def update(self, game_info):
        self.current_time = game_info[c.CURRENT_TIME]
        if self.state == c.UP:
            self.moving_up()
        elif self.state == c.FALL:
            self.bounce()
        self.animation()

    def moving_up(self):
        self.rect.y -= 0.15
        if self.rect.bottom >= self.box_height:
            self.rect.bottom = self.box_height
            self.state = c.FALL
            self.y_v = -3

    def bounce(self):
        self.x_v = 4 if self.facing_right else -4
        self.y_v = min(self.y_v + self.gravity, self.max_y_v)

    def animation(self):
        if self.current_time - self.timer > 50:
            self.timer = self.current_time
            self.frame_index = (self.frame_index + 1) % 4
            self.image = self.frames[self.frame_index]


