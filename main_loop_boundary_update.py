# Main_loop_boundary_update function.

def main_loop_boundary_update(self):
    # Control the boundary on the main_loop screen.
    if self.boundary_color_loop == 0:
        self.boundary_color -= 5
    elif self.boundary_color_loop == 1:
        self.boundary_color += 5
    if self.boundary_color == 0:
        self.boundary_color_loop = 1
    elif self.boundary_color == 255:
        self.boundary_color_loop = 0
    if self.boundary_size == 1:
        self.boundary_size_loop = 0
    elif self.boundary_size == 10:
        self.boundary_size_loop = 1
    if self.boundary_size_loop_loop == 5:
        self.boundary_size_loop_loop = 0
        if self.boundary_size_loop == 0:
            self.boundary_size += 1
        elif self.boundary_size_loop == 1:
            self.boundary_size -= 1
