import pygame


class Checker:
    """
    This is a basic class that contains functions to check spaces above,
    below, and diagonal to the last piece placed.
    """
    def __init__(self, x_loc, y_loc, board, player, player_piece):
        self.columns = 7
        self.rows = 6
        self.win_counter = 0
        self.x = x_loc
        self.y = y_loc
        self.board = board
        self.player = player
        self.player_piece = player_piece

    def check_left(self):
        """
        Checks the positions to the left of the last placed piece
        :return: add 1 to counter everytime same symbol is checked
        """
        while self.x > 0 and self.win_counter <= 3:
            if self.x-1 >= 0 and self.board[self.y][self.x-1] == self.board[self.y][self.x]:
                self.win_counter += 1

    def check_right(self):
        """
        Checks the positions to the right of the last places piece
        :return: add 1 to counter everytime same symbol is checked
        """
        while self.x > self.columns and self.win_counter <= 3:
            if self.x+1 <= self.columns and self.board[self.y][self.x-1] == self.board[self.y][self.x]:
                self.win_counter += 1
                if self.win_counter == 3:
                    break

    def is_game_over(self, counter, player_piece):
        """
        Checks if the game is over by checking to see if there are
        4 pieces in a row or if all 42 pieces are taken

        :param counter: Counter variable carried throughout game
        :param player_piece: Dictionary containing player synmbols
        :return: False if game is over, True if its not
        """
        win_counter = 0
        if counter == 42:
            return False


