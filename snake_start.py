# Snake_start function.

import logging, time

import pygame
from pygame.locals import *


def snake_start(self):
    # Play the music.
    pygame.mixer.music.load('music/snake_start/snake_start.mp3')
    pygame.mixer.music.play(-1)
    self.screen.blit(self.start_background, (0, 0))
    logging.info('Loaded game music and background correctly.')
    # While true if user doesn't press any keys.
    while not self.continued:
        self.snake_start_check_keys()
        self.screen.fill(pygame.Color(0, 0, 0), Rect(0, 560, 900, 40))
        if not int(time.time()) % 2:
            self.screen.blit(self.font.render('按任意键继续……',
                                              True, Color(255, 255, 255)),
                             (20, 572))
        pygame.display.flip()  # Update screen.
