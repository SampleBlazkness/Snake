# Basic of game.

# Code by SampleBlazkness@outlook.com. Send emails to learn more.
# This is the first project I did in my whole life. A Little game, includes thousands of days' hard word.

# '#' means explanatory notes, '''...''' means now-useless code.

# Modules: pygame, time, random, logging, os, json(not used yet), sys.exit.
import logging, os

import pygame
from pygame.locals import *

# Import all the resource that the program needs.
from main_loop import main_loop
from main_loop_boundary_update import main_loop_boundary_update
from main_loop_check_keys import main_loop_check_keys
from main_loop_strawberry import main_loop_strawberry
from main_loop_tnt import main_loop_tnt
from show_end import show_end
from show_end_check_keys import show_end_check_keys
from snake import Snake
from snake_start import snake_start
from snake_start_check_keys import snake_start_check_keys
from strawberry import Strawberry
from tnt import Tnt

# Set log output.
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
'''logging.disable(logging.ERROR)'''
logging.info('Start of program.')

# Check if there's the path in your drive.
if not os.path.exists('C:/snake_file'):
    os.makedirs('C:/snake_file')


class Game:
    # Init.
    def __init__(self):
        logging.info('Loading game...')
        # Init pygame module.
        pygame.init()
        pygame.mixer.init()
        pygame.font.init()

        # Set screen.
        logging.info('Creating screen...(size:900 * 600)')
        self.screen = pygame.display.set_mode((900, 600))
        pygame.display.set_caption('Snake')
        pygame.display.set_icon(pygame.image.load('image/strawberry_skin/strawberry.png'))

        # Preparing for reading game data.
        self.game_data = []
        self.data_path = 'C:/snake_file/snake.dat'

        try:
            # Read saved game data.
            with open(self.data_path) as f:
                self.game_data = [data.strip() for data in f.readlines()]
                self.snake_line = eval(self.game_data[0])
                self.tnt_line = eval(self.game_data[1])
                self.strawberry_line = eval(self.game_data[2])
                self.level = eval(self.game_data[3])
                self.score = eval(self.game_data[4])
                logging.info(f'Game data:{self.game_data}')
        except:
            self.snake_line = self.tnt_line = self.strawberry_line = self.level = self.score = None
            # No data had been found in your computer.
            logging.info('No snake data had been found in your computer.')

        # Preparing for start screen.
        self.font = pygame.font.Font('font/SimSun.ttf', 16)
        # Load bg for start screen.
        self.start_background = pygame.image.load('image/snake_start/snake_start.png')
        self.continued = False

        # Preparing for main_loop screen.
        self.snake = self.Snake(self.screen, self.snake_line)
        '''self.computer_snake = self.Computer_snake(self.screen, self.snake_line)'''
        self.clock = pygame.time.Clock()  # Control FPS.
        if self.level is None:
            self.level = 400
        if self.score is None:
            self.score = 0
        self.last_collide = None
        self.SNAKEEVENT = USEREVENT + 1
        pygame.time.set_timer(self.SNAKEEVENT, self.level)
        self.KEY = None
        self.ate = []
        self.game_run = True

        # Control the boundary in the main_loop screen.
        self.boundary_size_loop_loop = 0
        self.boundary_color_loop = 0
        self.boundary_color = 255
        self.boundary_size_loop = 0
        self.boundary_size = 1

        # Load the images for main_loop screen.
        self.main_loop_background = pygame.image.load('image/snake_main_loop/snake_background.png')
        self.sound_eat = pygame.mixer.Sound('music/snake_main_loop/snake_main_loop_eat.wav')
        self.sound_hit = pygame.mixer.Sound('music/snake_main_loop/snake_main_loop_hit.wav')
        self.sound_bomp = pygame.mixer.Sound('music/snake_main_loop/snake_main_loop_bomp.wav')
        self.game_pause = self.font.render('游戏暂停', True, Color(255, 255, 255))

        # Game data for ui 'snake_end'.
        self.origin_end_image = pygame.image.load('image/snake_end/snake_end.png')

        # Main game part.
        self.snake_start()  # Show start screen.
        self.show_end(self.main_loop())  # Show main_loop screen and end_screen when the snake dies.

    def main_loop(self):
        return main_loop(self)

    def main_loop_boundary_update(self):
        main_loop_boundary_update(self)

    def main_loop_check_keys(self):
        main_loop_check_keys(self)

    def main_loop_strawberry(self, number=1, index=0, operator='default'):
        main_loop_strawberry(self, number, index, operator)

    def main_loop_tnt(self, number=1, index=0, operator='default'):
        main_loop_tnt(self, number, index, operator)

    def show_end(self, score):
        show_end(self, score)

    def show_end_check_keys(self):
        show_end_check_keys(self)

    def snake_start(self):
        snake_start(self)

    def snake_start_check_keys(self):
        snake_start_check_keys(self)

    class Snake(Snake):
        pass

    class Tnt(Tnt):
        pass

    class Strawberry(Strawberry):
        pass
