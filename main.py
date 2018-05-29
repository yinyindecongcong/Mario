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
                  c.LEVEL1: level1.Level1()
                  }
    Controller.setup_state(state_dict, c.MAIN_MENU)
    Controller.loop()

'''
def runGame():
    pygame.init()
    #screen = pygame.Surface((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
    screen = pygame.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
    back_g = pygame.image.load(r'D:\pycharm\projects\Mario\graph\level_1.png')
    screen.fill((111,111,111))
    image = pygame.image.load(r"D:\pycharm\projects\Mario\graph\item_objects.png")
    #image.set_colorkey((255,0,220))
    rect = image.get_rect()
    print(rect)
    print(image.get_alpha())
    #image = image.convert_alpha(screen)
    image2 = pygame.Surface((100,100))
    image2.blit(image, (0,0), (0, 0, 100,100))
    print(image.get_alpha())
    rectx = back_g.get_rect()
    #rectx.x = -100
    print(rectx)
    screen.blit(back_g, image.get_rect())
    screen.blit(image2, image.get_rect())
    while 1:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                sys.exit()
            elif ev.type == pygame.KEYDOWN:
                a = pygame.key.get_pressed()
                print(type(a))
                print(len(a))
                print(sum(a))
                print(a)
        pygame.display.flip()
runGame()
'''

if __name__ == '__main__':
    main()
    #runGame()