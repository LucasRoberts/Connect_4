"""
Author: Lucas Roberts
Description: A simple game of Connect 4 using the pygame library
Date: 9/25/2021
"""
import pygame
import board
import checker
import player
import mouse

# Creating the board piece tracking array
tracker = [[0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0]]
# Move this into Piece class
piece_position_list = [[(50, 41), (140, 41), (230, 41), (320, 41), (410, 41), (500, 41), (590, 41)],
                       [(50, 121), (140, 121), (230, 121), (320, 121), (410, 121), (500, 121), (590, 121)],
                       [(50, 201), (140, 201), (230, 201), (320, 201), (410, 201), (500, 201), (590, 201)],
                       [(50, 281), (140, 281), (230, 281), (320, 281), (410, 281), (500, 281), (590, 281)],
                       [(50, 361), (140, 361), (230, 361), (320, 361), (410, 361), (500, 361), (590, 361)],
                       [(50, 441), (140, 441), (230, 441), (320, 441), (410, 441), (500, 441), (590, 441)]]
# player variables
player_pieces = {True: 1, False: 2}
player_flag = True
running = True
turn_tracker = 0
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
# Initializes pygame
pygame.init()
SCREEN_SIZE = SCREEN_HEIGHT, SCREEN_WIDTH = 640, 480
clock = pygame.time.Clock()
flags = pygame.SCALED | pygame.RESIZABLE
screen = pygame.display.set_mode(SCREEN_SIZE, flags=flags)
pygame.display.set_caption("Connect 4!")
# Initializing classes
background = board.Background()
players = player.Player()
mouse = mouse.Mouse()
checker = checker.Checker(board, player, player_pieces)
# Creating a sprite group
player_token_group = pygame.sprite.Group()


def get_position():
    x_loc = mouse.get_mouse_location()
    return x_loc


while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Checks for the players input, this will grab where the player places their piece
            if mouse.get_mouse_location() != -1 and tracker[0][mouse.get_mouse_location()] == 0:
                piece = board.Piece(tracker, piece_position_list, player_pieces, player_flag)
                piece.place_piece(piece.piece_gravity(get_position(), player_flag))
                player_token_group.add(piece)
                turn_tracker += 1
                player_flag = players.switch_players(turn_tracker)
                running = checker.is_game_over(turn_tracker, tracker)
                screen.blit(piece.image, piece.rect)
    # This sets the background to white and then adds the connect4.png on top
    screen.fill(WHITE)
    screen.blit(background.BACKGROUND_IMG, background.background_rect)
    for entity in player_token_group:
        screen.blit(entity.image, entity.rect)
    # Player turn
    pygame.display.flip()
    pygame.display.update()

# if __name__ == "__main__":
#     main()
