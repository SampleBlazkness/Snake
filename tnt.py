import random

import pygame
from pygame.locals import *


class Tnt(pygame.sprite.Sprite):
    # An NPC: user's enemy.
    # Meaning: Make the game full of challenges and excitements.

    tnt_line = [[], []]  # Tnt's locations.
    group = pygame.sprite.Group()
    screen_black_grid = [(x * 30, y * 30) for x in range(0, 30) for y in range(0, 20)]

    def __init__(self, snake_line=[], index=None, xy=None):
        pygame.sprite.Sprite.__init__(self)
        # Get xy which is valid.
        # Only xy is not on the snake's body, the tnt will spawn.
        self.black_grid = list(filter(lambda x: x not in snake_line, self.screen_black_grid))
        if xy is None:  # Means a new game.
            while True:
                # Choose for a place to spawn the tnt. But sometimes it will be summoned on the strawberry.
                self.xy = random.choice(self.black_grid)
                x = snake_line[0][0] - snake_line[1][0]
                y = snake_line[0][1] - snake_line[1][1]
                if x == 30 and y == 0:
                    if self.xy[1] == snake_line[0][1]:
                        if 90 >= self.xy[0] - snake_line[0][0] >= 0:
                            continue
                elif x == -30 and y == 0:
                    if self.xy[1] == snake_line[0][1]:
                        if 90 >= snake_line[0][0] - self.xy[0] >= 0:
                            continue
                elif x == 0 and y == 30:
                    if self.xy[0] == snake_line[0][0]:
                        if 90 >= snake_line[0][1] - self.xy[1] >= 0:
                            continue
                elif x == 0 and y == -30:
                    if self.xy[0] == snake_line[0][0]:
                        if 90 >= self.xy[1] - snake_line[0][1] >= 0:
                            continue
                self.rect = Rect(self.xy[0], self.xy[1], 30, 30)
                if index is not None:  # Index is valid:
                    # Means the tnt is now changing its location.
                    self.tnt_line[1][index] = self.xy
                else:
                    # Means the tnt is now getting more.
                    self.tnt_line[1].append(self.xy)
                # Location found successfully.
                break
        else:  # Means an old game.
            self.rect = Rect(xy[0], xy[1], 30, 30)
            self.tnt_line[1].append((xy[0], xy[1]))
        # Set image.
        self.image = pygame.image.load('image/tnt_skin/tnt.png')
        # Add to the tnt group.
        self.group.add(self)
