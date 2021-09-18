import pygame
pygame.init()


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        pass

    def pick_location(self, board, player_piece, player1, player2):
        if player1:
            x_loc = int(input("Player 1 enter which row you want to change(1-7): ")) - 1
            y_loc = int(input("Now enter which column you want to change(1-6): ")) - 1
            while x_loc > 6 or x_loc < 0:
                print("Enter a x value in between 1 and 7\n")
                print("First while")
                x_loc = int(input("Enter which row you want to change(1-7): ")) - 1
            while y_loc > 5 or y_loc < 0:
                print("Enter a y value in between 1 and 6\n")
                print("Second While")
                y_loc = int(input("Enter which column you want to change(1-6): ")) - 1
            while board[y_loc][x_loc] > 0:
                print("That space was already used, enter another location\n")
                x_loc = int(input("Enter which row you want to change(1-7): ")) - 1
                y_loc = int(input("Enter which column you want to change(1-6): ")) - 1
            board[y_loc][x_loc] = player_piece["player_1"]
            return board
        elif player2:
            x_loc = int(input("Player 2 enter which row you want to change(1-7): ")) - 1
            y_loc = int(input("Now enter which column you want to change(1-6): ")) - 1
            while x_loc > 6 or x_loc < 0:
                print("Enter a x value in between 1 and 7\n")
                print("First while")
                x_loc = int(input("Enter which row you want to change(1-7): ")) - 1
            while y_loc > 5 or y_loc < 0:
                print("Enter a y value in between 1 and 6\n")
                print("Second While")
                y_loc = int(input("Enter which column you want to change(1-6): ")) - 1
            while board[y_loc][x_loc] > 0:
                print("That space was already used, enter another location\n")
                x_loc = int(input("Enter which row you want to change(1-7): ")) - 1
                y_loc = int(input("Enter which column you want to change(1-6): ")) - 1
            board[y_loc][x_loc] = player_piece["player_2"]
            return board

    def switch_players(self, turn_tracker):
        self.turn_tracker = turn_tracker
        if self.turn_tracker % 2 == 0:
            return True, False
        else:
            return False, True
