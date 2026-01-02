# Show_end function.

import logging, os

import pygame
from pygame.locals import *


def show_end(self, score):
    logging.info('Snake died.')
    pygame.mixer.music.load('music/snake_end/snake_end.mp3')
    pygame.mixer.music.play(-1)

    # CLear old snake data.
    logging.info('Clearing game data...')
    try:
        os.remove('C:/snake_file/snake.dat')
        logging.info('Clearing game data correctly.')
    except:
        logging.info('Failed to clear game data. Are there some strange reasons?')

    # Get a copy of the background when the snake die. Blit it on the screen after every time update the screen.
    old_screen = self.screen.copy()
    clock = pygame.time.Clock()
    # Scale the show_end picture.
    ratios = self.origin_end_image.get_rect().width / self.origin_end_image.get_rect().height
    new_width = 200
    old_ticks = pygame.time.get_ticks()
    while True:
        clock.tick(100)
        self.show_end_check_keys()
        # Showing end.
        ticks = pygame.time.get_ticks() - old_ticks
        if new_width <= 700:
            new_width += int(ticks / 1000 * 5)
        end_image = pygame.transform.smoothscale(self.origin_end_image, (new_width, int(new_width / ratios)))
        x, y = int((900 - end_image.get_rect().width) / 2), int((400 - end_image.get_rect().height) / 2)
        self.screen.blit(old_screen, (0, 0))
        self.screen.blit(end_image, (x, y))
        if new_width > 700:
            pygame.draw.rect(self.screen, Color(150, 205, 50), Rect(270, 380, 370, 100))
            self.screen.blit(self.font.render("得分：", True, Color(255, 0, 0)), (390, 420))
            self.screen.blit(self.font.render(str(score), True, Color(0, 0, 255)), (460, 420))
        pygame.display.flip()
