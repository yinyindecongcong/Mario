import pygame as pg
import os
import config as c
import graph
def load_all_graphs(directory, colorkey=(255, 0, 255), accept=('.png', '.jpg', '.bmp')):
    graphs = {}
    for each in os.listdir(directory):
        name, ext = os.path.splitext(each)
        if ext.lower() in accept:
            img = pg.image.load(os.path.join(directory, each))
            if img.get_alpha():
                img = img.convert_alpha()  # 优化透明通道
            else:  # 为各种字体
                img.set_colorkey(colorkey)  # 去掉紫色
            graphs[name] = img
    return graphs

def load_all_music():
    pass

def load_all_sound():
    pass

def load_all_font():
    pass

keybinding = {'fireball':pg.K_s,
              'jump':pg.K_UP,
              'left':pg.K_LEFT,
              'right':pg.K_RIGHT,
              'down':pg.K_DOWN}

pg.init()
screen = pg.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
pg.display.set_caption(c.CAPTION)
GFX = load_all_graphs('graph')
