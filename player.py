import pygame
pygame.init()


class Player(pygame.sprite.Sprite):
    """
    Class for the player logic
    """
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        pass

    def pick_location(self, board, player_piece, player1, player2, player_choice):
        """
        Determines if the place the player is selecting is a selectable
        location
        :param board:
        :param player_piece:
        :param player1:
        :param player2:
        :return: the board with the players new location
        """

    def switch_players(self, turn_tracker):
        """
        Determines which players turn it is
        :param turn_tracker: int
        :return: True, False if its player 1's turn, False, True if player 2's
        """
        self.turn_tracker = turn_tracker
        if self.turn_tracker % 2 == 0:
            return True, False
        else:
            return False, True
