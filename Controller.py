import pygame as pg
import sys

import config as c
import os
class Control():
    '''
    this is the Controller of whole game, which is used to ----
    1.initialize the game, create some variables used later
    2.setup the game --- that is, to initialize the state
    3.deal with events and update
    4.switch the game state, which indicates the game's part right now
    '''
    def __init__(self, caption):
        self.screen = pg.display.get_surface() #get screen
        self.caption = caption
        self.state = None
        self.state_name = None
        self.state_dict = None #state to control
        self.keys = pg.key.get_pressed()
        self.done = False      #is current state over
        self.clock = pg.time.Clock()
        self.current_time = 0
        self.fps = 60       #fps

    def setup_state(self, state_dict, state_name):
        self.state_dict, self.state_name = state_dict, state_name
        self.state = state_dict[state_name]

    def get_event(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif event.type == pg.KEYDOWN:
                self.keys = pg.key.get_pressed()
            elif event.type == pg.KEYUP:
                self.keys = pg.key.get_pressed()

    def update(self):
        self.current_time = pg.time.get_ticks() #get current time
        if self.state.done:
            self.flip_state()
        self.state.update(self.screen, self.keys, self.current_time)

    def flip_state(self):
        prev_state, self.state_name = self.state_name, self.state.next_state
        persist = self.state.clearup()
        self.state = self.state_dict[self.state_name]
        self.state.startup(self.current_time, persist)
        self.state.prev_state = prev_state

    def loop(self):
        while 1:
            self.get_event()
            self.update()
            pg.display.update()
            self.clock.tick(self.fps) #tick by fps

class State():
    '''
    base class of different States of the game, like State menu, State load_screen, State level 1;
    all State needs to maintain following info, including:
        game_info/persist --- info showing;  done/quit --- is state over?
        next_state/prev_state --- state switching; current_time --- timing or others
    '''
    def __init__(self):
        self.done = False
        self.quit = False
        self.next_state = None
        self.prev_state = None
        self.persist = None
        self.current_time = 0

    def startup(self, current_time, persist):
        '''call to start every state, behave like a constructive function'''
        pass

    def get_event(self):
        pass

    def update(self, screen, keys, current_time):
        pass

    def clearup(self):
        '''call when the state end, return game info'''
        self.done = False
        return self.persist  #game info maintained in every state