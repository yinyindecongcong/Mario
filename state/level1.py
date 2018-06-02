import pygame as pg
import config as c, resource, Controller
from component import  mario, info, collider, stone, flag_pole, checkpoint, score, enemies, castle_flag

class Level1(Controller.State):
    def __init__(self):
        super().__init__()

    def startup(self, current_time, game_info):
        self.game_info = game_info
        self.game_info[c.CURRENT_TIME] = current_time
        self.game_info[c.LEVEL_STATE] = c.NOT_FROZEN
        self.game_info[c.MARIO_DEAD] = False

        self.level_over_time = 0
        self.state = c.NOT_FROZEN

        #setup elements
        self.score_group = pg.sprite.Group()
        self.info = info.Info(self.game_info, c.LEVEL1)

        self.setup_background()
        self.setup_ground()
        self.setup_pipes()
        self.setup_steps()
        self.setup_bricks()
        self.setup_coin_boxs()
        self.setup_flag_pole()
        self.setup_checkpoints()
        self.setup_enemies()
        self.setup_mario()
        self.setup_sprite_groups()

    def setup_background(self):
        self.background = resource.GFX['level_1']
        self.bg_rect = self.background.get_rect()
        self.background = pg.transform.scale(self.background, (int(self.bg_rect.width * c.BACKGROUND_MULTIPLER),
                                                               int(self.bg_rect.height * c.BACKGROUND_MULTIPLER)))
        self.bg_rect = self.background.get_rect()
        self.level = pg.Surface((self.bg_rect.width, self.bg_rect.height))
        self.level_rect = self.background.get_rect()
        self.viewport = resource.screen.get_rect()
        self.viewport.x = self.game_info[c.CAMERA_START_X]

    def setup_ground(self):
        '''setup invisible collider for four ground'''
        ground1 = collider.Collider(0, c.GROUND_HEIGHT,    2953, 60)
        ground2 = collider.Collider(3048, c.GROUND_HEIGHT,  635, 60)
        ground3 = collider.Collider(3819, c.GROUND_HEIGHT, 2735, 60)
        ground4 = collider.Collider(6647, c.GROUND_HEIGHT, 2300, 60)
        self.ground_group = pg.sprite.Group(ground1, ground2, ground3, ground4)

    def setup_pipes(self):
        '''setup invisible collider for 6 pipes'''
        pipe1 = collider.Collider(1202, 452, 83, 82)
        pipe2 = collider.Collider(1631, 409, 83, 140)
        pipe3 = collider.Collider(1973, 366, 83, 170)
        pipe4 = collider.Collider(2445, 366, 83, 170)
        pipe5 = collider.Collider(6989, 452, 83, 82)
        pipe6 = collider.Collider(7675, 452, 83, 82)
        self.pipe_group = pg.sprite.Group(pipe1, pipe2,pipe3, pipe4,pipe5, pipe6)

    def setup_steps(self):
        '''setup steps for level 1'''
        self.step_group = pg.sprite.Group()
        self.step_group.add(collider.Collider(5739, 495, 176, 44))
        self.step_group.add(collider.Collider(5739 + 44, 495 - 44, 132, 44))
        self.step_group.add(collider.Collider(5739 + 88, 495 - 88, 88, 44))
        self.step_group.add(collider.Collider(5739 + 132, 495 - 132, 44, 44))

        self.step_group.add(collider.Collider(6001, 495, 176, 44))
        self.step_group.add(collider.Collider(6001, 495 - 44, 132, 44))
        self.step_group.add(collider.Collider(6001, 495 - 88, 88, 44))
        self.step_group.add(collider.Collider(6001, 495 - 132, 44, 44))

        self.step_group.add(collider.Collider(6342, 495, 220, 44))
        self.step_group.add(collider.Collider(6342 + 44, 495 - 44, 176, 44))
        self.step_group.add(collider.Collider(6342 + 88, 495 - 88, 132, 44))
        self.step_group.add(collider.Collider(6342 + 132, 495 - 132, 88, 44))

        self.step_group.add(collider.Collider(6642, 495, 176, 44))
        self.step_group.add(collider.Collider(6642, 495 - 44, 132, 44))
        self.step_group.add(collider.Collider(6642, 495 - 88, 88, 44))
        self.step_group.add(collider.Collider(6642, 495 - 132, 44, 44))

        self.step_group.add(collider.Collider(7755, 495, 44 * 9, 44))
        self.step_group.add(collider.Collider(7755 + 44, 495 - 44, 44 * 8, 44))
        self.step_group.add(collider.Collider(7755 + 44 * 2, 495 - 88, 44 * 7, 44))
        self.step_group.add(collider.Collider(7755 + 44 * 3, 495 - 132, 44 * 6, 44))
        self.step_group.add(collider.Collider(7755 + 44 * 4, 495 - 176, 44 * 5, 44))
        self.step_group.add(collider.Collider(7755 + 44 * 5, 495 - 220, 44 * 4, 44))
        self.step_group.add(collider.Collider(7755 + 44 * 6, 495 - 264, 132, 44))
        self.step_group.add(collider.Collider(7755 + 44 * 7, 495 - 308, 88, 44))

        self.step_group.add(collider.Collider(8486, 495, 44, 44))

    def setup_bricks(self):
        self.coin_group = pg.sprite.Group()
        self.powerup_group = pg.sprite.Group()
        self.broken_brick_group = pg.sprite.Group()
        self.brick_group = pg.sprite.Group()
        self.brick_group.add(stone.Brick(858, 365, c.SIXCOINS, self.coin_group))
        self.brick_group.add(stone.Brick(944, 365))
        self.brick_group.add(stone.Brick(1030, 365))
        self.brick_group.add(stone.Brick(3299, 365))
        self.brick_group.add(stone.Brick(3385, 365))
        self.brick_group.add(stone.Brick(3430, 193))
        self.brick_group.add(stone.Brick(3473, 193))
        self.brick_group.add(stone.Brick(3516, 193))
        self.brick_group.add(stone.Brick(3559, 193))
        self.brick_group.add(stone.Brick(3602, 193))
        self.brick_group.add(stone.Brick(3645, 193))
        self.brick_group.add(stone.Brick(3688, 193))
        self.brick_group.add(stone.Brick(3731, 193))
        self.brick_group.add(stone.Brick(3901, 193))
        self.brick_group.add(stone.Brick(3944, 193))
        self.brick_group.add(stone.Brick(3987, 193))
        self.brick_group.add(stone.Brick(4030, 365, c.SIXCOINS, self.coin_group))
        self.brick_group.add(stone.Brick(4287, 365))
        self.brick_group.add(stone.Brick(4330, 365, c.STAR, self.powerup_group))
        self.brick_group.add(stone.Brick(5058, 365))
        self.brick_group.add(stone.Brick(5187, 193))
        self.brick_group.add(stone.Brick(5230, 193))
        self.brick_group.add(stone.Brick(5273, 193))
        self.brick_group.add(stone.Brick(5488, 193))
        self.brick_group.add(stone.Brick(5574, 193))
        self.brick_group.add(stone.Brick(5617, 193))
        self.brick_group.add(stone.Brick(5531, 365))
        self.brick_group.add(stone.Brick(5574, 365))
        self.brick_group.add(stone.Brick(7202, 365))
        self.brick_group.add(stone.Brick(7245, 365))
        self.brick_group.add(stone.Brick(7331, 365))

    def setup_coin_boxs(self):
        self.coin_box_group = pg.sprite.Group()
        """Creates all the coin boxes and puts them in a sprite group"""
        self.coin_box_group.add(stone.Coin_box(685, 365, c.COIN, self.coin_group))
        self.coin_box_group.add(stone.Coin_box(901, 365, c.MUSHROOM, self.powerup_group))
        self.coin_box_group.add(stone.Coin_box(987, 365, c.COIN, self.coin_group))
        self.coin_box_group.add(stone.Coin_box(943, 193, c.COIN, self.coin_group))
        self.coin_box_group.add(stone.Coin_box(3342, 365, c.MUSHROOM, self.powerup_group))
        self.coin_box_group.add(stone.Coin_box(4030, 193, c.COIN, self.coin_group))
        self.coin_box_group.add(stone.Coin_box(4544, 365, c.COIN, self.coin_group))
        self.coin_box_group.add(stone.Coin_box(4672, 365, c.COIN, self.coin_group))
        self.coin_box_group.add(stone.Coin_box(4672, 193, c.MUSHROOM, self.powerup_group))
        self.coin_box_group.add(stone.Coin_box(4800, 365, c.COIN, self.coin_group))
        self.coin_box_group.add(stone.Coin_box(5531, 193, c.COIN, self.coin_group))
        self.coin_box_group.add(stone.Coin_box(7288, 365, c.COIN, self.coin_group))

    def setup_flag_pole(self):
        self.flag = flag_pole.Flag(8505, 96)
        self.flag_pole_group = pg.sprite.Group(self.flag)
        self.flag_pole_group.add(flag_pole.Pole(8505, 97))
        self.flag_pole_group.add(flag_pole.Pole_ball(8505, 97)) #flag_top

    def setup_enemies(self):
        """Creates all the enemies and stores them in a list of lists."""
        goomba0 = enemies.Goomba()
        goomba1 = enemies.Goomba()
        goomba2 = enemies.Goomba()
        goomba3 = enemies.Goomba()
        goomba4 = enemies.Goomba(bottom=193)
        goomba5 = enemies.Goomba(bottom=193)
        goomba6 = enemies.Goomba()
        goomba7 = enemies.Goomba()
        goomba8 = enemies.Goomba()
        goomba9 = enemies.Goomba()
        goomba10 = enemies.Goomba()
        goomba11 = enemies.Goomba()
        goomba12 = enemies.Goomba()
        goomba13 = enemies.Goomba()
        goomba14 = enemies.Goomba()
        goomba15 = enemies.Goomba()

        koopa0 = enemies.Koopa()

        enemy_group1 = pg.sprite.Group(goomba0)
        enemy_group2 = pg.sprite.Group(goomba1)
        enemy_group3 = pg.sprite.Group(goomba2, goomba3)
        enemy_group4 = pg.sprite.Group(goomba4, goomba5)
        enemy_group5 = pg.sprite.Group(goomba6, goomba7)
        enemy_group6 = pg.sprite.Group(koopa0)
        enemy_group7 = pg.sprite.Group(goomba8, goomba9)
        enemy_group8 = pg.sprite.Group(goomba10, goomba11)
        enemy_group9 = pg.sprite.Group(goomba12, goomba13)
        enemy_group10 = pg.sprite.Group(goomba14, goomba15)

        self.enemy_group = pg.sprite.Group()
        self.enemy_group_list = [enemy_group1,enemy_group2,enemy_group3,enemy_group4,
                                 enemy_group5,enemy_group6,enemy_group7,enemy_group8,
                                 enemy_group9,enemy_group10]
        #when reach checkpoint, add correspondent enemy subgroup to enemy_group

    def setup_checkpoints(self):
        '''invisible check point to check if elements like enemies should appear'''
        self.check_point_group = pg.sprite.Group()
        self.check_point_group.add(checkpoint.Checkpoint(510, "1"))
        self.check_point_group.add(checkpoint.Checkpoint(1400, '2'))
        self.check_point_group.add(checkpoint.Checkpoint(1740, '3'))
        self.check_point_group.add(checkpoint.Checkpoint(3080, '4'))
        self.check_point_group.add(checkpoint.Checkpoint(3750, '5'))
        self.check_point_group.add(checkpoint.Checkpoint(4150, '6'))
        self.check_point_group.add(checkpoint.Checkpoint(4470, '7'))
        self.check_point_group.add(checkpoint.Checkpoint(4950, '8'))
        self.check_point_group.add(checkpoint.Checkpoint(5100, '9'))
        self.check_point_group.add(checkpoint.Checkpoint(6800, '10'))
        self.check_point_group.add(checkpoint.Checkpoint(8504, '11', 5, 6))
        self.check_point_group.add(checkpoint.Checkpoint(8775, '12'))
        self.check_point_group.add(checkpoint.Checkpoint(2740, 'secret_mushroom', 360, 40, 12))

    def setup_mario(self):
        self.mario = mario.Mario()
        self.mario.rect.x = self.game_info[c.CAMERA_START_X] + 110
        self.mario.rect.bottom = c.GROUND_HEIGHT
        self.mario_group = pg.sprite.Group(self.mario)

    def setup_sprite_groups(self):
        self.ground_pipe_step_group = pg.sprite.Group(self.ground_group, self.pipe_group, self.step_group)
        self.die_later_group = pg.sprite.Group()
        self.shell_group = pg.sprite.Group()

    def update(self, screen, keys, current_time):
        self.current_time = current_time
        self.game_info[c.CURRENT_TIME] = current_time
        self.handle_keys(keys)
        self.is_timeout()
        self.blit_all(screen)

    def handle_keys(self, keys):
        if self.state == c.NOT_FROZEN:
            self.update_all_sprites(keys)
        elif self.state == c.FROZEN:
            self.update_when_frozen(keys)
        elif self.state == c.IN_CASTLE:
            self.update_in_castle()
        elif self.state == c.FLAG_AND_FIREWORKS:
            self.update_castle_flag()

    def update_when_frozen(self, keys):
        self.mario.update(keys, self.game_info, self.powerup_group)
        self.info.update(self.game_info, self.mario)
        self.flag_pole_group.update()
        self.check_flag()
        self.check_frozen()
        self.check_mario_death()
        self.score_group.update()
        self.update_viewport()

    def update_in_castle(self):
        self.score_group.update()
        self.info.update(self.game_info)
        if self.info.state == c.END_OF_LEVEL:
            self.state = c.FLAG_AND_FIREWORKS
            self.flag_pole_group.add(castle_flag.Castle_flag(8745, 322))
            print('1212', self.state)

    def update_castle_flag(self):
        print('2323')
        self.score_group.update()
        self.info.update(self.game_info)
        self.flag_pole_group.update()
        if self.level_over_time == 0:
            self.level_over_time = self.current_time
        elif self.current_time - self.level_over_time > 1500:
            self.next_state = c.GAME_OVER
            self.set_game_info()
            self.level_over_time = 0

    def set_game_info(self):
        self.done = True
        if self.game_info[c.TOP_SCORE] < self.game_info[c.SCORE]:
            self.game_info[c.TOP_SCORE] = self.game_info[c.SCORE]
        if self.mario.dead:
            self.game_info[c.LIVES] -= 1
            if self.game_info[c.LIVES] == 0:
                self.next_state = c.GAME_OVER
                self.game_info[c.CAMERA_START_X] = 0
            elif self.game_info[c.LIVES]:
                self.next_state = c.LOAD_SCREEN
                if self.mario.rect.x > 3670:
                    self.game_info[c.CAMERA_START_X] = 3440




    def is_timeout(self):
        if self.info.time <= 0 and not self.mario.dead and \
                not (self.state == c.IN_CASTLE or self.state == c.FLAG_AND_FIREWORKS):
            self.state = c.FROZEN
            self.mario.dead = 1
            self.game_info[c.LEVEL_STATE] = c.FROZEN
            self.game_info[c.MARIO_DEAD] = True
            self.mario.start_death_jump()

    def update_all_sprites(self, keys):
        self.mario.update(keys, self.game_info, self.powerup_group)
        self.powerup_group.update(self.game_info)
        self.brick_group.update(self.game_info)
        self.broken_brick_group.update()
        self.coin_box_group.update(self.game_info)
        self.coin_group.update(self.game_info)
        self.flag_pole_group.update()
        self.check_point_check()
        self.score_group.update()
        self.enemy_group.update(self.game_info)
        self.die_later_group.update(self.game_info)
        self.check_flag()
        self.check_frozen()
        self.adjust_sprites_position()
        self.check_mario_death()
        self.update_viewport()
        self.info.update(self.game_info, self.mario)

    def adjust_sprites_position(self):
        self.adjust_enemies_position()
        self.adjust_powerup_position()
        self.adjust_mario_position()

    def check_point_check(self):
        '''check if is mario reaching any checkpoint'''
        reach_point = pg.sprite.spritecollideany(self.mario, self.check_point_group)
        if reach_point:
            #if is the first ten checkpoint, add correspondent enemies
            if reach_point.name != 'secret_mushroom' and \
                    int(reach_point.name) in range(1, 11):
                for index, enemy in enumerate(self.enemy_group_list[int(reach_point.name) - 1]):
                    enemy.rect.x = self.viewport.right + index * 60
                self.enemy_group.add(self.enemy_group_list[int(reach_point.name) - 1])
            #flag point
            elif reach_point.name == '11':
                self.mario.invincible = False
                self.mario.state = c.FLAGPOLE
                self.mario.in_transition_state = True
                self.state = self.game_info[c.LEVEL_STATE] = c.FROZEN
                self.mario.rect.right = reach_point.rect.right
                if self.mario.rect.bottom < self.flag.rect.y:
                    self.mario.rect.bottom = self.flag.rect.y
                self.flag.state = c.MOVE
                self.get_flag_score()
            #end
            elif reach_point.name == '12':
                self.state = c.IN_CASTLE
                self.mario.state = c.STAND
                self.mario.in_castle = True
                self.mario.kill()
                self.info.state = c.FAST_COUNT_DOWN
                print('999xxx', self.state)
            #1up
            elif reach_point.name == 'secret_mushroom' and self.mario.y_v < 0:
                mushroom_box = stone.Coin_box(reach_point.rect.x, reach_point.rect.bottom - 40,
                                              c.LIFE_MUSHROOM, self.powerup_group)
                mushroom_box.collide(self.score_group)
                self.coin_box_group.add(mushroom_box)
                self.mario.rect.top = reach_point.rect.bottom
                self.mario.y_v = 7
                self.mario.state = c.FALL
            reach_point.kill()

    def get_flag_score(self):
        '''call to decide the score mario get by jump to flag_pole'''
        x, y = 8518, 470
        if self.mario.rect.bottom < 150:
            self.score_group.add(score.Score(x, y, 5000))
            self.game_info[c.SCORE] += 5000
        elif self.mario.rect.bottom < 250:
            self.score_group.add(score.Score(x, y, 2000))
            self.game_info[c.SCORE] += 2000
        elif self.mario.rect.bottom < 350:
            self.score_group.add(score.Score(x, y, 800))
            self.game_info[c.SCORE] += 800
        elif self.mario.rect.bottom < 450:
            self.score_group.add(score.Score(x, y, 400))
            self.game_info[c.SCORE] += 400
        else:
            self.score_group.add(score.Score(x, y, 100))
            self.game_info[c.SCORE] += 100

    def adjust_mario_position(self):
        #TODO
        '''adjust mario position based on its speed and collision'''
        if not self.mario.in_transition_state:
            self.mario.rect.x += round(self.mario.x_v)
            self.check_mario_x_collision()
            if not self.mario.in_transition_state:
                self.mario.rect.y += round(self.mario.y_v)
                self.check_mario_y_collision()
        if self.mario.rect.x < self.viewport.x:
            self.mario.rect.x = self.viewport.x

    def check_mario_x_collision(self):
        #TODO
        collider = pg.sprite.spritecollideany(self.mario, self.ground_pipe_step_group)
        brick = pg.sprite.spritecollideany(self.mario, self.brick_group)
        coin_box = pg.sprite.spritecollideany(self.mario, self.coin_box_group)
        enemy = pg.sprite.spritecollideany(self.mario, self.enemy_group)
        if collider:
            self.adjust_mario_x_collision(collider)
        elif brick:
            self.adjust_mario_x_collision(brick)
        elif coin_box:
            self.adjust_mario_x_collision(coin_box)
        elif enemy:
            self.adjust_mario_enemy_x_collision(enemy)

    def adjust_mario_x_collision(self, collider):
        '''if collide with collider(pile, step, box...), adjust x axis'''
        if self.mario.rect.x < collider.rect.x:
            self.mario.rect.right = collider.rect.left
        else:
            self.mario.rect.left = collider.rect.right
        self.mario.x_v = 0

    def adjust_mario_enemy_x_collision(self, enemy):
        print('xxx')
        #invincible
        if self.mario.invincible:
            self.game_info[c.SCORE] += 100
            self.score_group.add(score.Score(self.mario.rect.x, self.mario.rect.y, 100))
            enemy.kill()
            enemy.start_death_jump()
            self.die_later_group.add(enemy)
        elif self.mario.hurt_invincible:
            pass
        #hurt mario
        elif enemy.state == c.WALK or enemy.state == c.FALL or enemy.state == c.SLIDE:
            if self.mario.big:
                self.mario.fire = False
                self.mario.state = c.BIG_TO_SMALL
                self.mario.in_transition_state = True
                self.mario.hurt_invincible = True
                self.convert_fireflower_to_mushroom()
                print('tt', self.mario.state)
            else:
                self.state = c.FROZEN
                self.game_info[c.LEVEL_STATE] = c.FROZEN
                self.game_info[c.MARIO_DEAD] = True
                self.mario.start_death_jump()
                print(self.mario.state)
        #just a still shell
        elif enemy.state == c.JUMPED_ON:
            if self.mario.rect.x < enemy.rect.x: #left -> right
                enemy.rect.x = self.mario.rect.right
                enemy.facing_right = True
            else:  #right -> left
                enemy.rect.right = self.mario.rect.left
                enemy.facing_right = False
            self.game_info[c.SCORE] += 400
            self.score_group.add(score.Score(self.mario.rect.x, self.mario.rect.y, 400))
            enemy.state = c.SLIDE

    def check_mario_y_collision(self):
        print('qqq')
        print(self.mario.state)
        collider = pg.sprite.spritecollideany(self.mario, self.ground_pipe_step_group)
        brick = pg.sprite.spritecollideany(self.mario, self.brick_group)
        coin_box = pg.sprite.spritecollideany(self.mario, self.coin_box_group)
        powerup = pg.sprite.spritecollideany(self.mario, self.powerup_group)
        enemy = pg.sprite.spritecollideany(self.mario, self.enemy_group)
        if collider:
            self.adjust_mario_y_ground_collision(collider)
            print(self.mario.state)
        elif brick:
            self.adjust_mario_y_brick_collision(brick)
        elif coin_box:
            self.adjust_mario_y_coin_box_collision(coin_box)
        elif powerup:
            self.adjust_mario_powerup_collision(powerup)
        elif enemy:
            self.adjust_mario_enemy_y_collision(enemy)
        self.check_falling()
        print(self.mario.state)


    def adjust_mario_y_ground_collision(self, collider):
        '''if collide with collider(ground, step, box...), adjust y axis'''
        if self.mario.rect.bottom < collider.rect.bottom: #high -> low
            self.mario.rect.bottom = collider.rect.top
            self.mario.y_v = 0
            if self.mario.state == c.END_OF_LEVEL_FALL:
                self.mario.state = c.WALKING_TO_CASTLE
            elif not self.mario.state == c.WALKING_TO_CASTLE:
                self.mario.state = c.WALK
        else:                                             #low -> high
            self.mario.rect.top = collider.rect.bottom
            self.mario.y_v = 7
            self.mario.state = c.FALL

    def adjust_mario_y_brick_collision(self, brick):
        '''if collide with brick, adjust both mario and brick'''
        if self.mario.rect.bottom > brick.rect.bottom:  #low -> high
            if brick.state == c.RESTING:
                self.check_if_enemy_on_brick(brick)
                if self.mario.big and not brick.content:
                    rect = brick.rect
                    self.broken_brick_group.add(stone.Broken_brick(rect.x, rect.y - rect.height / 2, -2, -12))
                    self.broken_brick_group.add(stone.Broken_brick(rect.right, rect.y - rect.height / 2, 2, -12))
                    self.broken_brick_group.add(stone.Broken_brick(rect.x, rect.y, -2, -6))
                    self.broken_brick_group.add(stone.Broken_brick(rect.right, rect.y, 2, -6))
                    brick.kill()
                else:
                    if brick.coins > 0:
                        self.game_info[c.COIN_TOTAL] += 1
                        self.game_info[c.SCORE] += 200
                    brick.collide(self.score_group)
            elif brick.state == c.USELESS:
                pass #sound
            self.mario.state = c.FALL
            self.mario.y_v = 7
            self.mario.rect.top = brick.rect.bottom
        else:                                           #high -> low
            self.mario.rect.bottom = brick.rect.top
            self.mario.y_v = 0
            self.mario.state = c.WALK

    def check_if_enemy_on_brick(self, brick):
        brick.rect.y -= 5
        enemy = pg.sprite.spritecollideany(brick, self.enemy_group)
        if enemy:
            enemy.kill()
            enemy.start_death_jump()
            self.die_later_group.add(enemy)
            self.game_info[c.SCORE] += 200
            self.score_group.add(score.Score(enemy.rect.x, enemy.rect.y, 200))
        brick.rect.y += 5

    def adjust_mario_y_coin_box_collision(self, coin_box):
        '''if collide with coin_box, adjust both mario and coin_box'''
        if self.mario.rect.bottom > coin_box.rect.bottom:  # low -> high
            if coin_box.state == c.RESTING:
                self.check_if_enemy_on_brick(coin_box)
                if coin_box.content == c.COIN:
                    self.game_info[c.COIN_TOTAL] += 1
                    self.game_info[c.SCORE] += 200
                coin_box.collide(self.score_group)
            elif coin_box.state == c.USELESS:
                pass  # sound
            self.mario.state = c.FALL
            self.mario.y_v = 7
            self.mario.rect.top = coin_box.rect.bottom
        else:  # high -> low
            self.mario.rect.bottom = coin_box.rect.top
            self.mario.y_v = 0
            self.mario.state = c.WALK

    def adjust_mario_powerup_collision(self, powerup):
        if powerup.name == c.LIFE_MUSHROOM:
            self.score_group.add(score.Score(self.mario.rect.x + 20, self.mario.rect.y, c.ONEUP))
            self.game_info[c.LIVES] += 1
            powerup.kill()
        elif not powerup.name == c.FIREBALL:
            powerup.kill()
            self.game_info[c.SCORE] += 1000
            self.score_group.add(score.Score(self.mario.rect.x + 20, self.mario.rect.y, 1000))
        if powerup.name == c.STAR:
            self.mario.invincible = True
            self.mario.invincible_start_timer = self.current_time
        elif powerup.name == c.MUSHROOM:
            self.mario.state = c.SMALL_TO_BIG
            self.mario.in_transition_state = True
            self.convert_mushroom_to_fireflower()
        elif powerup.name == c.FIREFLOWER:
            if self.mario.big and not self.mario.fire:
                self.mario.state = c.BIG_TO_FIRE
                self.mario.in_transition_state = True
            elif not self.mario.big:
                self.mario.state = c.SMALL_TO_BIG
                self.convert_mushroom_to_fireflower()
                self.mario.in_transition_state = True

    def convert_mushroom_to_fireflower(self):
        for coin_box in self.coin_box_group:
            if coin_box.content == c.MUSHROOM:
                coin_box.content = c.FIREFLOWER

    def convert_fireflower_to_mushroom(self):
        for coin_box in self.coin_box_group:
            if coin_box.content == c.FIREFLOWER:
                coin_box.content = c.MUSHROOM

    def adjust_mario_enemy_y_collision(self, enemy):
        print('yyy')
        if self.state == c.FROZEN:
            return
        if self.mario.invincible:
            self.game_info[c.SCORE] += 100
            self.score_group.add(score.Score(self.mario.rect.x, self.mario.rect.y, 100))
            enemy.kill()
            enemy.start_death_jump()
            self.die_later_group.add(enemy)
        elif self.mario.rect.top < enemy.rect.top:  #high to low
            if enemy.name == 'Goomba':
                self.game_info[c.SCORE] += 100
                self.score_group.add(score.Score(self.mario.rect.x, self.mario.rect.y, 100))
                enemy.kill()
                enemy.state = c.JUMPED_ON
                self.die_later_group.add(enemy)
            #stop sliding shell or make it a shell
            elif enemy.state == c.SLIDE or enemy.state == c.WALK:
                enemy.state = c.JUMPED_ON
                enemy.x_v, enemy.y_v = 0, 0
            # mario jump on shell
            elif enemy.state == c.JUMPED_ON:
                if self.mario.rect.centerx < enemy.rect.centerx:
                    enemy.facing_right = True
                    enemy.rect.left = self.mario.rect.right
                else:
                    enemy.facing_right = False
                    enemy.rect.right = self.mario.rect.left
                enemy.state = c.SLIDE
                self.game_info[c.SCORE] += 200
                self.score_group.add(score.Score(self.mario.rect.x, self.mario.rect.y, 200))

            self.mario.bottom = enemy.rect.top
            self.mario.y_v = -10
            self.mario.state = c.JUMP
        else: #low to high, hurts
            if self.mario.hurt_invincible:
                return
            elif self.mario.big:
                self.mario.fire = False
                self.mario.in_transition_state = True
                self.mario.state = c.BIG_TO_SMALL
                self.mario.hurt_invincible = True
                self.convert_fireflower_to_mushroom()
            else:
                self.state = c.FROZEN
                self.game_info[c.LEVEL_STATE] = c.FROZEN
                self.game_info[c.MARIO_DEAD] = True
                self.mario.start_death_jump()

    def check_falling(self):
        '''check if mario is at the place that is higher than ground, pipe, brick, etc'''
        self.mario.rect.y += 1
        test_group = pg.sprite.Group(self.ground_pipe_step_group, self.brick_group, self.coin_box_group)
        if not pg.sprite.spritecollideany(self.mario, test_group):
            if self.mario.state == c.WALKING_TO_CASTLE:
                self.mario.state = c.END_OF_LEVEL_FALL
            if self.mario.state == c.STAND or self.mario.state == c.WALK:
                self.mario.state = c.FALL
        self.mario.rect.y -= 1

    def adjust_powerup_position(self):
        for powerup in self.powerup_group:
            if powerup.name == c.MUSHROOM or powerup.name == c.LIFE_MUSHROOM:
                self.adjust_mushroom_position(powerup)
            elif powerup.name == c.STAR:
                self.adjust_star_position(powerup)
            elif powerup.name == c.FIREBALL:
                self.adjust_fireball_position(powerup)

    def adjust_mushroom_position(self, mushroom):
        if mushroom.state != c.UP:
            mushroom.rect.x += mushroom.x_v
            self.check_mushroom_x_collision(mushroom)
            mushroom.rect.y += mushroom.y_v
            self.check_mushroom_y_collision(mushroom)
            self.if_off_screen(mushroom)

    def check_mushroom_x_collision(self, mushroom):
        test_group = pg.sprite.Group(self.ground_pipe_step_group, self.brick_group, self.coin_box_group)
        collider = pg.sprite.spritecollideany(mushroom, test_group)
        if collider:
            #if collide with collider(pile, step, box...), adjust x axis
            if mushroom.rect.x < collider.rect.x:
                mushroom.rect.right = collider.rect.left
                mushroom.facing_right = False
            else:
                mushroom.rect.left = collider.rect.right
                mushroom.Facing_right = True

    def check_mushroom_y_collision(self, mushroom):
        test_group = pg.sprite.Group(self.ground_pipe_step_group, self.brick_group, self.coin_box_group)
        collider = pg.sprite.spritecollideany(mushroom, test_group)
        if collider:
            mushroom.rect.bottom = collider.rect.top
            mushroom.state = c.SLIDE
            mushroom.y_v = 0
        self.check_powerup_falling(mushroom)

    def check_powerup_falling(self, powerup):
        powerup.rect.y += 1
        test_group = pg.sprite.Group(self.ground_pipe_step_group, self.brick_group, self.coin_box_group)
        if not pg.sprite.spritecollideany(powerup, test_group):
            powerup.state = c.FALL
        powerup.rect.y -= 1

    def if_off_screen(self, item):
        if item.rect.x > self.viewport.right + 100 or item.rect.x < self.viewport.left - 100 \
                or item.rect.y > self.viewport.bottom:
            item.kill()

    def adjust_star_position(self, star):
        if star.state != c.UP:
            star.rect.x += star.x_v
            self.check_mushroom_x_collision(star)
            star.rect.y += star.y_v
            self.check_star_y_collision(star)
            self.if_off_screen(star)

    def check_star_y_collision(self, star):
        collider = pg.sprite.spritecollideany(star, self.ground_pipe_step_group)
        brick = pg.sprite.spritecollideany(star, self.brick_group)
        coin_box = pg.sprite.spritecollideany(star, self.coin_box_group)
        if collider:
            self.adjust_star_y_collision(collider, star)
        elif brick:
            self.adjust_star_y_collision(brick, star)
        elif coin_box:
            self.adjust_star_y_collision(coin_box, star)
        self.check_powerup_falling(star)

    def adjust_star_y_collision(self, collider, star):
        if star.rect.bottom > collider.rect.bottom:  # low -> high
            star.state = c.FALL
            star.y_v = 0
            star.rect.top = collider.rect.bottom
        else:  # high -> low
            star.rect.bottom = collider.rect.top
            star.y_v = -13
            star.state = c.FALL

    def adjust_fireball_position(self, fireball):
        fireball.rect.x += fireball.x_v
        self.check_fireball_x_collision(fireball)
        if fireball.state != c.EXPLODING:
            fireball.rect.y += fireball.y_v
            self.check_fireball_y_collision(fireball)
            fireball.y_v += fireball.gravity
            self.if_off_screen(fireball)

    def check_fireball_x_collision(self, fireball):
        #TODO
        test_group = pg.sprite.Group(self.ground_pipe_step_group, self.brick_group, self.coin_box_group)
        collider = pg.sprite.spritecollideany(fireball, test_group)
        enemy = pg.sprite.spritecollideany(fireball, self.enemy_group)
        if collider:
            fireball.kill()
            self.die_later_group.add(fireball)
            fireball.explode()
        elif enemy:
            enemy.kill()
            enemy.start_death_jump()
            self.die_later_group.add(enemy)
            self.game_info[c.SCORE] += 200
            self.score_group.add(score.Score(enemy.rect.x, enemy.rect.y, 200))
            fireball.kill()
            self.die_later_group.add(fireball)
            fireball.explode()

    def check_fireball_y_collision(self, fireball):
        test_group = pg.sprite.Group(self.ground_pipe_step_group, self.brick_group, self.coin_box_group)
        collider = pg.sprite.spritecollideany(fireball, test_group)
        enemy = pg.sprite.spritecollideany(fireball, self.enemy_group)
        if collider:
            fireball.rect.bottom = collider.rect.top
            fireball.bounce()
        elif enemy:
            fireball.kill()
            self.die_later_group.add(fireball)
            fireball.explode()
            enemy.kill()
            enemy.start_death_jump()
            self.die_later_group.add(enemy)
            self.game_info[c.SCORE] += 200
            self.score_group.add(score.Score(enemy.rect.x, enemy.rect.y, 200))

    def adjust_enemies_position(self):
        for enemy in self.enemy_group:
            enemy.rect.x += enemy.x_v
            self.check_enemy_x_collision(enemy)
            if not enemy.state == c.DEATH_JUMP:
                enemy.rect.y += enemy.y_v
                self.check_enemy_y_collision(enemy)
            self.if_off_screen(enemy)

    def check_enemy_x_collision(self, enemy):
        '''check if collide with colliders or partner'''
        enemy.kill() #kill first
        test_group = pg.sprite.Group(self.ground_pipe_step_group, self.brick_group, self.coin_box_group)
        collider = pg.sprite.spritecollideany(enemy, test_group)
        enemy_collider = pg.sprite.spritecollideany(enemy, self.enemy_group)
        if collider:
            if enemy.facing_right:
                enemy.rect.right = collider.rect.left
                enemy.facing_right = False
            else:
                enemy.rect.left = collider.rect.right
                enemy.facing_right = True
            enemy.x_v = 2 if enemy.facing_right else -2
        elif enemy_collider:
            if enemy.name == 'Goomba' and enemy_collider.name == 'Koopa':
                self.die_later_group.add(enemy)
                enemy.start_death_jump()
                self.game_info[c.SCORE] += 100
                self.score_group.add(score.Score(enemy.rect.x, enemy.rect.y, 100))
                return
            elif enemy.name == 'Koopa' and enemy_collider.name == 'Goomba':
                enemy_collider.kill()
                self.die_later_group.add(enemy_collider)
                enemy_collider.start_death_jump()
                print(enemy_collider.state)
                self.game_info[c.SCORE] += 100
                self.score_group.add(score.Score(enemy_collider.rect.x, enemy_collider.rect.y, 100))
            elif enemy.facing_right:
                enemy.facing_right = False
                enemy_collider.facing_right = True
                enemy.rect.right = enemy_collider.rect.left
            else:
                enemy.rect.left = enemy_collider.rect.right
                enemy.facing_right = True
                enemy_collider.facing_right = False
            enemy.x_v = 2 if enemy.facing_right else -2
            enemy_collider.x_v = 2 if enemy_collider.facing_right else -2
        self.enemy_group.add(enemy)

    def check_enemy_y_collision(self, enemy):
        test_group = pg.sprite.Group(self.ground_pipe_step_group, self.brick_group, self.coin_box_group)
        collider = pg.sprite.spritecollideany(enemy, test_group)
        if collider:
            enemy.rect.bottom = collider.rect.top
            enemy.state = c.WALK
            enemy.y_v = 0
        self.check_powerup_falling(enemy)

    def check_flag(self):
        if self.flag.state == c.BOTTOM_OF_POLE and self.mario.state == c.BOTTOM_OF_POLE:
            print('zzz')
            self.mario.state = c.WALKING_TO_CASTLE
            self.mario.in_transition_state = False
            right = self.mario.rect.right
            self.mario.rect.x = right

    def check_frozen(self):
        if self.state == c.FLAG_AND_FIREWORKS or self.state == c.IN_CASTLE:
            return
        if self.mario.in_transition_state:
            self.game_info[c.LEVEL_STATE] = self.state = c.FROZEN
        else:
            self.game_info[c.LEVEL_STATE] = self.state = c.NOT_FROZEN

    def check_mario_death(self):
        if self.mario.rect.top >= self.viewport.bottom:
            self.mario.dead = True
            self.state = c.FROZEN
            self.game_info[c.MARIO_DEAD] = True
        if self.mario.dead:
            if self.level_over_time == 0:
                self.level_over_time = self.current_time
            elif self.current_time - self.level_over_time > 1500:
                self.set_game_info()
                self.level_over_time = 0

    def update_viewport(self):
        one_third = self.viewport.x + self.viewport.width // 3
        mario_centerx = self.mario.rect.centerx
        if self.mario.x_v > 0 and mario_centerx >= one_third:
            multiple = 0.5 if mario_centerx < self.viewport.centerx else 1
            self.viewport.x = self.viewport.x + multiple * self.mario.x_v #calc the next viewport
            if self.viewport.centerx < self.mario.rect.centerx:           #if exceed 1/2, adjust
                self.viewport.centerx = self.mario.rect.centerx
            if self.viewport.right > self.level_rect.right:               #if it is the end
                self.viewport.right = self.level_rect.right
            print('aaa', self.viewport.centerx, self.mario.rect.x)

    def blit_all(self, screen):
        print(self.mario.state)
        print(self.mario.x_v)
        print(self.mario.rect)
        print(self.state)
        self.level.blit(self.background, self.viewport, self.viewport) #draw background on level image
        self.powerup_group.draw(self.level)
        self.brick_group.draw(self.level)
        self.coin_box_group.draw(self.level)
        self.coin_group.draw(self.level)
        self.broken_brick_group.draw(self.level)
        self.die_later_group.draw(self.level)
        self.flag_pole_group.draw(self.level)
        self.mario_group.draw(self.level)
        self.enemy_group.draw(self.level)
        for score in self.score_group:
            score.draw(self.level)
        screen.blit(self.level, (0,0), self.viewport)
        self.info.draw(screen)





