import pygame
import mouse
pygame.init()


class Player(pygame.sprite.Sprite):
    """
    Class for the player logic
    """
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.player_win_counter = 0
        self.player_flag = None
        self.mouse = mouse.Mouse()

    def switch_players(self, turn_tracker):
        """
        Determines which players turn it is
        :param turn_tracker: int
        :return: True, False if its player 1's turn, False, True if player 2's
        """
        self.turn_tracker = turn_tracker
        if self.turn_tracker % 2 == 0:
            return True
        else:
            return False

    def get_position(self):
        x_loc = self.mouse.get_mouse_location()
        return x_loc

