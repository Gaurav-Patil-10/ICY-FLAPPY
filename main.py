import pygame # importing pygame module
import random # importing random for generating random numbers
import sys    # for using sys.exit() for exiting the game when X is pressed
from pygame.locals  import * # basic pygame imports

# Global Variables for the game

FPS = 32   # frames per second for rendering
SCREEN_WIDTH = 500 
SCREEN_HEIGHT = 650 
SCREEN = pygame.display.set_mode((SCREEN_WIDTH , SCREEN_HEIGHT))
GROUNDY = SCREEN_HEIGHT
GAME_SPRITES = {}
GAME_SOUNDS = {}
PLAYER = "Sprites/bird.png"
BACKGROUND = "Sprites/background.png"
OBSTACLES = 'Sprites/obstacles.png'


# Defining the Functions for the game 

def welcome_screen():
    """ 
    Shows welcome images on the screen
    """

    playerX = int(SCREEN_WIDTH / 5)
    playerY = int((SCREEN_HEIGHT - GAME_SPRITES['player'].get_height())/2)
    messageX = int((SCREEN_HEIGHT - GAME_SPRITES['message'].get_width())/2)
    messageY = int(SCREEN_HEIGHT  * 0.13)
    baseX = 0
    baseY = int((SCREEN_HEIGHT - GAME_SPRITES['player'].get_height() - 20))
    while True:

        for event in pygame.event.get():
            # if user clicks on X button game will end there
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):

                pygame.quit()
                sys.exit()

            # if user presses Space or Up key Start the game 

            elif event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                return 

            else:
                # showing the images on the screen

                SCREEN.blit(GAME_SPRITES['background'] , (0 ,0 ))
                SCREEN.blit(GAME_SPRITES['message'] , (0,0 ))
                pygame.display.update()
                FPS_CLOCK.tick(FPS)
                
def main_game () :

    """
    The main Game Function
    """
    score = 0
    playerX = int(SCREEN_WIDTH / 5)
    playerY = int(SCREEN_HEIGHT / 2)
    baseX = 0
    baseY = int((SCREEN_HEIGHT - GAME_SPRITES['player'].get_height() - 20))

    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):

                    pygame.quit()
                    sys.exit()

                # if user presses Space or Up key Start the game 

            elif event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                return 

            else:
                # showing the images on the screen
                SCREEN.blit(GAME_SPRITES['background'] , (0 ,0 ))
                SCREEN.blit(GAME_SPRITES['player'] , (playerX , playerY ))
                SCREEN.blit(GAME_SPRITES['base'] , (baseX, baseY ))
                pygame.display.update()
                FPS_CLOCK.tick(FPS)

                









# driver code from where the game will start
if __name__ == "__main__":

    pygame.init()   # initialising all pygame modules
    FPS_CLOCK = pygame.time.Clock()
    pygame.display.set_caption("ICY FLAPPY")
    GAME_SPRITES['numbers'] = (
        pygame.image.load('Sprites\\0.png').convert_alpha(),
        pygame.image.load('Sprites\\1.png').convert_alpha(),
        pygame.image.load('Sprites\\2.png').convert_alpha(),
        pygame.image.load('Sprites\\3.png').convert_alpha(),
        pygame.image.load('Sprites\\4.png').convert_alpha(),
        pygame.image.load('Sprites\\5.png').convert_alpha(),
        pygame.image.load('Sprites\\6.png').convert_alpha(),
        pygame.image.load('Sprites\\7.png').convert_alpha(),
        pygame.image.load('Sprites\\8.png').convert_alpha(),
        pygame.image.load('Sprites\\9.png').convert_alpha()

    )

    GAME_SPRITES['message'] = pygame.image.load('Sprites/message.png').convert_alpha()
    GAME_SPRITES['base'] = pygame.image.load('Sprites/base.png').convert_alpha()
    GAME_SPRITES['obstacles'] = (
        pygame.image.load(OBSTACLES).convert_alpha(),
        pygame.transform.rotate(pygame.image.load(OBSTACLES).convert_alpha() , 180)
    )

    # Game Sounds 

    GAME_SOUNDS['die'] = pygame.mixer.Sound('audio/die.wav')
    GAME_SOUNDS['hit'] = pygame.mixer.Sound('audio/hit.wav')
    GAME_SOUNDS['point'] = pygame.mixer.Sound('audio/point.wav')
    GAME_SOUNDS['swoosh'] = pygame.mixer.Sound('audio/swoosh.wav')
    GAME_SOUNDS['wing'] = pygame.mixer.Sound('audio/wing.wav')

    # background , Player Sprites

    GAME_SPRITES['background'] = pygame.image.load(BACKGROUND).convert_alpha()
    GAME_SPRITES['player'] = pygame.image.load(PLAYER).convert_alpha()

    # game Loop

    while True:

        welcome_screen()   # Shows the welcome screen until user click the play OR tap 
        main_game()        # this is the main Game Function






