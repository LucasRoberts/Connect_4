import pygame


class Mouse:
    """
    Class for tracking mouse events and movements
    """
    def __init__(self):
        self.mouse = pygame.mouse
        # This is because I will not be changing the screen resolution
        self.x1 = 95
        self.x2 = 185
        self.x3 = 275
        self.x4 = 365
        self.x5 = 455
        self.x6 = 545
        self.x7 = 640
        self.y1 = 85

    def get_mouse_location(self):
        if self.mouse.get_pos()[0] <= self.x1 and self.mouse.get_pos()[1] <= self.y1:
            return 0
        elif self.x1 <= self.mouse.get_pos()[0] <= self.x2 and self.mouse.get_pos()[1] <= self.y1:
            return 1
        elif self.x2 <= self.mouse.get_pos()[0] <= self.x3 and self.mouse.get_pos()[1] <= self.y1:
            return 2
        elif self.x3 <= self.mouse.get_pos()[0] <= self.x4 and self.mouse.get_pos()[1] <= self.y1:
            return 3
        elif self.x4 <= self.mouse.get_pos()[0] <= self.x5 and self.mouse.get_pos()[1] <= self.y1:
            return 4
        elif self.x5 <= self.mouse.get_pos()[0] <= self.x6 and self.mouse.get_pos()[1] <= self.y1:
            return 5
        elif self.x6 <= self.mouse.get_pos()[0] <= self.x7 and self.mouse.get_pos()[1] <= self.y1:
            return 6
        else:
            return -1  # This is a sentinel
