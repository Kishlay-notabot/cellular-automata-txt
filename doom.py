import pygame
import numpy as np

# Initialize Pygame
pygame.init()
letter_configs = {

      '.': [[0,0,0,0],
            [0,0,0,1],
            [0,1,0,1],
            [0,0,1,1]],

    'a': [[0, 1, 1, 0],
          [1, 0, 0, 1],
          [1, 1, 1, 1],
          [1, 0, 0, 1],
          [1, 0, 0, 1]],

    'b': [[1,1,1,0],
          [1,0,0,1],
          [1,1,1,0],
          [1,0,0,1],
          [1,1,1,0]],
    'c': [[0,1,1,1],
          [1,0,0,0],
          [1,0,0,0],
          [1,0,0,0],
          [0,1,1,1]],
    'd': [[1,1,1,0],
          [1,0,0,1],
          [1,0,0,1],
          [1,0,0,1],
          [1,1,1,0]],
    'e': [[1,1,1,1],
          [1,0,0,0],
          [1,1,1,0],
          [1,0,0,0],
          [1,1,1,1]],
    'f': [[1,1,1,1],
          [1,0,0,0],
          [1,1,1,0],
          [1,0,0,0],
          [1,0,0,0]],
    'g': [[0,1,1,1],
          [1,0,0,0],
          [1,0,1,1],
          [1,0,0,1],
          [0,1,1,1]],
    'h': [[1,0,0,1],
          [1,0,0,1],
          [1,1,1,1],
          [1,0,0,1],
          [1,0,0,1]],
    'i': [[1,1,1,1],
          [0,1,0,0],
          [0,1,0,0],
          [0,1,0,0],
          [1,1,1,1]],
    'j': [[1,1,1,1],
          [0,0,0,1],
          [0,0,0,1],
          [1,0,0,1],
          [0,1,1,0]],
    'k': [[1,0,0,1],
          [1,0,1,0],
          [1,1,0,0],
          [1,0,1,0],
          [1,0,0,1]],
    'l': [[1,0,0,0],
          [1,0,0,0],
          [1,0,0,0],
          [1,0,0,0],
          [1,1,1,1]],
    'm': [[1,0,0,0,1],
          [1,1,0,1,1],
          [1,0,1,0,1],
          [1,0,0,0,1],
          [1,0,0,0,1]],
    'n': [[1,0,0,0,1],
          [1,1,0,0,1],
          [1,0,1,0,1],
          [1,0,0,1,1],
          [1,0,0,0,1]],
    'o': [[0,1,1,0],
          [1,0,0,1],
          [1,0,0,1],
          [1,0,0,1],
          [0,1,1,0]],
    'p': [[1,1,1,0],
          [1,0,0,1],
          [1,1,1,0],
          [1,0,0,0],
          [1,0,0,0]],
    'q': [[0,1,1,0],
          [1,0,0,1],
          [1,0,0,1],
          [1,0,1,1],
          [0,1,1,1]],
    'r': [[1,1,1,0],
          [1,0,0,1],
          [1,1,1,0],
          [1,0,1,0],
          [1,0,0,1]],
    's': [[0,1,1,1],
          [1,0,0,0],
          [0,1,1,0],
          [0,0,0,1],
          [1,1,1,0]],
    't': [[1,1,1,1],
          [0,1,0,0],
          [0,1,0,0],
          [0,1,0,0],
          [0,1,0,0]],
    'u': [[1,0,0,1],
          [1,0,0,1],
          [1,0,0,1],
          [1,0,0,1],
          [0,1,1,0]],
    'v': [[1,0,0,0,1],
          [1,0,0,0,1],
          [0,1,0,1,0],
          [0,1,0,1,0],
          [0,0,1,0,0]],
    'w': [[1,0,0,0,1],
          [1,0,0,0,1],
          [1,0,1,0,1],
          [1,1,0,1,1],
          [1,0,0,0,1]],
    'x': [[1,0,0,0,1],
          [0,1,0,1,0],
          [0,0,1,0,0],
          [0,1,0,1,0],
          [1,0,0,0,1]],
    'y': [[1,0,0,1],
          [1,0,0,1],
          [0,1,1,0],
          [0,0,0,1],
          [0,0,0,1]],
    'z': [[1,1,1,1],
          [0,0,0,1],
          [0,0,1,0],
          [0,1,0,0],
          [1,1,1,1]]
}
# Screen and grid setup
res = width, height = 1400, 700
viewport_left = 1200, 700
tile = 10
fps = 60
surface_full = pygame.display.set_mode(res)
viewport_surface_left = pygame.Surface(viewport_left)
viewport_surface_right = pygame.Surface((200, 700))
clock = pygame.time.Clock()

