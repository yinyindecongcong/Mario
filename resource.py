import pygame as pg
import os
import config as c

def load_all_graphs(directory, colorkey=(255, 0, 220), accept=('.png', '.jpg', '.bmp')):
    '''load graphs with extension test'''
    graphs = {}
    for each in os.listdir(directory):
        name, ext = os.path.splitext(each)
        if ext.lower() in accept:
            img = pg.image.load(os.path.join(directory, each))
            if img.get_alpha():
                img = img.convert_alpha()  # 优化透明通道
            else:  # 为各种字体
                img.set_colorkey(colorkey)  # 去掉紫色背景
            graphs[name] = img
    return graphs

def load_all_music(directory, accept=('.wav', '.ogg', 'mdi')):
    '''load music with extension test'''
    music = {}
    for each in os.listdir(directory):
        name, ext = os.path.splitext(each)
        if ext.lower() in accept:
            music[name] = os.path.join(directory, each)
            #music can play in streaming mode while loading, needn't to load at first
    return music

def load_all_sound(directory, accept=('.wav', '.ogg', 'mdi')):
    '''load sound with extension test'''
    sound = {}
    for each in os.listdir(directory):
        name, ext = os.path.splitext(each)
        if ext.lower() in accept:
            sound[name] = pg.mixer.Sound(os.path.join(directory, each))
    return sound

'''set control key, determining different action'''
keybinding = {'fireball':pg.K_s,
              'jump':pg.K_UP,
              'left':pg.K_LEFT,
              'right':pg.K_RIGHT,
              'down':pg.K_DOWN}
'''initialize pygame and pygame_mixer to prepare for show and sound playing'''
pg.init()
pg.mixer.init()
screen = pg.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
pg.display.set_caption(c.CAPTION)
GFX = load_all_graphs('graph')
SFX = load_all_sound('sound')
MUSIC = load_all_music('music')
