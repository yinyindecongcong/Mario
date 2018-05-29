import pygame as pg
import config as c, resource
from component import coin, powerup

class Stone(pg.sprite.Sprite):
    def __init__(self, x, y, content=None, group=None):
        super().__init__()
        self.image_sheet = resource.GFX['tile_set']
        self.setup_frames()  # setup frames
        self.frame_index = 0
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
        self.rest_height = y
        self.state = c.RESTING
        self.y_v = 0
        self.gravity = 1.2
        self.content = content
        self.group = group
        self.timer = 0
        self.current_time = 0

    def get_image(self, x, y, width, height):
        image = pg.Surface((width, height))
        image.blit(self.image_sheet, (0,0), (x, y, width, height))
        image.set_colorkey(c.BLACK)
        rect = image.get_rect()
        return pg.transform.scale(image, (int(rect.width * c.BRICK_SIZE_MULTIPLIER),
                                          int(rect.height * c.BRICK_SIZE_MULTIPLIER)))

    def update(self, game_info):
        '''update based on brick state'''
        self.current_time = game_info[c.CURRENT_TIME]
        if self.state == c.RESTING:
            self.resting()
        if self.state == c.BUMPED:
            self.bump()
        elif self.state == c.USELESS:
            self.useless()

    def collide(self, score_group):
        '''call when clllision happened, score_group for create coin'''
        pass

    def resting(self):
        '''call when nothing happened'''
        pass

    def bump(self):
        '''call to make animation after collision '''
        pass

    def useless(self):
        pass

class Brick(Stone):
    '''bricks that could be destroyed, which may hide coins or invincible star'''
    def __init__(self, x, y, content = None, group = None):
        super().__init__(x, y, content, group)
        self.coins = 6 if content == c.SIXCOINS else 0
        self.powerup_in_box = True

    def setup_frames(self):
        self.frames = []
        self.frames.append(self.get_image(16, 0, 16, 16))
        self.frames.append(self.get_image(432, 0, 16, 16))

    def bump(self):
        self.rect.y += self.y_v
        self.y_v += self.gravity
        if self.rect.y >= self.rest_height + 5:
            self.rect.y = self.rest_height
            if self.content == c.STAR or (self.content == c.SIXCOINS and self.coins == 0):
                self.state = c.USELESS
            else:
                self.state = c.RESTING

    def collide(self, score_group):
        '''call when collision happened, determine the brick's behavior based on its state'''
        self.y_v = -6
        self.state = c.BUMPED #change state into bump to animation
        if self.content == c.SIXCOINS:
            if self.coins > 0:
                self.group.add(coin.Coin(self.rect.centerx, self.rect.y, score_group))
                self.coins -= 1
        elif self.content == c.STAR and self.powerup_in_box:
            self.group.add(powerup.Star(self.rect.centerx, self.rect.y, c.STAR))
            self.powerup_in_box = False

    def useless(self):
        self.frame_index = 1
        self.image = self.frames[self.frame_index]

class Coin_box(Stone):
    def __init__(self, x, y, content = None, group = None):
        super().__init__(x, y, content, group)
        self.content = content

    def setup_frames(self):
        self.frames = []
        self.frames.append(self.get_image(384, 0, 16, 16))
        self.frames.append(self.get_image(400, 0, 16, 16))
        self.frames.append(self.get_image(416, 0, 16, 16))
        self.frames.append(self.get_image(432, 0, 16, 16))

    def collide(self, score_group):
        self.y_v = -6
        self.state = c.BUMPED  # change state into bump to animation
        if self.content == c.COIN:
            self.group.add(coin.Coin(self.rect.centerx, self.rect.y, score_group))
        elif self.content == c.MUSHROOM:
            self.group.add(powerup.Mushroom(self.rect.centerx, self.rect.y, c.MUSHROOM))
        elif self.content == c.LIFE_MUSHROOM:
            self.group.add(powerup.LifeMushroom(self.rect.centerx, self.rect.y, c.LIFE_MUSHROOM))
        elif self.content == c.FIREFLOWER:
            self.group.add(powerup.FireFlower(self.rect.centerx, self.rect.y, c.FIREFLOWER))

    def resting(self):
        '''flushing coin box'''
        if self.current_time - self.timer > 200:
            self.frame_index = (self.frame_index + 1) % 3
            self.timer = self.current_time
            self.image = self.frames[self.frame_index]

    def bump(self):
        self.rect.y += self.y_v
        self.y_v += self.gravity
        if self.rect.y >= self.rest_height + 5:
            self.rect.y = self.rest_height
            self.state = c.USELESS
            if self.state == c.MUSHROOM:
                pass
            elif self.state == c.FIREFLOWER:
                pass
            elif self.state == c.LIFE_MUSHROOM:
                pass
        self.frame_index = 3
        self.image = self.frames[self.frame_index]

    def set_content(self, content):
        self.content = content

class Broken_brick(pg.sprite.Sprite):
    '''brick pieces when brick is broken, which just need to fly out to screen'''
    def __init__(self, x, y, x_v, y_v):
        super().__init__()
        self.image_sheet = resource.GFX['item_objects']
        self.image = self.get_image(68, 20, 8, 8)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
        self.x_v, self.y_v = x_v, y_v
        self.gravity = 0.8

    def get_image(self, x, y, width, height):
        image = pg.Surface((width, height))
        image.blit(self.image_sheet, (0,0), (x, y, width, height))
        image.set_colorkey(c.BLACK)
        rect = image.get_rect()
        return pg.transform.scale(image, (int(rect.width * c.BRICK_SIZE_MULTIPLIER),
                                          int(rect.height * c.BRICK_SIZE_MULTIPLIER)))

    def update(self):
        self.rect.x += self.x_v
        self.rect.y += self.y_v
        self.y_v += self.gravity
        if self.rect.y > c.SCREEN_HEIGHT:
            self.kill()