left_width = viewport_surface_left.get_width()
left_height = viewport_surface_left.get_height()

# Initialize board
board = np.zeros((left_height // tile, left_width // tile), dtype=int)

# Grid drawing function
def draw_grid(surface, width, height, tile_size):
    for x in range(0, width, tile_size):
        pygame.draw.line(surface, pygame.Color('dimgray'), (x, 0), (x, height))
    for y in range(0, height, tile_size):
        pygame.draw.line(surface, pygame.Color('dimgray'), (0, y), (width, y))

# Cell drawing function
def draw_cells():
    for y in range(board.shape[0]):
        for x in range(board.shape[1]):
            if board[y, x] == 1:
                rect = pygame.Rect(x * tile, y * tile, tile, tile)
                pygame.draw.rect(viewport_surface_left, pygame.Color('white'), rect)

# Update board function (for Game of Life)
def update_board(board):
    new_board = np.zeros_like(board)
    for y in range(board.shape[0]):
        for x in range(board.shape[1]):
            neighbours = np.sum(board[max(0, y-1):min(y+2, board.shape[0]), max(0, x-1):min(x+2, board.shape[1])]) - board[y, x]
            if board[y, x] == 1 and neighbours in [2, 3]:
                new_board[y, x] = 1
            elif board[y, x] == 0 and neighbours == 3:
                new_board[y, x] = 1
    return new_board

# Text input box setup
rect = pygame.Rect(10, 645, 1180, 40)
active = False
text = ''
font = pygame.font.Font(None, 32)
rect_color_active = pygame.Color('dodgerblue2')
rect_color_inactive = pygame.Color('lightskyblue3')
rect_color = rect_color_inactive

# Main loop
running = True
while running:
    surface_full.fill((0, 0, 0))
    viewport_surface_left.fill((0, 0, 0))
    
    draw_grid(viewport_surface_left, left_width, left_height, tile)
    draw_cells()
    
    surface_full.blit(viewport_surface_left, (0, 0))
    surface_full.blit(viewport_surface_right, (1200, 0))

    # Draw input box
    txt_surface = font.render(text, True, rect_color_active)
    rect_surface = pygame.Surface(rect.size, pygame.SRCALPHA)
    pygame.draw.rect(rect_surface, rect_color, rect_surface.get_rect(), 2)
    rect_surface.blit(txt_surface, (5, 5))
    surface_full.blit(rect_surface, rect.topleft)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if rect.collidepoint(event.pos):
                active = not active
                rect_color = rect_color_active if active else rect_color_inactive
            else:
                active = False
                rect_color = rect_color_inactive

        if event.type == pygame.KEYDOWN and active:
            if event.key == pygame.K_RETURN:
                current_x, current_y = 10, 10
                for letter in text:
                    if letter == ' ':
                        current_x += 1
                    else:
                        config = letter_configs.get(letter.lower(), [])
                        for y, row in enumerate(config):
                            for x, value in enumerate(row):
                                if 0 <= current_y + y < board.shape[0] and 0 <= current_x + x < board.shape[1]:
                                    board[current_y + y, current_x + x] = value
                        current_x += len(config[0]) + 1
                text = ''
            elif event.key == pygame.K_BACKSPACE:
                text = text[:-1]
            else:
                text += event.unicode

    board = update_board(board)
    pygame.display.flip()
    clock.tick(fps)

pygame.quit()