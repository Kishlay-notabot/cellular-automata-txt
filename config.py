import pygame

# Define cell configurations for English letters
letter_configs = {
    'a': [[0,1,1,0],
          [1,0,0,1],
          [1,1,1,1],
          [1,0,0,1],
          [1,0,0,1]],
    'b': [[1,1,1,0],
          [1,0,0,1],
          [1,1,1,0],
          [1,0,0,1],
          [1,1,1,0]],
    'c': [[0,1,1,1],
          [1,0,0,0],
          [1,0,0,0],
          [1,0,0,0],
          [0,1,1,1]]
}

# Function to draw a configuration at a given position
def draw_configuration(surface, config, pos, tile_size):
    for y, row in enumerate(config):
        for x, value in enumerate(row):
            if value == 1:
                rect = pygame.Rect((pos[0] + x) * tile_size, (pos[1] + y) * tile_size, tile_size, tile_size)
                pygame.draw.rect(surface, pygame.Color('white'), rect)

# Initialize pygame
pygame.init()

# Define constants
res = width, height = 1000, 700
tile = 50
w, h = width // tile, height // tile
fps = 10

# Create display surface
surface = pygame.display.set_mode(res)
clock = pygame.time.Clock()

# Main loop
while True:
    surface.fill(pygame.Color('black'))
    
    # Draw grid lines
    for x in range(0, width, tile):
        pygame.draw.line(surface, pygame.Color('dimgray'), (x, 0), (x, height))
    for y in range(0, height, tile):
        pygame.draw.line(surface, pygame.Color('dimgray'), (0, y), (width, y))
    
    # Draw letters
    current_x = 0
    for letter in ['a', 'b', 'c']:
        draw_configuration(surface, letter_configs[letter], (current_x, 1), tile)
        current_x += len(letter_configs[letter][0]) + 1  # Add gap of one grid box
    
    pygame.display.flip()
    clock.tick(fps)
