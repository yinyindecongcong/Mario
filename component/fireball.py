import pygame as pg
import config as c, resource

class FireBall(pg.sprite.Sprite):
    def __init__(self, x, y, facing_right, name=c.FIREBALL):
        super().__init__()
        self.image_sheet = resource.GFX['item_objects']
        self.setup_frames()
        self.facing_right = facing_right
        self.x_v = 12 if facing_right else -12
        self.y_v = 1
        self.gravity = 1
        self.current_time, self.timer = 0, 0
        self.state = c.FLYING
        self.frame_index = 0
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
        self.name = name
    def setup_frames(self):
        '''setup images for animation'''
        self.frames = []
        self.frames.append(self.get_image(96, 144, 8, 8))       #flying 1 [0]
        self.frames.append(self.get_image(104, 144, 8, 8))      #flying 2 [1]
        self.frames.append(self.get_image(96, 152, 8, 8))       #flying 3 [2]
        self.frames.append(self.get_image(104, 152, 8, 8))      #flying 4 [3]
        self.frames.append(self.get_image(112, 144, 16, 16))    #exploding 1 [4]
        self.frames.append(self.get_image(112, 160, 16, 16))    #exploding 2 [5]
        self.frames.append(self.get_image(112, 176, 16, 16))    #exploding 3 [6]

    def get_image(self, x, y, width, height):
        image = pg.Surface((width, height))
        image.blit(self.image_sheet, (0, 0), (x, y, width, height))
        image.set_colorkey(c.BLACK)
        rect = image.get_rect()
        return pg.transform.scale(image, (int(rect.width * 2.5), int(rect.height * 2.5)))

    def update(self, game_info):
        self.current_time = game_info[c.CURRENT_TIME]
        self.animation()

    def animation(self):
        if self.state == c.FLYING or self.state == c.BOUNCING:
            if self.current_time - self.timer > 200:
                self.timer = self.current_time
                self.frame_index = (self.frame_index + 1) % 4
                self.image = self.frames[self.frame_index]
        elif self.state == c.EXPLODING:
            if self.current_time - self.timer > 50:
                if self.frame_index < 6:
                    self.timer = self.current_time
                    self.frame_index += 1
                    self.image = self.frames[self.frame_index]
                else:
                    self.kill()

    def explode(self):
        '''call when collide with collision'''
        self.frame_index = 4
        centerx = self.rect.centerx
        self.image = self.frames[self.frame_index]
        self.rect.centerx = centerx
        self.state = c.EXPLODING

    def bounce(self):
        self.y_v = -8
        self.state = c.BOUNCING