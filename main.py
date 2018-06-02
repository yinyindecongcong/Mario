import pygame
import os
import sys
import config as c
import Controller as Con
from state import menu, load_screen, level1
import resource
def main():
    Controller = Con.Control(c.CAPTION)
    '''add states to control'''
    state_dict = {c.MAIN_MENU: menu.Menu(),
                  c.LOAD_SCREEN: load_screen.LoadScreen(),
                  c.LEVEL1: level1.Level1(),
                  c.GAME_OVER: load_screen.GameOver()
                  }
    Controller.setup_state(state_dict, c.MAIN_MENU)
    Controller.loop()

if __name__ == '__main__':
    main()