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


class Piece(pygame.sprite.Sprite):
    """
    Class that sets up and initializes the player pieces
    """
    def __init__(self, board, piece_coords, player_piece_dict, player_turn):
        pygame.sprite.Sprite.__init__(self)
        if player_turn:
            self.piece = "red.png"
        else:
            self.piece = "yellow.png"
        self.piece_dimensions = self.piece_dim_x, self.piece_dim_y = 70, 70
        self.image = pygame.image.load(self.piece)
        self.image = pygame.transform.smoothscale(self.image, self.piece_dimensions)
        self.rect = self.image.get_rect()
        self.board = board
        self.piece_coords = piece_coords
        self.player_piece_dict = player_piece_dict

    def place_piece(self, location):
        """
        Takes player bool flag, determine which player symbol to use
        :param location: int
        :return: piece location for each player
        """
        # location[0] is x
        # location[1] is y
        self.rect.center = (location[0], location[1])

    def piece_gravity(self, player_piece_loc, player_turn):
        """
        Checks if the y value below the player's input is empty, if it is repeats until
        it is at the 'bottom' of the board
        If the player didnt click in the specified area, ignores it
        :param player_piece_loc: int -> mouse input
        :param player_turn: bool -> decides what player's piece to use
        :return: tuple -> location for the players piece
        """
        for below_checker in range(6):
            if self.board[0][player_piece_loc] != 0:
                print("This column is already full\nSelect another spot")
                break
            elif below_checker == 5:
                location = self.piece_coords[below_checker][player_piece_loc]
                Piece.update_board(self, below_checker, player_piece_loc, self.player_piece_dict, player_turn)
                return location
            elif self.board[below_checker+1][player_piece_loc] != 0:
                location = self.piece_coords[below_checker][player_piece_loc]
                Piece.update_board(self, below_checker, player_piece_loc, self.player_piece_dict, player_turn)
                return location

    def update_board(self, x, y, player_piece, player):
        """
        Updates the board logic tracker
        :param x: int
        :param y: int
        :param player_piece: dict
        :param player: bool
        :return: matrix: updated board logic
        """
        self.board[x][y] = player_piece[player]
        return self.board
