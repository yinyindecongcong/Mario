import pygame as pg
import config as c, resource
from component import score
class Coin(pg.sprite.Sprite):
    def __init__(self, x, y, score_group):
        super().__init__()
        self.image_sheet = resource.GFX['item_objects']
        self.setup_frames()
        self.frame_index = 0
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect()
        self.animate_timer = 0
        self.current_time = 0
        self.state = c.SPIN
        self.rect.centerx, self.rect.bottom = x, y - 5
        self.gravity = 1
        self.y_v = -15
        self.initial_height = self.rect.bottom - 5
        self.score_group = score_group


    def setup_frames(self):
        '''get frame list'''
        self.frames = []
        self.frames.append(self.get_image(52, 113, 8, 14))
        self.frames.append(self.get_image(4, 113, 8, 14))
        self.frames.append(self.get_image(20, 113, 8, 14))
        self.frames.append(self.get_image(36, 113, 8, 14))

    def get_image(self, x, y, width, height):
        image = pg.Surface((width, height))
        image.blit(self.image_sheet, (0,0), (x, y, width, height))
        image.set_colorkey(c.BLACK)
        rect = image.get_rect()
        return pg.transform.scale(image, (int(rect.width * 2.5), int(rect.height * 2.5)))

    def update(self, game_info):
        self.current_time = game_info[c.CURRENT_TIME]
        if self.state == c.SPIN:
            self.spinning()

    def spinning(self):
        self.image = self.frames[self.frame_index]
        self.rect.y += self.y_v
        self.y_v += self.gravity
        if self.current_time - self.animate_timer > 80:
            self.animate_timer = self.current_time
            self.frame_index = (self.frame_index + 1) % 4
        if self.rect.bottom > self.initial_height:
            self.score_group.add(score.Score(self.rect.x + 20, self.rect.y, 200))
            self.kill()  # if lower than threshold, kill


