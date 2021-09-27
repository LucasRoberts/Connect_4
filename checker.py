import mouse


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
        self.mouse = mouse.Mouse()

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
        # This is getting sent to the running variable in main
        # So if it's true that means it will keep running
        # False means it will exit
        horizontal = Checker.check_horizontal(self, tracker)
        vertical = Checker.check_vertical(self, tracker)
        diagonal = Checker.check_diagonal(self, tracker)
        if not horizontal or not vertical or not diagonal:
            return False
        if end_counter == 42:
            return False
        else:
            return True

    def check_horizontal(self, board):
        width = 7
        height = 6
        win_counter = 0
        horizontal_flag = True
        # The first bracket for the board is the height
        # The second bracket is the width
        for i in range(height):
            for j in range(width):
                try:
                    if board[i][j] == board[i][j+1] and board[i][j] != 0:
                        win_counter += 1
                        if win_counter == 3:
                            return False
                        else:
                            horizontal_flag = True
                except IndexError:
                    horizontal_flag = True
            win_counter = 0
        return horizontal_flag

    def check_vertical(self, board):
        height = 6
        win_counter = 0
        vertical_flag = True
        # The first bracket for the board is the height
        # The second bracket is the width
        for i in range(height):
            try:
                if board[i][self.mouse.get_mouse_location()] == board[i + 1][self.mouse.get_mouse_location()] and\
                        board[i][self.mouse.get_mouse_location()] != 0:
                    win_counter += 1
                    if win_counter == 3:
                        return False
                    else:
                        vertical_flag = True
            except IndexError:
                vertical_flag = True
        return vertical_flag

    def check_diagonal(self, board):
        width = 7
        height = 6
        win_counter = 0
        diagonal_flag = True
        # The first bracket for the board is the height
        # The second bracket is the width
        for i in range(height):
            for j in range(width):
                try:
                    while board[i][j] == board[i + 1][j + 1] and board[i][j] != 0:
                        win_counter += 1
                        print(win_counter)
                        if win_counter == 3:
                            return False
                        else:
                            diagonal_flag = True
                        i += 1
                        j += 1
                    win_counter = 0
                except IndexError:
                    diagonal_flag = True
        return diagonal_flag
