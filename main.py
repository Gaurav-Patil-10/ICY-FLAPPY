import pygame # importing pygame module
import random # importing random for generating random numbers
import sys    # for using sys.exit() for exiting the game when X is pressed
from pygame.locals  import * # basic pygame imports

# Global Variables for the game

FPS = 32   # frames per second for rendering
SCREEN_WIDTH = 350   
SCREEN_HEIGHT = 600  
SCREEN = pygame.display.set_mode((SCREEN_WIDTH , SCREEN_HEIGHT))
GROUNDY = SCREEN_HEIGHT
GAME_SPRITES = {}
GAME_SOUNDS = {}
PLAYER = "/ICY FLAPPY/Sprites/bird.png"
BACKGROUND = "/ICY FLAPPY/Sprites/background.png"
OBSTACLES = '/ICY FLAPPY/Sprites/obstacles.png'


# driver code from where the game will start
if __name__ == "__main__":

    pygame.init()   # initialising all pygame modules
    FPS_CLOCK = pygame.time.Clock()
    pygame.display.set_caption("ICY FLAPPY")
    GAME_SPRITES['numbers'] = (
        pygame.image.load('/ICY FLAPPY/Sprites/0.png').convert_alpha(),
        pygame.image.load('/ICY FLAPPY/Sprites/1.png').convert_alpha(),
        pygame.image.load('/ICY FLAPPY/Sprites/2.png').convert_alpha(),
        pygame.image.load('/ICY FLAPPY/Sprites/3.png').convert_alpha(),
        pygame.image.load('/ICY FLAPPY/Sprites/4.png').convert_alpha(),
        pygame.image.load('/ICY FLAPPY/Sprites/5.png').convert_alpha(),
        pygame.image.load('/ICY FLAPPY/Sprites/6.png').convert_alpha(),
        pygame.image.load('/ICY FLAPPY/Sprites/7.png').convert_alpha(),
        pygame.image.load('/ICY FLAPPY/Sprites/8.png').convert_alpha(),
        pygame.image.load('/ICY FLAPPY/Sprites/9.png').convert_alpha()

    )

    GAME_SPRITES['message'] = pygame.image.load('/ICY FLAPPY/Sprites/message.png').convert_alpha()
    GAME_SPRITES['base'] = pygame.image.load('/ICY FLAPPY/Sprites/base.png').convert_alpha()
    GAME_SPRITES['obstacles'] = (
        pygame.image.load(OBSTACLES).convert_alpha(),
        pygame.transform.rotate(pygame.image.load(OBSTACLES).convert_alpha() , 180)
    )

    # Game Sounds 

    GAME_SOUNDS['die'] = pygame.mixer.Sound('/ICY FLAPPY/audio/die.wav')
    GAME_SOUNDS['hit'] = pygame.mixer.Sound('/ICY FLAPPY/audio/hit.wav')
    GAME_SOUNDS['point'] = pygame.mixer.Sound('/ICY FLAPPY/audio/point.wav')
    GAME_SOUNDS['swoosh'] = pygame.mixer.Sound('/ICY FLAPPY/audio/swoosh.wav')
    GAME_SOUNDS['wing'] = pygame.mixer.Sound('/ICY FLAPPY/audio/wing.wav')

    # background , Player Sprites

    GAME_SPRITES['background'] = pygame.image.load(BACKGROUND).convert_aplha()
    GAME_SPRITES['player'] = pygame.image.load(PLAYER).convert_aplha()

    # game Loop

    while True:

        welcome_screen()
        main_game()






