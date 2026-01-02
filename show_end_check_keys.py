# Show_end_check_keys function.

import logging

import pygame
from pygame.locals import *


def show_end_check_keys(self):
    # Check events when is showing the end_screen.
    for i in pygame.event.get():
        if i.type == QUIT:
            pygame.mixer.music.stop()
            logging.info('End of program -- user typed quit.')
            exit()
        if i.type == KEYUP and i.key == K_ESCAPE:
            pygame.mixer.music.stop()
            logging.info('End of program -- user keyed esc.')
            exit()
