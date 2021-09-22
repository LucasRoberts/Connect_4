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
    def __init__(self, board, piece_coords):
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

    def piece_gravity(self, player_piece_loc):
        if player_piece_loc == -1:
            return -1
        for below_checker in range(7):
            if below_checker == 5:
                location = self.piece_coords[below_checker][player_piece_loc]
                return location
            elif self.board[below_checker-1][player_piece_loc] != 0:
                location = self.piece_coords[below_checker-1][player_piece_loc]
                print(location)
                return location
