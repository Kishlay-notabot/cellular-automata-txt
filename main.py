import pygame
import numpy as np
import pygame_widgets
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox
# the "k.k. config isnt giving the final equilibrium as the past version[s]"
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



def update_board(board, width, height):
    new_board = np.zeros((height, width), dtype=int)
    for y in range(height):
        for x in range(width):
            neighbors = 0
            for dy in [-1, 0, 1]:
                for dx in [-1, 0, 1]:
                    if dy == 0 and dx == 0:
                        continue
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < height and 0 <= nx < width:
                        neighbors += board[ny, nx]
            if board[y, x] == 1:
                new_board[y, x] = 1 if neighbors == 2 or neighbors == 3 else 0
            else:
                new_board[y, x] = 1 if neighbors == 3 else 0
    return new_board


pygame.init()

res = width, height = 1200, 700
viewport = 1400, 700
tile = 10
w, h = width // tile, height // tile
fps = 60  # Control the display refresh rate
simulation_speed = 60  # Control the speed of simulation updates

surface = pygame.display.set_mode(viewport)
clock = pygame.time.Clock()


# Text input box
input_box = pygame.Rect(10, height - 40, width - 20, 30)
colortab = pygame.color.Color("#FFFFFF")
pygame.draw.rect(surface, colortab,[1200,0,200,700])
font = pygame.font.Font(None, 32)
text = ''
color_inactive = pygame.Color('lightskyblue3')
color_active = pygame.Color('dodgerblue2')
color = color_inactive
grid_surface = pygame.Surface((width, height), pygame.SRCALPHA)
active = False

# Game board
board = np.zeros((h, w), dtype=int)

# Main loop
running = True
last_update_time = pygame.time.get_ticks()
time_between_updates = 1000 // simulation_speed  # Time between updates in milliseconds

while running:

    # Draw grid lines
    for x in range(0, width, tile):
        pygame.draw.line(grid_surface, pygame.Color('dimgray'), (x, 0), (x, height))
    for y in range(0, height, tile):
        pygame.draw.line(grid_surface, pygame.Color('dimgray'), (0, y), (width, y))

    # Draw cells
    for y in range(h):
        for x in range(w):
            if board[y, x] == 1:
                rect = pygame.Rect(x * tile, y * tile, tile, tile)
                pygame.draw.rect(surface, pygame.Color('white'), rect)
                print('cell added')

    surface.blit(grid_surface, (0, 0))
    # Render text input box
    txt_surface = font.render(text, True, color)
    pygame.draw.rect(surface, color, input_box, 2)
    surface.blit(txt_surface, (input_box.x + 5, input_box.y + 5))

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_box.collidepoint(event.pos):
                active = not active
                color = color_active if active else color_inactive
            else:
                active = False
                color = color_active if active else color_inactive
        if event.type == pygame.KEYDOWN:
            if active:
                if event.key == pygame.K_RETURN:
                    # Append letter configurations to the board
                    current_x = 10
                    current_y = 10
                    for letter in text:
                        if letter == ' ':
                            current_x += 1
                        else:
                            config = letter_configs.get(letter.lower(), [])
                            for y, row in enumerate(config):
                                for x, value in enumerate(row):
                                    board[current_y + y - 1, current_x + x - 1] = value
                            current_x += len(config[0]) + 1
                    text = ''
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode

    # Simulation update
    current_time = pygame.time.get_ticks()
    if current_time - last_update_time >= time_between_updates:
        board = update_board(board, w, h)
        last_update_time = current_time

    pygame.display.flip()
    clock.tick(fps)  # Control display refresh rate and overall frame rate

pygame.quit()
