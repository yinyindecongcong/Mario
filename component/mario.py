import pygame as pg
import config as c, resource
from component import fireball
class Mario(pg.sprite.Sprite):
    def __init__(self, name='1'):
        super().__init__()
        self.name = name
        self.image_sheet = resource.GFX['mario_bros']
        self.setup_timers()
        self.setup_states()
        self.setup_images()
        self.setup_frames_counter()
        self.setup_force()
        self.state = c.STAND
        self.image = self.right_frames[self.frame_index]
        self.rect = self.image.get_rect()
        #添加了名字用来初始化mario，调整mario颜色
        self.current_time = 0

    def setup_timers(self):
        '''setup timers for every state of mario, used for animation'''
        self.walking_timer = 0 #walking
        self.big_transition_timer = 0  #timer of SMALL-TO-BIG state
        self.fire_transition_timer = 0 #timer of BIG-TO-FIRE state
        self.invincible_animation_timer = 0 #timer of invincible state
        self.invincible_start_timer = 0
        self.death_timer = 0    #timer of DEATH state
        self.last_fireball_timer = 0 #fireball
        self.flag_pole_timer = 0 #
        self.hurt_invincible_timer = 0

    def setup_states(self):
        '''setup states that affect the behavior of mario'''
        self.facing_right = True
        self.allow_jump = True
        self.crouching = False
        self.big = False
        self.fire = False
        self.dead = False
        self.invincible = False
        self.allow_fireball = True
        self.in_transition_state = False
        self.hurt_invincible = False #when hurt, a short time invincible
        self.in_castle = False

    def setup_frames_counter(self):
        '''setup frame index of animation and counter of fire_ball'''
        self.frame_index = 0
        self.invincible_index = 0
        self.fire_ball_count = 0
        self.flag_pole_index = 0

    def setup_force(self):
        '''setup forces to adjust mario's speed in different action'''
        self.x_v = 0
        self.y_v = 0
        self.max_x_v = c.MAX_WALK_SPEED
        self.max_y_v = c.MAX_Y_VEL
        self.x_ac = c.WALK_ACCEL
        self.jump_v = c.JUMP_VEL
        self.y_ac = c.GRAVITY

    def setup_images(self):
        '''load all images and divide them into different groups for convenience'''
        self.right_small_normal_frames = []    #normal color
        self.right_small_green_frames = []     #green\red\black used when transition and invincible
        self.right_small_red_frames = []
        self.right_small_black_frames = []
        self.left_small_normal_frames = []
        self.left_small_green_frames = []
        self.left_small_red_frames = []
        self.left_small_black_frames = []

        self.right_big_normal_frames = []       # normal color
        self.right_big_green_frames = []        # green\red\black used when transition and invincible
        self.right_big_red_frames = []
        self.right_big_black_frames = []
        self.left_big_normal_frames = []
        self.left_big_green_frames = []
        self.left_big_red_frames = []
        self.left_big_black_frames = []

        self.right_fire_frames = []  # normal color
        self.left_fire_frames = []


        #right_small_normal_frames
        self.right_small_normal_frames.append(self.get_image(178, 32, 12, 16))  # right standing [0]
        self.right_small_normal_frames.append(self.get_image(80, 32, 15, 16))   # Right walking 1 [1]
        self.right_small_normal_frames.append(self.get_image(96, 32, 16, 16))   # Right walking 2 [2]
        self.right_small_normal_frames.append(self.get_image(112, 32, 16, 16))  # Right walking 3 [3]
        self.right_small_normal_frames.append(self.get_image(144, 32, 16, 16))  # Right jump [4]
        self.right_small_normal_frames.append(self.get_image(130, 32, 14, 16))  # Right skid [5]
        self.right_small_normal_frames.append(self.get_image(160, 32, 15, 16))  # Death frame [6]
        self.right_small_normal_frames.append(self.get_image(320, 8, 16, 24))   # Transition small to big [7]
        self.right_small_normal_frames.append(self.get_image(241, 33, 16, 16))  # Transition big to small [8]
        self.right_small_normal_frames.append(self.get_image(194, 32, 12, 16))  # Frame 1 of flag pole Slide [9]
        self.right_small_normal_frames.append(self.get_image(210, 33, 12, 16))  # Frame 2 of flag pole slide [10]

        #right_small_green_frames for invincible animation
        self.right_small_green_frames.append(self.get_image(178, 128, 12, 16))  # right standing [0]
        self.right_small_green_frames.append(self.get_image(80, 128, 15, 16))  # Right walking 1 [1]
        self.right_small_green_frames.append(self.get_image(96, 128, 16, 16))  # Right walking 2 [2]
        self.right_small_green_frames.append(self.get_image(112, 128, 16, 16))  # Right walking 3 [3]
        self.right_small_green_frames.append(self.get_image(144, 128, 16, 16))  # Right jump [4]
        self.right_small_green_frames.append(self.get_image(130, 128, 14, 16))  # Right skid [5]
        self.right_small_green_frames.append(self.get_image(160, 128, 15, 16))  # Death frame [6]
        #TODO 绿的变大图片可能有问题
        self.right_small_green_frames.append(self.get_image(320, 104, 16, 24))   # Transition small to big [7]
        self.right_small_green_frames.append(self.get_image(241, 128, 16, 16))  # Transition big to small [8]
        self.right_small_green_frames.append(self.get_image(194, 128, 12, 16))  # Frame 1 of flag pole Slide [9]
        self.right_small_green_frames.append(self.get_image(210, 128, 12, 16))  # Frame 2 of flag pole slide [10]

        # right_small_red_frames for invincible animation
        self.right_small_red_frames.append(self.get_image(178, 272, 12, 16))  # right standing [0]
        self.right_small_red_frames.append(self.get_image(80, 272, 15, 16))  # Right walking 1 [1]
        self.right_small_red_frames.append(self.get_image(96, 272, 16, 16))  # Right walking 2 [2]
        self.right_small_red_frames.append(self.get_image(112, 272, 16, 16))  # Right walking 3 [3]
        self.right_small_red_frames.append(self.get_image(144, 272, 16, 16))  # Right jump [4]
        self.right_small_red_frames.append(self.get_image(130, 272, 14, 16))  # Right skid [5]

        # right_small_black_frames for invincible animation
        self.right_small_black_frames.append(self.get_image(178, 176, 12, 16))  # right standing [0]
        self.right_small_black_frames.append(self.get_image(80, 176, 15, 16))  # Right walking 1 [1]
        self.right_small_black_frames.append(self.get_image(96, 176, 16, 16))  # Right walking 2 [2]
        self.right_small_black_frames.append(self.get_image(112, 176, 16, 16))  # Right walking 3 [3]
        self.right_small_black_frames.append(self.get_image(144, 176, 16, 16))  # Right jump [4]
        self.right_small_black_frames.append(self.get_image(130, 176, 14, 16))  # Right skid [5]

        # right_big_normal_frames
        self.right_big_normal_frames.append(self.get_image(176, 0, 16, 32))  # right standing [0]
        self.right_big_normal_frames.append(self.get_image(81, 0, 16, 32))   # Right walking 1 [1]
        self.right_big_normal_frames.append(self.get_image(97, 0, 15, 32))   # Right walking 2 [2]
        self.right_big_normal_frames.append(self.get_image(113, 0, 15, 32))  # Right walking 3 [3]
        self.right_big_normal_frames.append(self.get_image(144, 0, 16, 32))  # Right jump [4]
        self.right_big_normal_frames.append(self.get_image(128, 0, 16, 32))  # Right skid [5]
        self.right_big_normal_frames.append(self.get_image(336, 0, 16, 32))  # Right throwing [6]
        self.right_big_normal_frames.append(self.get_image(160, 10, 16, 22))  # Right crouching [7]
        self.right_big_normal_frames.append(self.get_image(272, 2, 16, 29))  # Transition big to small [8]
        self.right_big_normal_frames.append(self.get_image(193, 2, 16, 30))  # Frame 1 of flag pole slide [9]
        self.right_big_normal_frames.append(self.get_image(209, 2, 16, 29))  # Frame 2 of flag pole slide [10]

        # right_big_green_frames for invincible animation
        self.right_big_green_frames.append(self.get_image(176, 96, 16, 32))  # right standing [0]
        self.right_big_green_frames.append(self.get_image(81, 96, 16, 32))  # Right walking 1 [1]
        self.right_big_green_frames.append(self.get_image(97, 96, 15, 32))  # Right walking 2 [2]
        self.right_big_green_frames.append(self.get_image(113, 96, 15, 32))  # Right walking 3 [3]
        self.right_big_green_frames.append(self.get_image(144, 96, 16, 32))  # Right jump [4]
        self.right_big_green_frames.append(self.get_image(128, 96, 16, 32))  # Right skid [5]
        self.right_big_green_frames.append(self.get_image(336, 96, 16, 32))  # Right throwing [6]
        self.right_big_green_frames.append(self.get_image(160, 106, 16, 22))  # Right crouching [7]
        self.right_big_green_frames.append(self.get_image(272, 98, 16, 29))  # Transition big to small [8]
        self.right_big_green_frames.append(self.get_image(193, 98, 16, 30))  # Frame 1 of flag pole slide [9]
        self.right_big_green_frames.append(self.get_image(209, 98, 16, 29))  # Frame 2 of flag pole slide [10]

        # right_big_red_frames for invincible animation
        self.right_big_red_frames.append(self.get_image(176, 240, 16, 32))  # right standing [0]
        self.right_big_red_frames.append(self.get_image(81, 240, 16, 32))  # Right walking 1 [1]
        self.right_big_red_frames.append(self.get_image(97, 240, 15, 32))  # Right walking 2 [2]
        self.right_big_red_frames.append(self.get_image(113, 240, 15, 32))  # Right walking 3 [3]
        self.right_big_red_frames.append(self.get_image(144, 240, 16, 32))  # Right jump [4]
        self.right_big_red_frames.append(self.get_image(128, 240, 16, 32))  # Right skid [5]
        self.right_big_red_frames.append(self.get_image(336, 240, 16, 32))  # Right throwing [6]
        self.right_big_red_frames.append(self.get_image(160, 250, 16, 22))  # Right crouching [7]

        # right_big_black_frames for invincible animation
        self.right_big_black_frames.append(self.get_image(176, 144, 16, 32))  # right standing [0]
        self.right_big_black_frames.append(self.get_image(81, 144, 16, 32))  # Right walking 1 [1]
        self.right_big_black_frames.append(self.get_image(97, 144, 15, 32))  # Right walking 2 [2]
        self.right_big_black_frames.append(self.get_image(113, 144, 15, 32))  # Right walking 3 [3]
        self.right_big_black_frames.append(self.get_image(144, 144, 16, 32))  # Right jump [4]
        self.right_big_black_frames.append(self.get_image(128, 144, 16, 32))  # Right skid [5]
        self.right_big_black_frames.append(self.get_image(336, 144, 16, 32))  # Right throwing [6]
        self.right_big_black_frames.append(self.get_image(160, 154, 16, 22))  # Right crouching [7]

        #right_big_fire_frames
        self.right_fire_frames.append(self.get_image(176, 48, 16, 32))  # Right standing [0]
        self.right_fire_frames.append(self.get_image(81, 48, 16, 32))   # Right walking 1 [1]
        self.right_fire_frames.append(self.get_image(97, 48, 15, 32))   # Right walking 2 [2]
        self.right_fire_frames.append(self.get_image(113, 48, 15, 32))  # Right walking 3 [3]
        self.right_fire_frames.append(self.get_image(144, 48, 16, 32))  # Right jump [4]
        self.right_fire_frames.append(self.get_image(128, 48, 16, 32))  # Right skid [5]
        self.right_fire_frames.append(self.get_image(336, 48, 16, 32))  # Right throwing [6]
        self.right_fire_frames.append(self.get_image(160, 58, 16, 22))  # Right crouching [7]
        self.right_fire_frames.append(self.get_image(0, 0, 0, 0))       # Place holder [8]
        self.right_fire_frames.append(self.get_image(193, 50, 16, 29))  # Frame 1 of flag pole slide [9]
        self.right_fire_frames.append(self.get_image(209, 50, 16, 29))  # Frame 2 of flag pole slide [10]

        #判断是否是路易，交换两个列表
        if self.name == '2':
            self.right_small_normal_frames, self.right_small_green_frames = \
                self.right_small_green_frames, self.right_small_normal_frames
            self.right_big_normal_frames, self.right_big_green_frames = \
                self.right_big_green_frames, self.right_big_normal_frames

        self.right_frames_group = [self.right_small_normal_frames, self.right_small_green_frames,
                                   self.right_small_red_frames, self.right_small_black_frames,
                                   self.right_big_normal_frames, self.right_big_green_frames,
                                   self.right_big_red_frames, self.right_big_black_frames,
                                   self.right_fire_frames]
        self.left_frames_group = [self.left_small_normal_frames, self.left_small_green_frames,
                                  self.left_small_red_frames, self.left_small_black_frames,
                                  self.left_big_normal_frames, self.left_big_green_frames,
                                  self.left_big_red_frames, self.left_big_black_frames,
                                  self.left_fire_frames]

        #setup left frames using pygame.transform.flip()
        for i in range(len(self.right_frames_group)):
            for frame in self.right_frames_group[i]:
                self.left_frames_group[i].append(pg.transform.flip(frame, True, False))

        #classify
        self.normal_small_frames = [self.right_small_normal_frames,
                                    self.left_small_normal_frames]
        self.green_small_frames = [self.right_small_green_frames,
                                   self.left_small_green_frames]
        self.red_small_frames = [self.right_small_red_frames,
                                 self.left_small_red_frames]
        self.black_small_frames = [self.right_small_black_frames,
                                   self.left_small_black_frames]
        self.invincible_small_frames_list = [self.normal_small_frames, self.green_small_frames,
                                             self.red_small_frames, self.black_small_frames]
        self.normal_big_frames = [self.right_big_normal_frames,
                                  self.left_big_normal_frames]
        self.green_big_frames = [self.right_big_green_frames,
                                 self.left_big_green_frames]
        self.red_big_frames = [self.right_big_red_frames,
                               self.left_big_red_frames]
        self.black_big_frames = [self.right_big_black_frames,
                                 self.left_big_black_frames]
        self.fire_frames = [self.right_fire_frames,
                            self.left_fire_frames]
        self.invincible_big_frames_list = [self.normal_big_frames, self.green_big_frames,
                                           self.red_big_frames, self.black_big_frames]
        self.all_frames_group = self.right_frames_group + self.left_frames_group
        self.right_frames = self.normal_small_frames[0]
        self.left_frames = self.normal_small_frames[1]

    def get_image(self, x, y, width, height):
        image = pg.Surface([width, height])
        image.blit(self.image_sheet, (0, 0), (x, y, width, height)) #draw img onto image
        image.set_colorkey(c.BLACK) #创建的surface对象背景色为黑色
        image = pg.transform.scale(image, (int(width * 2.5), int(height * 2.5)))
        return image

    def update(self, keys, game_info, fireball_group):
        self.current_time = game_info[c.CURRENT_TIME]
        self.handle_state(keys, fireball_group)         #adjust state based on keys
        self.check_state_update_frame()  #check if there is any special state like invincible
        self.animation()                #animation the behavior of mario, that is, choose the right image

    def handle_state(self, keys, fireball_group):
        '''determine behavior of Mario based on state'''
        if self.state == c.STAND:
            self.standing(keys, fireball_group)
        elif self.state == c.WALK:
            self.walking(keys, fireball_group)
        elif self.state == c.JUMP:
            self.jumping(keys, fireball_group)
        elif self.state == c.FALL:
            self.falling(keys, fireball_group)
        elif self.state == c.SMALL_TO_BIG:
            self.small_to_big()
        elif self.state == c.BIG_TO_FIRE:
            self.big_to_fire()
        elif self.state == c.BIG_TO_SMALL:
            self.big_to_small()
        elif self.state == c.DEATH_JUMP:
            self.death_jump()
        elif self.state == c.FLAGPOLE:
            self.slide_down_pole()
        elif self.state == c.BOTTOM_OF_POLE:
            self.sitting_on_bottom()
        elif self.state == c.WALKING_TO_CASTLE:
            self.walking_to_castle()
        elif self.state == c.END_OF_LEVEL_FALL:
            self.end_fall()


    def standing(self, keys, fireball_group):
        '''
        check if Mario is still standing,
        actually fireball_group contains not only fireball
        '''
        self.check_to_allow_jump(keys)
        self.check_to_allow_fireball(keys) #check some special state

        self.frame_index = 0
        self.x_v, self.y_v = 0, 0
        if not keys[resource.keybinding['down']]:
            self.get_out_of_crouch()
        if keys[resource.keybinding['fireball']]:
            if self.fire and self.allow_fireball:
                self.shoot(fireball_group)
        elif keys[resource.keybinding['down']]:
            self.crouching = True
        elif keys[resource.keybinding['right']] and (not keys[resource.keybinding['left']]):
            self.facing_right = True
            self.state = c.WALK
        elif keys[resource.keybinding['left']] and (not keys[resource.keybinding['right']]):
            self.facing_right = False
            self.state = c.WALK
        elif keys[resource.keybinding['jump']]:
            if self.allow_jump:
                self.state = c.JUMP
                self.y_v = c.JUMP_VEL
                if self.big:
                    resource.SFX['big_jump'].play()
                else:
                    resource.SFX['small_jump'].play()
        else:
            self.state = c.STAND

    def shoot(self, fireball_group):
        '''produce a fireball if permit'''
        list1 = [1 for x in fireball_group if x.name == c.FIREBALL]
        if len(list1) < 2:
            if self.current_time - self.last_fireball_timer > 200:
                self.last_fireball_timer = self.current_time
                self.allow_fireball = False
                fireball_group.add(fireball.FireBall(self.rect.x, self.rect.y, self.facing_right))
                resource.SFX['fireball'].play()
                self.frame_index = 6

    def get_out_of_crouch(self):
        '''become stand'''
        bottom, x = self.rect.bottom, self.rect.x
        self.image = self.right_frames[0] if self.facing_right else self.left_frames[0]
        self.rect = self.image.get_rect()
        self.rect.bottom, self.rect.x = bottom, x
        self.crouching = False

    def walking(self, keys, fireball_group):
        '''determine mario's behavior when walking based on keys'''
        self.check_to_allow_jump(keys)
        self.check_to_allow_fireball(keys)  # check some special state
        #switch frame
        if self.frame_index == 0:
            self.frame_index = 1
            self.walking_timer = self.current_time
        elif self.current_time - self.walking_timer > self.animation_interval():
                if self.frame_index < 3:
                    self.frame_index += 1
                else:
                    self.frame_index = 1
                self.walking_timer = self.current_time
        #run or fireball
        if keys[resource.keybinding['fireball']]:
            #run and shoot
            self.max_x_v = c.MAX_RUN_SPEED
            self.x_ac = c.RUN_ACCEL
            if self.fire and self.allow_fireball:
                self.shoot(fireball_group)
        else:
            self.max_x_v = c.MAX_WALK_SPEED
            self.x_ac = c.WALK_ACCEL

        #jump
        if keys[resource.keybinding['jump']]:
            if self.allow_jump:
                self.state = c.JUMP
                self.y_v = c.JUMP_VEL
                if self.big:
                    resource.SFX['big_jump'].play()
                else:
                    resource.SFX['small_jump'].play()
        #left or right
        if keys[resource.keybinding['left']] and (not keys[resource.keybinding['right']]):
            self.facing_right = False
            if self.x_v > 0:
                self.x_ac = c.TURNAROUND
                self.frame_index = 5
            else:
                self.x_ac = c.WALK_ACCEL
            if self.x_v <= -1 * self.max_x_v:
                self.x_v = -1 * self.max_x_v
            else:
                self.x_v -= self.x_ac
        elif keys[resource.keybinding['right']] and (not keys[resource.keybinding['left']]):
            self.facing_right = True
            if self.x_v < 0:
                self.x_ac = c.TURNAROUND
                self.frame_index = 5
            else:
                self.x_ac = c.WALK_ACCEL
            if self.x_v > self.max_x_v:
                self.x_v = self.max_x_v
            else:
                self.x_v += self.x_ac
        #nothing or press left and right in the same time
        else:
            if self.facing_right:
                if self.x_v > 0:
                    self.x_v = max(0, self.x_v - self.x_ac)
                else:
                    self.x_v = 0
                    self.state = c.STAND
            else:
                if self.x_v < 0:
                    self.x_v = min(0, self.x_v + self.x_ac)
                else:
                    self.x_v = 0
                    self.state = c.STAND

    def animation_interval(self):
        '''adjust the animation interval based on mario's speed'''
        if self.x_v == 0:
            return c.INTERVEL
        return c.INTERVEL - abs(self.x_v) * 20

    def jumping(self, keys, fireball_group):
        '''determine mario's behavior when walking based on keys'''
        self.check_to_allow_fireball(keys)
        self.frame_index = 4
        self.allow_jump = False
        if keys[resource.keybinding['jump']]:
            self.y_ac = c.JUMP_AC
        else:
            self.state, self.y_ac = c.FALL, c.GRAVITY
        self.y_v += self.y_ac
        if self.y_v >= 0:
            self.state, self.y_ac = c.FALL, c.GRAVITY

        if keys[resource.keybinding['fireball']]:
            if self.fire and self.allow_fireball:
                self.shoot(fireball_group)
        if keys[resource.keybinding['left']] and not keys[resource.keybinding['right']]:
            self.facing_right = False
            if self.x_v > -1 * self.max_x_v:
                self.x_v -= self.x_ac
        elif keys[resource.keybinding['right']] and not keys[resource.keybinding['left']]:
            self.facing_right = True
            if self.x_v < self.max_x_v:
                self.x_v += self.x_ac

    def falling(self, keys, fireball_group):
        '''determine mario's behavior when walking based on keys'''
        self.y_ac = c.GRAVITY
        if self.y_v < self.max_y_v:
            self.y_v += self.y_ac
        self.check_to_allow_fireball(keys)
        if keys[resource.keybinding['fireball']]:
            if self.fire and self.allow_fireball:
                self.shoot(fireball_group)
        if keys[resource.keybinding['left']] and not keys[resource.keybinding['right']]:
            self.facing_right = False
            if self.x_v > -1 * self.max_x_v:
                self.x_v -= self.x_ac
        elif keys[resource.keybinding['right']] and not keys[resource.keybinding['left']]:
            self.facing_right = True
            if self.x_v < self.max_x_v:
                self.x_v += self.x_ac

    def small_to_big(self):
        '''transform to big, switch frame based on time intervel'''
        frames = [self.normal_small_frames[1 - self.facing_right][7],
                  self.normal_small_frames[1 - self.facing_right][0],
                  self.normal_big_frames[1 - self.facing_right][0]]
        if self.big_transition_timer == 0:
            self.big_transition_timer = self.current_time
        for i in range(9):
            if 70 * (i + 1) <= self.current_time - self.big_transition_timer < 70 * (i + 2):
                #switch frame(small,middle,big) by i
                self.image = frames[i % 3]
                bottom, centerx = self.rect.bottom, self.rect.centerx
                self.rect = self.image.get_rect()
                self.rect.bottom, self.rect.centerx = bottom, centerx
                if i == 8:
                    self.state = c.WALK
                    self.in_transition_state = False
                    self.big_transition_timer = 0
                    self.become_big()

    def become_big(self):
        '''adjust variable related to big state'''
        self.big = True
        self.right_frames, self.left_frames = self.normal_big_frames
        self.image = self.right_frames[0] if self.facing_right else self.left_frames[0]
        bottom, x = self.rect.bottom, self.rect.x
        self.rect = self.image.get_rect()
        self.rect.bottom, self.rect.x = bottom, x

    def big_to_fire(self):
        '''transform from big to fire, switch frame based on time intervel'''
        frames = [self.fire_frames[1 - self.facing_right][3], self.green_big_frames[1 - self.facing_right][3],
                  self.red_big_frames[1 - self.facing_right][3], self.black_big_frames[1 - self.facing_right][3]]
        if self.fire_transition_timer == 0:
            self.fire_transition_timer = self.current_time
        for i in range(9):
            if 70 * (i + 1) <= self.current_time - self.fire_transition_timer < 70 * (i + 2):
                self.image = frames[i % 4]  # switch frame(fire, green, red, black) by i
                if i == 8:
                    self.state = c.WALK
                    self.fire = True
                    self.in_transition_state = False
                    self.fire_transition_timer = 0
                    self.right_frames, self.left_frames = self.fire_frames

    def big_to_small(self):
        '''transform from big/fire to small, switch frame based on time intervel'''
        frames = [self.normal_big_frames[1 - self.facing_right][4],
                  self.normal_big_frames[1 - self.facing_right][8],
                  self.normal_small_frames[1 - self.facing_right][8]]
        if self.big_transition_timer == 0:
            self.big_transition_timer = self.current_time
        for i in range(9):
            if 70 * (i + 1) <= self.current_time - self.big_transition_timer < 70 * (i + 2):
                #switch frame(small,middle,big) by i
                self.image = frames[i % 3]
                bottom, centerx = self.rect.bottom, self.rect.centerx
                self.rect = self.image.get_rect()
                self.rect.bottom, self.rect.centerx = bottom, centerx
                if i == 8:
                    self.state = c.WALK
                    self.in_transition_state = False
                    self.big_transition_timer = 0
                    self.become_small()

    def become_small(self):
        '''adjust variable related to small state'''
        self.big = False
        self.hurt_invincible_timer = self.current_time
        self.right_frames, self.left_frames = self.normal_small_frames
        self.image = self.right_frames[0] if self.facing_right else self.left_frames[0]
        bottom, x = self.rect.bottom, self.rect.x
        self.rect = self.image.get_rect()
        self.rect.bottom, self.rect.x = bottom, x

    def start_death_jump(self):
        '''call when mario die to switch mario's state into DEATH_JUMP'''
        self.state = c.DEATH_JUMP
        self.in_transition_state = True
        self.y_v = -10
        self.y_ac = 0.5
        self.frame_index = 6
        self.image = self.right_frames[self.frame_index]
        self.death_timer = self.current_time

    def death_jump(self):
        if self.current_time - self.death_timer > 200:
            self.rect.y += self.y_v
            self.y_v += 0.5

    def check_to_allow_jump(self, keys):
        '''make it not keep jumping when we keep pressing jump'''
        if not keys[resource.keybinding['jump']]:
            self.allow_jump = True

    def check_to_allow_fireball(self, keys):
        '''make it not keep shooting when we keep pressing shoot'''
        if not keys[resource.keybinding['fireball']]:
            self.allow_fireball = True

    def slide_down_pole(self):
        '''image switch when slide down the pole'''
        self.x_v, self.y_v = 0, 5
        if self.rect.bottom < 495:
            if self.flag_pole_timer == 0:
                self.flag_pole_timer = self.current_time
            elif self.current_time - self.flag_pole_timer < 65:
                self.image = self.right_frames[9]
            elif self.current_time - self.flag_pole_timer < 130:
                self.image = self.right_frames[10]
            else:
                self.flag_pole_timer = self.current_time
            self.rect.y += self.y_v
        else:
            self.flag_pole_timer = self.current_time
            self.rect.bottom = 495
            self.state = c.BOTTOM_OF_POLE

    def sitting_on_bottom(self):
        '''sit for a while'''
        if self.current_time - self.flag_pole_timer > 210:
            self.image = self.left_frames[9]
            self.x_v, self.y_v = 0, 0
            self.flag_pole_timer = 0

    def walking_to_castle(self):
        '''keep walking until reach castle'''
        self.x_v = 4
        if self.frame_index == 0:
            self.frame_index = 1
            self.walking_timer = self.current_time
        elif self.current_time - self.walking_timer > self.animation_interval():
                if self.frame_index < 3:
                    self.frame_index += 1
                else:
                    self.frame_index = 1
                self.walking_timer = self.current_time

    def end_fall(self):
        '''falling from the brick under flag pole '''
        self.frame_index = 4
        self.y_v = 6

    def check_state_update_frame(self):
        '''
        check some special state and adjust frame list to show
        '''
        self.check_if_invincible()
        self.check_if_hurt_invincible()
        self.check_if_crouching()

    def check_if_invincible(self):
        '''image switch when invincible'''
        if self.invincible:
            if self.current_time - self.invincible_start_timer < 12000:
                self.switch_frames()
            else:
                self.invincible = False
        else:
            if self.fire:
                self.right_frames, self.left_frames = self.fire_frames
            elif self.big:
                self.right_frames, self.left_frames = self.normal_big_frames
            else:
                self.right_frames, self.left_frames = self.normal_small_frames

    def switch_frames(self):
        if self.current_time - self.invincible_animation_timer > 100:
            self.invincible_animation_timer = self.current_time
            self.invincible_index = (self.invincible_index + 1) % 4
        if self.big:
            self.right_frames, self.left_frames = self.invincible_big_frames_list[self.invincible_index]
        else:
            self.right_frames, self.left_frames = self.invincible_small_frames_list[self.invincible_index]

    def check_if_hurt_invincible(self):
        if self.hurt_invincible:
            for i in range(16):
                if 200 * i <= self.current_time - self.hurt_invincible_timer < 200 * (i + 1):
                    alpha = 255 if i % 2 else 0
                    self.image.set_alpha(alpha)
                    if i == 15:
                        self.hurt_invincible = False
                        self.set_alpha255()

    def set_alpha255(self):
        '''set all images not transparent'''
        for images in self.all_frames_group:
            for image in images:
                image.set_alpha(255)

    def check_if_crouching(self):
        '''change rect'''
        if self.big and self.crouching and self.state == c.STAND:
            bottom, x = self.rect.bottom, self.rect.x
            self.frame_index = 7
            self.rect = self.right_frames[self.frame_index].get_rect()
            self.rect.bottom, self.rect.x = bottom, x


    def animation(self):
        '''choose image by index'''
        if self.in_transition_state:
            pass
        elif self.facing_right:
            self.image = self.right_frames[self.frame_index]
        else:
            self.image = self.left_frames[self.frame_index]
