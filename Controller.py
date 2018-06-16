import pygame as pg
import sys

import config as c
from socket import socket, AF_INET, SOCK_DGRAM
import json

keys2 = []
pa_state = None
#UDPlistener = socket(AF_INET, SOCK_DGRAM)
UDPsender = socket(AF_INET, SOCK_DGRAM)
#UDPlistener.bind(player1_address[0])
UDPsender.bind(c.player1_address[0])

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
        self.nonekey = pg.key.get_pressed()
        self.done = False      #is current state over
        self.clock = pg.time.Clock()
        self.current_time = 0
        self.fps = 60       #fps
        self.index = 0
        self.count = 1
        self.character = 0

    def setup_state(self, state_dict, state_name):
        self.state_dict, self.state_name = state_dict, state_name
        self.state = state_dict[state_name]

    def recvkeys(self):
        tmp_packet, addr = UDPsender.recvfrom(1024)
        dic = json.loads(tmp_packet.decode())
        global keys2, pa_state
        keys2, pa_state = dic['keys'], dic['state']
        if dic.get('player1', 'no') != 'no':
            self.state.game_info[c.PLAYER1] = (not dic['player1'])

    def sendkeys(self):
        dic = {'keys': self.keys, 'state': self.state_name}
        UDPsender.sendto(json.dumps(dic).encode(), c.server_address)

    def get_event(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            else:
                self.keys = pg.key.get_pressed()
        if self.state.game_info[c.TWO_players]:
            self.sendkeys()
            try:
                self.recvkeys()
            except ConnectionResetError: #服务器未打开
                pass

    def update(self):
        self.current_time = pg.time.get_ticks() #get current time
        if self.state.done:
            self.flip_state()
        if self.state_name != c.LEVEL1:
            self.state.update(self.screen, self.keys, self.keys, self.current_time)
        elif self.state.game_info[c.TWO_players]:
            if pa_state != c.LEVEL1:
                if self.count:
                    self.state.update(self.screen, self.nonekey, self.nonekey, self.current_time)
                    self.count = 0
            elif pa_state == c.LEVEL1:
                if self.state.game_info[c.PLAYER1]:
                    self.state.update(self.screen, self.keys, keys2, self.current_time)
                else:
                    self.state.update(self.screen, keys2, self.keys, self.current_time)
        else:
            self.state.update(self.screen, self.keys, self.keys, self.current_time)

    def flip_state(self):
        prev_state, self.state_name = self.state_name, self.state.next_state
        game_info = self.state.clearup()
        self.state = self.state_dict[self.state_name]
        self.state.startup(self.current_time, game_info)
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
        game_info --- info showing;  done/quit --- is state over?
        next_state/prev_state --- state switching; current_time --- timing or others
    '''
    def __init__(self):
        self.done = False
        self.quit = False
        self.next_state = None
        self.prev_state = None
        self.game_info = None
        self.current_time = 0

    def startup(self, current_time, game_info):
        '''call to start every state, behave like a constructive function'''
        pass

    def get_event(self):
        pass

    def update(self, screen, keys1, keys2, current_time):
        pass

    def clearup(self):
        '''call when the state end, return game info'''
        self.done = False
        return self.game_info  #game info maintained in every state
