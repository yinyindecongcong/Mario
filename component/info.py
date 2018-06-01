import pygame as pg
import config as c, resource
from component import flashing_coin
class Character(pg.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()

class Info():
    '''
    class for showing info like coins, scores, mario, title box, etc;
    with entries including:
    image_dict(numbers\letters\chars) --- info string showing;
    flushing_coin --- image of coin, which could blink
    mario --- also for info showing, just need image
    (various) labels --- determined by state, with special info to show;
    '''
    def __init__(self, game_info, state):
        self.state = state
        self.game_info = game_info
        self.current_time = 0
        self.time = 401
        self.image_sheet = resource.GFX['text_images']
        self.coin_total = game_info[c.COIN_TOTAL]
        self.score = game_info[c.SCORE]
        self.top_score = game_info[c.TOP_SCORE]
        self.lives = game_info[c.LIVES]

        self.create_image_dict()
        self.create_score_group() #initialize score 000000
        self.create_info_labels()
        self.create_coin_counter() #initialize coin *00
        self.create_flushing_coin()
        self.create_menu_labels()
        self.create_mario_image()
        self.create_load_screen_labels()
        self.create_count_clock()


    def create_image_dict(self):
        '''create image dict for all characters--numbers, letters and so on'''
        self.image_dict = {}
        image_list = []
        #numbers 0 --- 9
        image_list.append(self.get_image(3, 230, 7, 7))
        image_list.append(self.get_image(12, 230, 7, 7))
        image_list.append(self.get_image(19, 230, 7, 7))
        image_list.append(self.get_image(27, 230, 7, 7))
        image_list.append(self.get_image(35, 230, 7, 7))
        image_list.append(self.get_image(43, 230, 7, 7))
        image_list.append(self.get_image(51, 230, 7, 7))
        image_list.append(self.get_image(59, 230, 7, 7))
        image_list.append(self.get_image(67, 230, 7, 7))
        image_list.append(self.get_image(75, 230, 7, 7))
        #letters
        image_list.append(self.get_image(83, 230, 7, 7))
        image_list.append(self.get_image(91, 230, 7, 7))
        image_list.append(self.get_image(99, 230, 7, 7))
        image_list.append(self.get_image(107, 230, 7, 7))
        image_list.append(self.get_image(115, 230, 7, 7))
        image_list.append(self.get_image(123, 230, 7, 7))
        image_list.append(self.get_image(3, 238, 7, 7))
        image_list.append(self.get_image(11, 238, 7, 7))
        image_list.append(self.get_image(20, 238, 7, 7))
        image_list.append(self.get_image(27, 238, 7, 7))
        image_list.append(self.get_image(35, 238, 7, 7))
        image_list.append(self.get_image(44, 238, 7, 7))
        image_list.append(self.get_image(51, 238, 7, 7))
        image_list.append(self.get_image(59, 238, 7, 7))
        image_list.append(self.get_image(67, 238, 7, 7))
        image_list.append(self.get_image(75, 238, 7, 7))
        image_list.append(self.get_image(83, 238, 7, 7))
        image_list.append(self.get_image(91, 238, 7, 7))
        image_list.append(self.get_image(99, 238, 7, 7))
        image_list.append(self.get_image(108, 238, 7, 7))
        image_list.append(self.get_image(115, 238, 7, 7))
        image_list.append(self.get_image(123, 238, 7, 7))
        image_list.append(self.get_image(3, 246, 7, 7))
        image_list.append(self.get_image(11, 246, 7, 7))
        image_list.append(self.get_image(20, 246, 7, 7))
        image_list.append(self.get_image(27, 246, 7, 7))
        #space, -, *
        image_list.append(self.get_image(48, 248, 7, 7))
        image_list.append(self.get_image(68, 247, 7, 7))
        image_list.append(self.get_image(75, 247, 6, 6))
        character_string = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ -*'
        for character, image in zip(character_string, image_list):
            self.image_dict[character] = image

    def create_score_group(self):
        self.score_image = []
        self.create_label(self.score_image, '000000', 75, 55)

    def create_info_labels(self):
        self.time_label = []
        self.world_label = []
        self.mario_label = []
        self.level_label = []
        self.create_label(self.time_label, 'TIME', 625, 30)
        self.create_label(self.world_label, 'WORLD', 450, 30)
        self.create_label(self.mario_label, 'MARIO', 75, 30)
        self.create_label(self.level_label, '1-1', 472, 55)
        self.label_list = [self.time_label, self.world_label, self.mario_label, self.level_label] #

    def create_coin_counter(self):
        self.coin_count_image = []
        self.create_label(self.coin_count_image, '*00', 300, 55)

    def create_flushing_coin(self):
        self.flush_coin = flashing_coin.Coin(280, 53)

    def create_menu_labels(self):
        '''create labels for menu'''
        one_player = []
        two_player = []
        top = []
        top_score = []
        self.create_label(one_player, '1 PLAYER GAME', 272, 360)
        self.create_label(two_player, '2 PLAYER GAME', 272, 405)
        self.create_label(top, 'TOP-', 298, 465)
        self.create_label(top_score, '000000', 390, 465)
        self.menu_labels = [one_player, two_player, top, top_score]

    def create_load_screen_labels(self):
        world_label = []
        level_label = []
        self.create_label(world_label, 'WORLD', 280, 200)
        self.create_label(level_label, '1-1', 430, 200)
        self.center_labels = [world_label, level_label]

    def create_mario_image(self):
        self.lives_label_image = self.image_dict['*']
        self.lives_label_rect = self.lives_label_image.get_rect(center=(378,295))
        self.lives_num_label = []
        self.create_label(self.lives_num_label, str(self.lives), 450, 285)
        self.image_sheet = resource.GFX['mario_bros']
        self.mario_image = self.get_image(178, 32, 12, 16)
        self.mario_rect = self.mario_image.get_rect(center=(320,290))

    def create_count_clock(self):
        self.clock_count_image = []
        self.create_label(self.clock_count_image, str(self.time), 645, 55)


    def create_label(self, label_list, string, x, y):
        for letter in string:
            label_list.append(Character(self.image_dict[letter]))
        for i, char in enumerate(label_list):
            char.rect.x = x + (char.rect.width + 3) * i
            char.rect.y = y

    def get_image(self, x, y, width, height):
        image = pg.Surface([width, height])
        image.blit(self.image_sheet, (0, 0), (x, y, width, height)) #draw img onto image
        image.set_colorkey((92,148,252)) #remove the blue
        image = pg.transform.scale(image, (int(width * 2.9), int(height * 2.9)))
        return image

    def update(self, game_info, mario=None):
        '''update all info'''
        self.mario = mario
        self.handle_game_info(game_info)

    def handle_game_info(self, game_info):
        if self.state == c.MAIN_MENU:
            self.score = game_info[c.SCORE]
            self.update_coin_total(game_info)
            self.update_score_images(self.score_image, self.score)
            self.update_score_images(self.menu_labels[3], self.top_score)
            self.flush_coin.update(game_info[c.CURRENT_TIME])
        if self.state == c.LOAD_SCREEN:
            self.score = game_info[c.SCORE]
            self.update_coin_total(game_info)
            self.update_score_images(self.score_image, self.score)
            self.flush_coin.update(game_info[c.CURRENT_TIME])
        if self.state == c.LEVEL1:
            self.score = game_info[c.SCORE]
            self.update_coin_total(game_info)
            self.update_score_images(self.score_image, self.score)
            self.flush_coin.update(game_info[c.CURRENT_TIME])
            self.clock_count_update(game_info)

    def update_coin_total(self, game_info):
        self.coin_total = game_info[c.COIN_TOTAL]
        coin_str = str(self.coin_total)
        if len(coin_str) == 1:
            coin_str = '*0' + coin_str
        elif len(coin_str) == 2:
            coin_str = '*' + coin_str
        else:
            coin_str = '*00'
        self.coin_count_image = []
        self.create_label(self.coin_count_image, coin_str, 300, 55)

    def clock_count_update(self, game_info):
        if game_info[c.LEVEL_STATE] != c.FROZEN and not self.mario.dead: #TODO: other state to count clock
            if self.mario.in_castle:
                self.time -= 1
            elif game_info[c.CURRENT_TIME] - self.current_time > 400:
                self.time -= 1
                self.current_time = game_info[c.CURRENT_TIME]
            self.clock_count_image = []
            time_str = str(self.time)
            if len(time_str) < 3:
                time_str = '0' * (3 - len(time_str)) + time_str
            self.create_label(self.clock_count_image, time_str, 645, 55)

    def update_score_images(self, images, score):
        index = len(images) - 1
        for digit in reversed(str(score)):
            rect = images[index].rect
            images[index] = Character(self.image_dict[digit])
            images[index].rect = rect
            index -= 1

    def draw(self, screen):
        if self.state == c.MAIN_MENU:
            self.draw_menu_info(screen)
        elif self.state == c.LOAD_SCREEN:
            self.draw_load_screen_info(screen)
        elif self.state == c.LEVEL1:
            self.draw_level1(screen)

    def draw_menu_info(self, screen):
        for each in self.score_image:
            screen.blit(each.image, each.rect)
        for label in self.menu_labels:
            for each in label:
                screen.blit(each.image, each.rect)
        for each in self.coin_count_image:
            screen.blit(each.image, each.rect)
        for label in self.label_list:
            for each in label:
                screen.blit(each.image, each.rect)
        screen.blit(self.flush_coin.image, self.flush_coin.rect)

    def draw_load_screen_info(self, screen):
        for each in self.score_image:
            screen.blit(each.image, each.rect)
        for label in self.label_list:
            for each in label:
                screen.blit(each.image, each.rect)
        for label in self.center_labels:
            for each in label:
                screen.blit(each.image, each.rect)
        for each in self.coin_count_image:
            screen.blit(each.image, each.rect)
        for each in self.lives_num_label:
            screen.blit(each.image, each.rect)
        screen.blit(self.lives_label_image, self.lives_label_rect)
        screen.blit(self.mario_image, self.mario_rect)
        screen.blit(self.flush_coin.image, self.flush_coin.rect)

    def draw_level1(self, screen):
        for each in self.score_image:
            screen.blit(each.image, each.rect)
        for label in self.label_list:
            for each in label:
                screen.blit(each.image, each.rect)
        for each in self.coin_count_image:
            screen.blit(each.image, each.rect)
        for each in self.clock_count_image:
            screen.blit(each.image, each.rect)
        screen.blit(self.flush_coin.image, self.flush_coin.rect)