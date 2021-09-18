import pygame
import board
import checker
import player

tracker = [[0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0]]
# The first list is "y" the second list is the "x"
player_pieces = {"player_1": 1, "player_2": 2}
player_1_turn = True
player_2_turn = False
running = False
turn_tracker = 0
clock = pygame.time.Clock()
pieces = board.Pieces((50, 41))
players = player.Player()
background = board.Background()
BLACK = (255, 255, 255)
# Initializes pygame
pygame.init()
SCREEN_SIZE = SCREEN_HEIGHT, SCREEN_WIDTH = 640, 480
flags = pygame.SCALED | pygame.RESIZABLE
screen = pygame.display.set_mode(SCREEN_SIZE, flags=flags)
pygame.display.set_caption("Connect 4!")

while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
    if player_1_turn:
        tracker = players.pick_location(tracker, player_pieces, player_1_turn, player_2_turn)
        turn_tracker += 1
        player_1_turn, player_2_turn = players.switch_players(turn_tracker)
        print(tracker)
    elif player_2_turn:
        tracker = players.pick_location(tracker, player_pieces, player_1_turn, player_2_turn)
        turn_tracker += 1
        player_1_turn, player_2_turn = players.switch_players(turn_tracker)
        print(tracker)
    # There is probably a better way to choose player pieces than this function
    pieces.place_piece(player_1_turn)
    screen.fill(BLACK)
    screen.blit(background.BACKGROUND_IMG, background.background_rect)
    screen.blit(pieces.piece2, pieces.rect2)
    pygame.display.flip()
