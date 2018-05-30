import pygame as pg
image = pg.image.load('graph\level_1.png')
screen = pg.display.set_mode((800,600))
rect = image.get_rect()
rect.x = 5
print(rect.width, rect.w, rect.w == rect.width)

while 1:
    screen.blit(image, image.get_rect())
    pg.display.update()