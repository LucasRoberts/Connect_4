import pygame


class Checker:
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
        while self.x > 0 and self.win_counter <= 3:
            if self.x-1 >= 0 and self.board[self.y][self.x-1] == self.board[self.y][self.x]:
                self.win_counter += 1

    def check_right(self):
        while self.x > self.columns and self.win_counter <= 3:
            if self.x+1 <= self.columns and self.board[self.y][self.x-1] == self.board[self.y][self.x]:
                self.win_counter += 1
                if self.win_counter == 3:
                    break


class GameOver:
    def __init__(self):
        pass

    def is_game_over(self, board, counter, end_game, player_piece):
        win_counter = 0
        if counter == 42:
            return False
        for x in range(7):
            for y in range(6):
                if board[x][y] == 1:
                    pass

