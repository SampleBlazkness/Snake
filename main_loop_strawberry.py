# Main_loop_strawberry function.

import pygame


def main_loop_strawberry(self, number=1, index=0, operator='default'):
    if operator == 'default':
        # Spawn strawberry in normal mode.
        for i in range(number):
            self.Strawberry.strawberry_line[0].append(self.Strawberry(self.snake.snake_line))
    elif operator == 'change':
        # Change strawberry's location.
        self.Strawberry.strawberry_line[0][index].kill()
        self.Strawberry.strawberry_line[0][index] = self.Strawberry(self.snake.snake_line, index)
    elif operator == 'add':
        # Spawn new strawberry.
        self.Strawberry.strawberry_line[0].append(self.Strawberry(self.snake.snake_line))
    elif operator == 'rebuild':
        # Use the last data.
        for i in self.strawberry_line:
            self.Strawberry.strawberry_line[0].append(self.Strawberry(xy=i))
    elif operator == 'check_hit':
        # Check if the snake hit the strawberry, means the snake eat one of the strawberries.
        rasp = pygame.sprite.spritecollideany(self.snake, self.Strawberry.group)
        if rasp:
            if rasp != self.last_collide:
                self.score += 10
                self.ate.append(rasp)
                self.snake.lengthening += 1
                self.level -= 10
                self.sound_eat.play()
                pygame.time.set_timer(self.SNAKEEVENT, self.level)
            else:
                rasp.image = pygame.transform.smoothscale(
                    rasp.image,
                    (int(rasp.rect.width - 1), int(rasp.rect.height - 1))
                )
                rasp.rect.inflate_ip(-2, -2)
            self.last_collide = rasp
        if self.last_collide and rasp != self.last_collide and \
                self.last_collide in self.Strawberry.group.sprites():
            for one_ate in self.ate:
                self.main_loop_strawberry(index=self.Strawberry.strawberry_line[1].index(one_ate.xy),
                                          operator='change')
            self.ate = []
