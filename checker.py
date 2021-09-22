import pygame


class Checker:
    """
    This is a basic class that contains functions to check spaces above,
    below, and diagonal to the last piece placed.
    """
    def __init__(self, board, player, player_piece):
        self.columns = 7
        self.rows = 6
        self.win_counter = 0
        self.board = board
        self.player = player
        self.player_piece = player_piece
        self.bottom_piece = False
        self.bottom_of_board_x = 0
        self.top_of_board_y = 7

    def is_game_over(self, counter, player_piece):
        """
        Checks if the game is over by checking to see if there are
        4 pieces in a row or if all 42 pieces are taken

        :param counter: Counter variable carried throughout game
        :param player_piece: Dictionary containing player symbols
        :return: False if game is over, True if its not
        """
        win_counter = 0
        if counter == 42:
            return False


