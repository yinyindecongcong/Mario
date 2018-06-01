import pygame as pg
import config as c, resource

class Enemy(pg.sprite.Sprite):
    '''base class for enemies(Goomba, Koopa)'''
    def __init__(self, x, bottom, name):
        super().__init__()
        self.image_sheet = resource.GFX['smb_enemies_sheet']
        self.setup_frames()
        self.frame_index = 0
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.bottom = x, bottom
        self.name = name
        self.facing_right = False
        self.x_v = 2 if self.facing_right else -2
        self.y_v = 0
        self.gravity = 1
        self.state = c.WALK
        self.current_time, self.timer = 0, 0

    def get_image(self, x, y, width, height):
        image = pg.Surface((width, height))
        image.blit(self.image_sheet, (0,0), (x, y, width, height))
        image.set_colorkey(c.BLACK)
        rect = image.get_rect()
        return pg.transform.scale(image, (int(rect.width * 2.5), int(rect.height * 2.5)))

    def update(self, game_info):
        self.current_time = game_info[c.CURRENT_TIME]
        self.handle_state()
        self.animation()

    def handle_state(self):
        '''update enemies data based on its state'''
        if self.state == c.WALK:
            self.walking()
        elif self.state == c.FALL:
            self.falling()
        elif self.state == c.JUMPED_ON:
            self.jumped_on()
        elif self.state == c.DEATH_JUMP:
            self.death_jump()
        elif self.state == c.SLIDE:     #only the shell-like enemies like turtle has this state
            self.slide()

    def walking(self):
        if self.current_time - self.timer > 125:
            self.timer = self.current_time
            self.frame_index = 1 - self.frame_index

    def falling(self):
        self.y_v = min(10, self.y_v + self.gravity)

    def jumped_on(self):
        '''call when is jumped on by mario'''
        pass

    def death_jump(self):
        self.rect.y += self.y_v
        self.rect.x += self.x_v
        self.y_v += self.gravity
        print(self.y_v)
        if self.rect.y > 600:
            self.kill()

    def start_death_jump(self):
        self.gravity = 0.5
        self.frame_index = 3
        self.state = c.DEATH_JUMP
        self.y_v = -10
        print('lalal')

    def animation(self):
        '''call to switch frame'''
        self.image = self.frames[self.frame_index]

class Goomba(Enemy):
    '''first enemy'''
    def __init__(self, x = 0, bottom = c.GROUND_HEIGHT, name = "Goomba"):
        super().__init__(x, bottom, name)

    def setup_frames(self):
        self.frames = []
        self.frames.append(self.get_image(0, 4, 16, 16))    #walk 1 [0]
        self.frames.append(self.get_image(30, 4, 16, 16))   #walk 2 [1]
        self.frames.append(self.get_image(61, 0, 16, 16))   #jumped on [2]
        self.frames.append(pg.transform.flip(self.frames[1], False, True)) #death jump [3]

    def jumped_on(self):
        self.frame_index = 2
        if self.current_time - self.timer > 500:
            self.kill()

class Koopa(Enemy):
    '''second enemy'''
    def __init__(self, x=0, bottom=c.GROUND_HEIGHT, name="Koopa"):
        super().__init__(x, bottom, name)

    def setup_frames(self):
        self.frames = []
        self.frames.append(self.get_image(150, 0, 16, 24))  #walk 1 [0]
        self.frames.append(self.get_image(180, 0, 16, 24))  #walk 2 [1]
        self.frames.append(self.get_image(360, 5, 16, 15))  #jumped on [2] -> shell
        self.frames.append(pg.transform.flip(self.frames[2], False, True))  #death jump [3]

    def jumped_on(self):
        '''become shell'''
        self.frame_index = 2
        self.x_v = 0
        bottom, x = self.rect.bottom, self.rect.x
        self.rect = self.frames[2].get_rect()
        self.rect.bottom, self.rect.x = bottom, x

    def slide(self):
        self.x_v = 10 if self.facing_right else -10

