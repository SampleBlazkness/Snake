# Snake class.

import pygame
from pygame.locals import *


class Snake(pygame.sprite.Sprite):
    # Snake itself.
    # The options of the class 'snake' is a bit hard to understand. So here are not any explanatory notes.
    snake_head = pygame.image.load('image/snake_skin/snake_head.png')
    snake_body = pygame.image.load('image/snake_skin/snake_body.png')
    snake_tail = pygame.image.load('image/snake_skin/snake_tail.png')
    snake_turn = pygame.image.load('image/snake_skin/snake_turn.png')

    def __init__(self, screen, snake_line):
        # Set default snake.
        pygame.sprite.Sprite.__init__(self)
        self.snake_line = snake_line
        if self.snake_line is None:
            self.snake_line = [(60, 0), (30, 0), (0, 0)]
        self.screen = screen
        self.rect = Rect(self.snake_line[0][0], self.snake_line[0][1], 30, 30)
        self.lengthening = 0
        self.live = True

    def show(self, new_snake_line=None):
        # Show snake on the screen.
        if new_snake_line is not None:
            self.snake_line = new_snake_line
        self.rect = Rect(self.snake_line[0], (30, 30))
        for inx, cord in enumerate(self.snake_line):
            self.screen.blit(self.get_body_image(inx), cord)

    def get_body_image(self, index):
        # Get the faces of each snake's head, body and tail.
        if index == 0 or index == len(self.snake_line) - 1:
            before = self.snake_line[0] if index == 0 else self.snake_line[-2]
            after = self.snake_line[1] if index == 0 else self.snake_line[-1]
            X = before[0] - after[0]
            Y = before[1] - after[1]
            if X == 30 and Y == 0:
                return self.snake_head if index == 0 else self.snake_tail
            elif X == -30 and Y == 0:
                return pygame.transform.rotate(self.snake_head if index == 0 else self.snake_tail, 180)
            elif X == 0 and Y == 30:
                return pygame.transform.rotate(self.snake_head if index == 0 else self.snake_tail, -90)
            elif X == 0 and Y == -30:
                return pygame.transform.rotate(self.snake_head if index == 0 else self.snake_tail, 90)
        elif self.snake_line[index - 1][0] == self.snake_line[index + 1][0]:
            return pygame.transform.rotate(self.snake_body, 90)
        elif self.snake_line[index - 1][1] == self.snake_line[index + 1][1]:
            return self.snake_body
        else:
            slope = (self.snake_line[index - 1][0] - self.snake_line[index + 1][0]) / (
                    self.snake_line[index - 1][1] - self.snake_line[index + 1][1])
            right = (max(self.snake_line[index - 1][0], self.snake_line[index + 1][0]) >
                     self.snake_line[index][0])
            if slope > 0 and right:
                return pygame.transform.rotate(self.snake_turn, 180)
            elif slope > 0 and not right:
                return self.snake_turn
            elif slope < 0 and right:
                return pygame.transform.rotate(self.snake_turn, 90)
            elif slope < 0 and not right:
                return pygame.transform.rotate(self.snake_turn, -90)

    def get_direction(self):
        # Get the snake's direction.
        x = self.snake_line[0][0] - self.snake_line[1][0]
        y = self.snake_line[0][1] - self.snake_line[1][1]
        if x == 30 and y == 0:
            return K_RIGHT
        elif x == -30 and y == 0:
            return K_LEFT
        elif x == 0 and y == 30:
            return K_DOWN
        elif x == 0 and y == -30:
            return K_UP

    def move(self, KEY=None):
        # Control the snake's moving.
        if len(set(self.snake_line)) < len(self.snake_line):
            # When the snake eat its body.
            self.live = False
            return
        for place in self.snake_line:
            if place[0] == -30 or place[0] == 900 or place[1] == -30 or place[1] == 600:
                self.live = False
                return
        wrong_press_list = [
            {K_RIGHT, K_RIGHT},
            {K_RIGHT, K_LEFT},
            {K_LEFT, K_LEFT},
            {K_UP, K_UP},
            {K_UP, K_DOWN},
            {K_DOWN, K_DOWN}
        ]
        right_press_list = [K_RIGHT, K_LEFT, K_UP, K_DOWN]
        if self.lengthening > 0:
            self.enlarge()
            self.lengthening -= 1
        if KEY is None or {self.get_direction(), KEY} in wrong_press_list or KEY not in right_press_list:
            # When get invalid key input, use snake's now direction.
            KEY = self.get_direction()
        if KEY == K_RIGHT:
            self.snake_line = [((self.snake_line[0][0] + 30), self.snake_line[0][1])] + self.snake_line[0:-1]
        elif KEY == K_UP:
            self.snake_line = [(self.snake_line[0][0], (self.snake_line[0][1] - 30))] + self.snake_line[0:-1]
        elif KEY == K_DOWN:
            self.snake_line = [(self.snake_line[0][0], (self.snake_line[0][1] + 30))] + self.snake_line[0:-1]
        elif KEY == K_LEFT:
            self.snake_line = [((self.snake_line[0][0] - 30), self.snake_line[0][1])] + self.snake_line[0:-1]

    def enlarge(self):
        # Enlarge the snake after eating strawberry.
        direction = self.snake_line[-1][0] - self.snake_line[-2][0]
        if direction == 0:
            insert = self.snake_line[-1]
            self.snake_line.insert(-1, insert)
        elif direction == -30:
            insert = self.snake_line[-1]
            self.snake_line.insert(-1, insert)
        elif direction == 30:
            insert = self.snake_line[-1]
            self.snake_line.insert(-1, insert)
        else:
            insert = self.snake_line[-1]
            self.snake_line.insert(-1, insert)
