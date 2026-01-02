# Snake_start_check_keys function.

import logging

import pygame
from pygame.locals import *


def snake_start_check_keys(self):
    # Press any keys to continue...
    for i in pygame.event.get():
        if i.type == QUIT:
            pygame.mixer.music.stop()
            logging.info('End of program -- user typed quit.')
            exit()
        if i.type == KEYUP:
            # User press something.
            pygame.mixer.music.stop()
            # If the key user press is Escape Button, exit.
            if i.key == K_ESCAPE:
                logging.info('End of program -- user keyed esc.')
                exit()
            # Else, the game will go on.
            self.continued = True
