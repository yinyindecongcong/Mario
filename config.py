SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
CAPTION = "Super Mario Level 1"

TWO_players = "two pp"

server_address = ('localhost', 8022)
player1_address = [('localhost', 3333), ('localhost', 4444)]
player2_address = [('localhost', 1111), ('localhost', 2222)]
#overhead state info
MAIN_MENU = 'main menu'
LOAD_SCREEN = 'loading screen'
LEVEL1 = 'level1'
GAME_OVER = 'game over'
FAST_COUNT_DOWN = 'fast count down'
END_OF_LEVEL = 'end of level'

#player info
COIN_TOTAL = 'coin total'
SCORE = 'score'
TOP_SCORE = 'top score'
LIVES = 'lives'
CURRENT_TIME = 'current time'
LEVEL_STATE = 'level state'
CAMERA_START_X = 'camera start x'
MARIO_DEAD = 'mario dead'


## Color
PURPLE       = (255,   0, 220)
BLACK        = (  0,   0,   0)

#offset
SIZE_MULTIPLIER = 2.5
BRICK_SIZE_MULTIPLIER = 2.69
BACKGROUND_MULTIPLER = 2.679
GROUND_HEIGHT = SCREEN_HEIGHT - 62

#menu cursor state
PLAYER1 = '1 player'
PLAYER2 = '2 player'

#stage for game control
MAIN_MENU = 'main menu'
LOAD_SCREEN = 'load screen'
GAME_OVER = 'game over'
LEVEL1 = 'level1'

#Mario States
STAND = 'standing'
WALK = 'walk'
JUMP = 'jump'
FALL = 'fall'
SMALL_TO_BIG = 'small to big'
BIG_TO_FIRE = 'big to fire'
BIG_TO_SMALL = 'big to small'
FLAGPOLE = 'flag pole'
WALKING_TO_CASTLE = 'walking to castle'
END_OF_LEVEL_FALL = 'end of level fall'
BOTTOM_OF_POLE = 'bottom of pole'
DEATH_JUMP = 'death jump'

#LEVEL STATES
FROZEN = 'frozen'
NOT_FROZEN = 'not frozen'
IN_CASTLE = 'in castle'
FLAG_AND_FIREWORKS = 'flag and fireworks'

#MARIO FORCES
WALK_ACCEL = 0.1
RUN_ACCEL = 20
TURNAROUND = 0.4

GRAVITY = 1.0
JUMP_AC = 0.25
JUMP_VEL = -10
MAX_Y_VEL = 11

MAX_RUN_SPEED = 8
MAX_WALK_SPEED = 6
INTERVEL = 200

#BRICK STATES
RESTING = 'resting'
BUMPED = 'bumped'

#COIN STATES
USELESS = 'run out'
SPIN = 'spin'

#Brick and coin box contents/powerup
MUSHROOM = 'mushroom'
STAR = 'star'
FIREFLOWER = 'fireflower'
SIXCOINS = '6-coins'
COIN = 'coin'
LIFE_MUSHROOM = '1up_mushroom'
FIREBALL = 'fireball'

#FLAG STATE
STILL = 'still'
MOVE = 'moving'

#powerup state
UP = 'up'
SLIDE = 'slide'
BOUNCE = 'bounce'
ONEUP = '1UP'

#Fireball state
FLYING = 'flying'
BOUNCING = 'bouncing'
EXPLODING = 'exploding'

#enemies
JUMPED_ON = 'jumped on'
DEATH_JUMP = 'death jump'

#SOUND STATEZ
NORMAL = 'normal'
STAGE_CLEAR = 'stage clear'
WORLD_CLEAR = 'world clear'
TIME_WARNING = 'time warning'
SPED_UP_NORMAL = 'sped up normal'
INVINCIBLE = 'mario invincible'