import random

import pygame
from pygame.locals import *


class Strawberry(pygame.sprite.Sprite):
    # An NPC: snake's food.
    # Meaning: set the goal of the game: eat the strawberries to get longer, forever.
    group = pygame.sprite.Group()
    # the locations of the strawberry.
    screen_blank_grid = [(x * 30, y * 30) for x in range(0, 30) for y in range(0, 20)]
    strawberry_line = [[], []]

    def __init__(self, snake_line=[], index=None, xy=None):
        pygame.sprite.Sprite.__init__(self)
        if xy is None:
            # If the xy is None, means the game is spawning strawberries in normal mode.
            # Filter the invalid locations: on the snake's body or other strawberries.
            blank_grid = list(filter(lambda x: x not in snake_line, self.screen_blank_grid))
            blank_grid = list(filter(lambda x: x not in self.strawberry_line[1], blank_grid))
            self.xy = random.choice(blank_grid)
            self.rect = Rect(self.xy[0], self.xy[1], 30, 30)
            if index is not None:
                # Changing the location.
                self.strawberry_line[1][index] = self.xy
            else:
                # Spawn new strawberry.
                self.strawberry_line[1].append(self.xy)
        else:  # Use old game data.
            self.rect = Rect(xy[0], xy[1], 30, 30)
            self.xy = (xy[0], xy[1])
            self.strawberry_line[1].append(self.xy)
        self.image = pygame.image.load('image/strawberry_skin/strawberry.png')
        self.group.add(self)
