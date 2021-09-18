import pygame

pygame.init()
SCREEN_SIZE = SCREEN_HEIGHT, SCREEN_WIDTH = 640, 480
flags = pygame.SCALED | pygame.RESIZABLE
screen = pygame.display.set_mode(SCREEN_SIZE, flags=flags)
pygame.display.set_caption("Connect 4!")
BLACK = (255, 255, 255)


class Background(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.ORIGIN = (0, 0)
        self.BACKGROUND_IMG = "Connect4Board.png"
        self.BACKGROUND_IMG = pygame.image.load(self.BACKGROUND_IMG)
        self.background_rect = self.BACKGROUND_IMG.get_rect()
        self.background_rect.topleft = self.ORIGIN


class Pieces(pygame.sprite.Sprite):
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
        if player:
            self.rect1.center = self.location
        else:
            self.rect2.center = self.location


clock = pygame.time.Clock()
running = True
# (50, 41) are the perfect coords to cover the first hole
pieces = Pieces((50, 41))
player = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
    background = Background()
    screen.fill(BLACK)
    screen.blit(background.BACKGROUND_IMG, background.background_rect)
    pieces.place_piece(player)
    screen.blit(pieces.piece1, pieces.rect1)
    pygame.display.flip()
