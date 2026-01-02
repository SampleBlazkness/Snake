# Main_loop function.

import logging, random

import pygame
from pygame.locals import *


def main_loop(self):
    # Game's main part.
    # Play the music.
    pygame.mixer.music.load('music/snake_main_loop/snake_main_loop.mp3')
    pygame.mixer.music.play(-1)
    # Add tnt.
    if self.tnt_line:
        self.main_loop_tnt(operator='rebuild')
    else:
        self.main_loop_tnt(1)
    # Add strawberry.
    if self.strawberry_line:
        self.main_loop_strawberry(operator='rebuild')
    else:
        self.main_loop_strawberry(10)
    # Main game.
    while True:
        self.clock.tick(60)
        # Update the screen.
        self.screen.blit(self.main_loop_background, (0, 0))
        self.Strawberry.group.draw(self.screen)
        self.Tnt.group.draw(self.screen)
        self.main_loop_boundary_update()
        self.screen.fill((35, 135, 200), (self.snake.snake_line[0][0], self.snake.snake_line[0][1], 30, 30))
        self.snake.show()
        '''
        if self.computer_snake.live:
            self.computer_snake.show()
        '''
        # Draw the boundary.
        pygame.draw.rect(
            self.screen,
            Color(self.boundary_color, 0, 0),
            Rect(0, 0, 900, 600),
            self.boundary_size
        )
        # Check the events and update snake's locations.
        self.main_loop_check_keys()
        if self.game_run:
            # Change the locations of tnt.
            i = random.randint(0, 2000)
            if not i % 1000:
                # Tnt is getting more.
                logging.info('Tnt is now getting more!')
                self.main_loop_tnt(len(self.Tnt.tnt_line[0]) + 1, operator='add')
            elif not i % 100:
                # Tnt's location is changing.
                logging.info('One tnt is now changing its xy!')
                index = random.randint(0, len(self.Tnt.tnt_line[0]) - 1)
                self.main_loop_tnt(index=index, operator='change')
        # Check if the snake eat the strawberry(hit).
        self.main_loop_strawberry(1, operator='check_hit')
        # Check if the computer eat the strawberry.
        '''
        rasp = pygame.sprite.spritecollideany(self.computer_snake, self.Strawberry.group)
        if rasp:
            if rasp != self.last_collide:
                self.score -= 10
                self.ate.append(rasp)
                self.computer_snake.lengthening += 1
                self.level -= 10
                self.sound_eat.play()
                pygame.time.set_timer(self.SNAKEEVENT, self.level)
            else:
                rasp.image = pygame.transform.smoothscale(
                    rasp.image,
                    (int(rasp.rect.width - 0.01), int(rasp.rect.height - 0.01))
                )
                rasp.rect.inflate_ip(-2, -2)
            self.last_collide = rasp
        if self.last_collide and rasp != self.last_collide and \
                self.last_collide in self.Strawberry.group.sprites():
            for one_ate in self.ate:
                one_ate.kill()
            self.ate = []
            self.Strawberry()
        '''
        # Check if the snake hit the tnt, then game over.
        rasp = pygame.sprite.spritecollideany(self.snake, self.Tnt.group)
        if rasp:
            self.snake.live = False
            self.sound_bomp.play()
            break
        # Or the snake hit the boundary, then snake die, either.
        if not self.snake.live:
            self.sound_hit.play()
            break
        # If game is paused, blit the sign on the screen.
        if not self.game_run:
            self.screen.blit(self.game_pause, (450 - self.game_pause.get_rect().width / 2, 10))
        # Update the screen.
        pygame.display.flip()
        # Update the boundary size.
        self.boundary_size_loop_loop += 1
        # Show logs.
        pygame.display.flip()
        logging.info('-----Snake_line-----')
        logging.info(self.snake.snake_line)
        logging.info('-----Tnt_line-----')
        logging.info(self.Tnt.tnt_line[0])
        logging.info(self.Tnt.tnt_line[1])
        logging.info('-----Strawberry_line-----')
        logging.info(self.Strawberry.strawberry_line)
        logging.info('-----Score-----')
        logging.info(self.score)
        print()
    return self.score
