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
    def __init__(self, location):
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
        self.location = location

    def place_piece(self, player):
        """
        Takes player bool flag, determine which player symbol to use
        :param player: Bool
        :return: piece location for each player
        """
        if player:
            self.rect1.center = self.location
        else:
            self.rect2.center = self.location
