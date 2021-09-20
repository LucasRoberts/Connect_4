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
running = True
turn_tracker = 0
clock = pygame.time.Clock()
pieces = board.Pieces((50, 41))
background = board.Background()
players = player.Player()
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
# Initializes pygame
pygame.init()
SCREEN_SIZE = SCREEN_HEIGHT, SCREEN_WIDTH = 640, 480
flags = pygame.SCALED | pygame.RESIZABLE
screen = pygame.display.set_mode(SCREEN_SIZE, flags=flags)
pygame.display.set_caption("Connect 4!")


def draw_images():
    pass


while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
    # if player_1_turn:
    #     tracker = players.pick_location(tracker, player_pieces, player_1_turn, player_2_turn)
    #     turn_tracker += 1
    #     player_1_turn, player_2_turn = players.switch_players(turn_tracker)
    #     print(tracker)
    # elif player_2_turn:
    #     tracker = players.pick_location(tracker, player_pieces, player_1_turn, player_2_turn)
    #     turn_tracker += 1
    #     player_1_turn, player_2_turn = players.switch_players(turn_tracker)
    #     print(tracker)
    screen.fill(WHITE)
    screen.blit(background.BACKGROUND_IMG, background.background_rect)
    # There is probably a better way to choose player pieces than this function
    pieces.place_piece(player_1_turn)
    screen.blit(pieces.piece1, pieces.rect1)
    # TESTING MOUSE REGIONS
    # MOUSE REGION 1
    pygame.draw.line(screen, BLACK, (95, 0), (95, 85))
    pygame.draw.line(screen, BLACK, (0, 85), (95, 85))
    # MOUSE REGION 2
    pygame.draw.line(screen, BLACK, (185, 0), (185, 85))
    pygame.draw.line(screen, BLACK, (95, 85), (185, 85))
    # MOUSE REGION 3
    pygame.draw.line(screen, BLACK, (275, 0), (275, 85))
    pygame.draw.line(screen, BLACK, (185, 85), (275, 85))
    # MOUSE REGION 4
    pygame.draw.line(screen, BLACK, (365, 0), (365, 85))
    pygame.draw.line(screen, BLACK, (275, 85), (365, 85))
    # MOUSE REGION 5
    pygame.draw.line(screen, BLACK, (455, 0), (455, 85))
    pygame.draw.line(screen, BLACK, (365, 85), (455, 85))
    # MOUSE REGION 6
    pygame.draw.line(screen, BLACK, (545, 0), (545, 85))
    pygame.draw.line(screen, BLACK, (455, 85), (545, 85))
    # MOUSE REGION 7
    pygame.draw.line(screen, BLACK, (640, 0), (640, 85))
    pygame.draw.line(screen, BLACK, (545, 85), (640, 85))
    pygame.display.flip()
    pygame.display.update()
