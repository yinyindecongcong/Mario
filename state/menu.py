from Controller import State
import config as c, resource
import pygame as pg
from component import info, mario
class Menu(State):
    '''
    first State when game start, with elements,
    including background, info(title, score, etc), mario
    '''
    def __init__(self): #call only once
        super().__init__()
        game_info = {c.SCORE: 0,
                   c.TOP_SCORE:0,
                   c.COIN_TOTAL: 0,
                   c.LIVES: 3,
                   c.CURRENT_TIME: 0.0,
                   c.LEVEL_STATE: None, #
                   c.CAMERA_START_X: 0, #position of Mario
                   c.MARIO_DEAD: False}
        self.startup(0, game_info)

    def startup(self, current_time, game_info):  #call every time switch into this state
        self.game_info = game_info
        self.game_info[c.SCORE] = 0
        self.game_info[c.COIN_TOTAL] = 0
        self.next_state = c.LOAD_SCREEN
        self.info = info.Info(self.game_info, c.MAIN_MENU)

        self.title_screen = resource.GFX['title_screen']
        self.load_background()
        self.load_Mario()
        self.load_cursor()

    def load_cursor(self):
        dest = (220, 358)
        self.cursor_image, self.cursor_rect = self.get_image(resource.GFX['title_screen'],
                                                             dest, 0, 150, 13, 13)
        self.cursor_image.set_colorkey(c.BLACK)
        self.cursor_state = c.PLAYER1

    def load_background(self):
        self.bg_image = resource.GFX['level_1']
        self.bg_rect = self.bg_image.get_rect()
        self.bg_image = pg.transform.scale(self.bg_image,
                                           (int(self.bg_rect.width * c.BACKGROUND_MULTIPLER),
                                            int(self.bg_rect.height * c.BACKGROUND_MULTIPLER)))
        self.bg_rect = resource.screen.get_rect()       #与屏幕重合
        self.game_box_image, self.game_box_rect = self.get_image(resource.GFX['title_screen'],
                                                                 (170, 100), 1, 60, 176, 88)

    def load_Mario(self):
        self.mario = mario.Mario()
        self.mario.rect.x = 110
        self.mario.rect.bottom = c.GROUND_HEIGHT

    def update(self, screen, keys, current_time):
        self.current_time = current_time
        self.game_info[c.CURRENT_TIME] = current_time
        self.update_cursor(keys)
        self.info.update(self.game_info)
        screen.blit(self.bg_image, self.bg_rect)
        screen.blit(self.cursor_image, self.cursor_rect)
        screen.blit(self.game_box_image, self.game_box_rect)
        screen.blit(self.mario.image, self.mario.rect)
        self.info.draw(screen)

    def update_cursor(self, keys):
        proceed = [pg.K_a, pg.K_s, pg.K_RETURN] #a or s or enter to proceed
        if self.cursor_state == c.PLAYER1:
            self.cursor_rect.y = 347
            if keys[pg.K_DOWN]:
                self.cursor_rect.y = 393
                self.cursor_state = c.PLAYER2
            for each in proceed:
                if keys[each]:
                    self.done = True
                    self.reset_game_info()
        else:
            if keys[pg.K_UP]:
                self.cursor_rect.y = 347
                self.cursor_state = c.PLAYER1


    def get_image(self, source, dest, x, y, width, height):
        image = pg.Surface([width, height])
        image.blit(source, (0, 0), (x, y, width, height)) #draw img onto image
        if source == resource.GFX['title_screen']:
            image.set_colorkey((255,0,220))
            image = pg.transform.scale(image, (int(width * c.SIZE_MULTIPLIER), int(height * c.SIZE_MULTIPLIER)))
        rect = image.get_rect()
        rect.x, rect.y = dest[0], dest[1]
        return image, rect

    def reset_game_info(self):
        '''called when restart or game over'''
        self.game_info[c.SCORE] = 0
        self.game_info[c.CURRENT_TIME] = 0
        self.game_info[c.LIVES] = 3
        self.game_info[c.COIN_TOTAL] = 0
        self.game_info[c.LEVEL_STATE] = None
        self.game_info[c.CAMERA_START_X] = 0





