import pygame as pg
import config as c, resource
from component.info import Character

class Score(pg.sprite.Sprite):
    def __init__(self, x, y, score):
        super().__init__()
        self.x, self.y = x, y
        self.image_sheet = resource.GFX['text_images']
        self.y_v = -7
        self.gravity = 0.3
        self.score_str = str(score)
        self.create_image_dict()
        self.create_score_label()

    def create_image_dict(self):
        '''create image dict for all numbers'''
        self.image_dict = {}
        image_list = []
        # numbers 0 --- 9
        image_list.append(self.get_image(3, 230, 7, 7))
        image_list.append(self.get_image(12, 230, 7, 7))
        image_list.append(self.get_image(19, 230, 7, 7))
        image_list.append(self.get_image(27, 230, 7, 7))
        image_list.append(self.get_image(35, 230, 7, 7))
        image_list.append(self.get_image(43, 230, 7, 7))
        image_list.append(self.get_image(51, 230, 7, 7))
        image_list.append(self.get_image(59, 230, 7, 7))
        image_list.append(self.get_image(67, 230, 7, 7))
        image_list.append(self.get_image(75, 230, 7, 7))
        image_list.append(self.get_image(115, 238, 7, 7))
        image_list.append(self.get_image(75, 238, 7, 7))
        character_string = '0123456789UP'
        for character, image in zip(character_string, image_list):
            self.image_dict[character] = image

    def get_image(self, x, y, width, height):
        image = pg.Surface([width, height])
        image.blit(self.image_sheet, (0, 0), (x, y, width, height)) #draw img onto image
        image.set_colorkey((92,148,252)) #remove the blue
        image = pg.transform.scale(image, (int(width * 1.6), int(height * 1.6)))
        return image

    def create_score_label(self):
        self.score_label = []
        for digit in self.score_str:
            self.score_label.append(Character(self.image_dict[digit]))
        for i, char in enumerate(self.score_label):
            char.rect.x = self.x + 12 * i
            char.rect.y = self.y

    def update(self):
        for each in self.score_label:
            each.rect.y += self.y_v
        self.y_v += self.gravity
        if self.y_v >= 0: self.kill()

    def draw(self, screen):
        for each in self.score_label:
            screen.blit(each.image, each.rect)