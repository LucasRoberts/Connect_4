import pygame

pygame.init()
ORIGIN = (0, 0)
SCREEN_SIZE = SCREEN_HEIGHT, SCREEN_WIDTH = 640, 480
flags = pygame.SCALED | pygame.RESIZABLE
screen = pygame.display.set_mode(SCREEN_SIZE, flags=flags)
BACKGROUND_IMG = "Connect4Board.png"
pygame.display.set_caption("Connect 4!")
BLACK = (255, 255, 255)


class Background(pygame.sprite.Sprite):
    def __init__(self, image, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.topleft = location


class Pieces(pygame.sprite.Sprite):
    def __init__(self, image1, image2, location):
        pygame.sprite.Sprite.__init__(self)
        self.image1 = pygame.image.load(image1)
        self.image2 = pygame.image.load(image2)
        self.rect1 = self.image1.get_rect()
        self.rect2 = self.image2.get_rect()
        self.location = location
        self.turn_tracker = ""

    def choose_piece(self, turn_tracker):
        self.turn_tracker = turn_tracker
        if self.turn_tracker % 2 == 0:
            return True
        else:
            return False

    def place_piece(self, player):
        if player:
            self.rect1.topleft = self.location
        else:
            self.rect2.topleft = self.location


clock = pygame.time.Clock()
running = True
pieces = Pieces()
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
    background = Background(BACKGROUND_IMG, ORIGIN)
    screen.fill(BLACK)
    screen.blit(background.image, background.rect)
    pygame.display.flip()
