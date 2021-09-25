import pygame


class Background(pygame.sprite.Sprite):
    """
    Class that sets up the background image
    """

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.ORIGIN = (0, 0)
        self.BACKGROUND_IMG = "Connect4Board.png"
        self.BACKGROUND_IMG = pygame.image.load(self.BACKGROUND_IMG)
        self.background_rect = self.BACKGROUND_IMG.get_rect()
        self.background_rect.topleft = self.ORIGIN


class Pieces(pygame.sprite.Sprite):
    """
    Class that sets up and initializes the player pieces
    """
    def __init__(self, board, piece_coords, player_piece_dict):
        pygame.sprite.Sprite.__init__(self)
        self.piece1 = "red.png"
        self.piece2 = "yellow.png"
        self.piece_dimensions = self.piece_x, self.piece_y = 70, 70
        self.piece1 = pygame.image.load(self.piece1)
        self.piece1 = pygame.transform.smoothscale(self.piece1, self.piece_dimensions)
        self.piece2 = pygame.image.load(self.piece2)
        self.piece2 = pygame.transform.smoothscale(self.piece2, self.piece_dimensions)
        self.rect1 = self.piece1.get_rect()
        self.rect2 = self.piece2.get_rect()
        self.board = board
        self.piece_coords = piece_coords
        self.player_piece_dict = player_piece_dict

    def place_piece(self, location, player):
        """
        Takes player bool flag, determine which player symbol to use
        :param player: Bool
        :param location: int
        :return: piece location for each player
        """
        if player:
            # location[0] is x
            # location[1] is y
            self.rect1.center = (location[0], location[1])
        else:
            self.rect2.center = (location[0], location[1])

    def piece_gravity(self, player_piece_loc, player_turn):
        """
        Checks if the y value below the player's input is empty, if it is repeats until
        it is at the 'bottom' of the board
        If the player didnt click in the specified area, ignores it
        :param player_piece_loc: int -> mouse input
        :return: tuple -> location for the players piece
        """
        if player_piece_loc == -1:
            return -1
        for below_checker in range(6):
            # THIS IS WHERE I LEFT OFF
            # For some reason the placement of pieces is happening twice
            # The first if statement is to try and make sure you cant place
            # pieces in an already full column
            # PROBLEM: This will break place_piece because it returns null
            if self.board[0][player_piece_loc] != 0:
                print("This column is already full")
                break
            elif below_checker == 5:
                location = self.piece_coords[below_checker][player_piece_loc]
                Pieces.update_board(self, below_checker, player_piece_loc, self.player_piece_dict, player_turn)
                print(self.board)
                return location
            elif self.board[below_checker+1][player_piece_loc] != 0:
                location = self.piece_coords[below_checker][player_piece_loc]
                Pieces.update_board(self, below_checker, player_piece_loc, self.player_piece_dict, player_turn)
                print(self.board)
                return location

    def update_board(self, x, y, player_piece, player):
        self.board[x][y] = player_piece[player]
        return self.board

