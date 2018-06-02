import pygame as pg
import config as c, resource

class Sound():
    '''handle all music in the game'''
    def __init__(self, info):
        self.sfx = resource.SFX
        self.music = resource.MUSIC
        self.info = info
        self.game_info = info.game_info
        self.set_bgm()

    def set_bgm(self):
        '''set music as bgm for level1'''
        if self.info.state == c.LEVEL1:
            self.play_music('main_theme', c.LEVEL1)
        elif self.info.state == c.GAME_OVER:
            self.play_music('game_over', c.GAME_OVER)

    def update(self, game_info, mario):
        self.game_info = game_info
        self.mario = mario
        self.handle()

    def handle(self):
        '''
        handle all state of mario or others,
        and promise that each music be play just once
        '''
        if self.state == c.LEVEL1:  #play a level1 music and switch state
            if self.game_info[c.MARIO_DEAD]:
                self.play_music('death', c.MARIO_DEAD)
            elif self.mario.invincible:
                self.play_music('invincible', c.INVINCIBLE)
            elif self.mario.state == c.FLAGPOLE:
                self.play_music('flagpole', c.FLAGPOLE)
            elif self.info.time == 100:
                self.play_music('out_of_time', c.TIME_WARNING)
        elif self.state == c.FLAGPOLE:  #play walking_to_castle music
            if self.mario.state == c.WALKING_TO_CASTLE:
                self.play_music('stage_clear', c.STAGE_CLEAR)
        elif self.state == c.STAGE_CLEAR:
            if self.mario.in_castle:    #play count down sound
                self.sfx['count_down'].play()
                self.state = c.FAST_COUNT_DOWN
        elif self.state == c.FAST_COUNT_DOWN:
            if self.info.time == 0:
                self.sfx['count_down'].stop()    #end count down sound
                self.state = c.WORLD_CLEAR
        elif self.state == c.TIME_WARNING:
            if pg.mixer.get_busy() == 0:    #wait for end of time warning music
                self.play_music('main_theme_sped_up', c.LEVEL1)
            elif self.mario.dead:
                self.play_music('death', c.MARIO_DEAD)
        elif self.state == c.INVINCIBLE:
            if self.mario.current_time - self.mario.invincible_start_timer > 11000:
                self.play_music('main_theme', c.LEVEL1)
            elif self.mario.dead:
                self.play_music('death', c.MARIO_DEAD)

    def play_music(self, name, state="state"):
        '''Plays new music'''
        pg.mixer.music.load(self.music[name])
        pg.mixer.music.play()
        self.state = state

    def stop_music(self):
        pg.mixer.music.stop()