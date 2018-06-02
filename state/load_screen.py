import pygame as pg
import config as c, resource, Controller
from component import info
class LoadScreen(Controller.State):
    '''temp State when state switch, such as Menu --> Level1, need a temp state showing info, with element info'''
    def __init__(self):
        super().__init__()

    def startup(self, current_time, game_info):
        self.start_time = current_time
        self.game_info = game_info
        self.next_state = self.set_next_state()
        info_state = self.set_info_state()
        self.info = info.Info(self.game_info, info_state)

    def set_next_state(self):
        return c.LEVEL1

    def set_info_state(self):
        return c.LOAD_SCREEN

    def update(self, screen, keys, current_time):
        self.game_info[c.CURRENT_TIME] = current_time
        if current_time - self.start_time < 2500:
            screen.fill(c.BLACK)
            self.info.update(self.game_info)
            self.info.draw(screen)
        elif current_time - self.start_time < 2700:
            screen.fill(c.BLACK)
        elif current_time - self.start_time < 2835:
            screen.fill((106,150,252))
        else:
            self.done = True

class GameOver(LoadScreen):
    def __init__(self):
        super().__init__()

    def set_info_state(self):
        return c.GAME_OVER

    def set_next_state(self):
        return c.MAIN_MENU



