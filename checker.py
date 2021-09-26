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

    def is_game_over(self, counter, tracker):
        """
        Checks if the game is over by checking to see if there are
        4 pieces in a row or if all 42 pieces are taken

        :param counter: Counter variable carried throughout game
        :param tracker: Nested list containing board logic
        :return: False if game is over, True if its not
        """
        end_counter = counter
        tracker = tracker
        horizontal = False
        vertical = False
        diagonal = False
        horizontal = Checker.check_horizontal(self, tracker)
        if horizontal or vertical or diagonal:
            return True
        if end_counter == 42:
            return False
        else:
            return True

    def check_horizontal(self, board):
        width = 7
        height = 6
        win_counter = 0
        # The first bracket for the board is the height
        # The second bracket is the width
        for i in range(height):
            for j in range(width):
                try:
                    # This is not working correctly
                    # For some reason it is only starting to check after 12 or
                    # so turns.
                    if board[i][j] == board[i][j+1] and board[i][j] != 0:
                        win_counter += 1
                        print(board)
                        print(f"board position {board[i][j]}")
                        print(win_counter)
                        if win_counter == 4:
                            return True
                        else:
                            return False
                except IndexError:
                    return False

