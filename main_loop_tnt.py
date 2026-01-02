# Main_loop_tnt function.

def main_loop_tnt(self, number=1, index=0, operator='default'):
    if operator == 'default':
        # Spawn tnt in normal mode.
        for i in range(number):
            self.Tnt.tnt_line[0].append(self.Tnt(self.snake.snake_line))
    elif operator == 'change':
        # Change the location of tnt.
        self.Tnt.tnt_line[0][index].kill()  # Kill the sprite.
        self.Tnt.tnt_line[0][index] = self.Tnt(self.snake.snake_line, index)  # Add a new sprite.
    elif operator == 'add':
        # Spawn new tnt.
        self.Tnt.tnt_line[0].append(self.Tnt(self.snake.snake_line))
    elif operator == 'rebuild':
        # Use the old data.
        for i in self.tnt_line:
            self.Tnt.tnt_line[0].append(self.Tnt(xy=i))
