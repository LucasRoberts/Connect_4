tracker = [[0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0]]
# The first list is "y" the second list is the "x"
player_pieces = {"player_1": 1, "player_2": 2}
player_1 = True
player_2 = False
game_over = False
turn_tracker = 0
print(player_pieces["player_2"])


# Might delete this due to Board class' player check
def switch_players(counter):
    if counter % 2 == 0:
        return True, False
    elif counter % 2 != 0:
        return False, True


def is_game_over(board, counter, end_game, player_piece):
    win_counter = 0
    if counter == 42:
        return False
    for x in range(7):
        for y in range(6):
            if board[x][y] == 1:
                pass


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

# wsu-design-ii-2021 / assignment2-junit-tdd-git-bertieDog


def pick_location(board, player_piece, player1, player2):
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


while not game_over:
    if player_1:
        tracker = pick_location(tracker, player_pieces, player_1, player_2)
        turn_tracker += 1
        player_1, player_2 = switch_players(turn_tracker)
        print(tracker)
    elif player_2:
        tracker = pick_location(tracker, player_pieces, player_1, player_2)
        turn_tracker += 1
        player_1, player_2 = switch_players(turn_tracker)
        print(tracker)

