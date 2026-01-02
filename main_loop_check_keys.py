# Main_loop_check_keys function.

import logging

import pygame
from pygame.locals import *


def main_loop_check_keys(self):
    # Check events when is showing the main_loop screen.
    for i in pygame.event.get():
        if i.type == QUIT:
            pygame.mixer.music.stop()
            logging.info('End of program -- user typed quit.')
            with open(self.data_path, 'w') as f:
                f.write(str(self.snake.snake_line))
                f.write('\n' + str(self.Tnt.tnt_line[1]))
                f.write('\n' + str(self.Strawberry.strawberry_line[1]))
                f.write('\n' + str(self.level))
                f.write('\n' + str(self.score))
                logging.info('Saving game data correctly.')
            exit()
        elif i.type == KEYUP:
            if i.key == K_ESCAPE:
                pygame.mixer.music.stop()
                logging.info('End of program -- user keyed esc.')
                with open(self.data_path, 'w') as f:
                    f.write(str(self.snake.snake_line))
                    f.write('\n' + str(self.Tnt.tnt_line[1]))
                    f.write('\n' + str(self.Strawberry.strawberry_line[1]))
                    f.write('\n' + str(self.level))
                    f.write('\n' + str(self.score))
                    logging.info('Saving game data correctly.')
                exit()
            elif i.key == K_SPACE:
                if self.game_run:
                    self.game_run = False
                else:
                    self.game_run = True
            self.KEY = i.key
        if i.type == self.SNAKEEVENT:
            if self.game_run:
                self.snake.move(self.KEY)
                '''self.computer_snake.computer_move(self.snake.snake_line, self.Strawberry.strawberry_line,
                                                   self.Tnt.tnt_line)
                '''
