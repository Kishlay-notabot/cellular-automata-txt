import pygame

# Define cell configurations for English letters
letter_configs = {
    'a': [[0,1,1,0],
          [1,0,0,1],
          [1,1,1,1],
          [1,0,0,1],
          [1,0,0,1]],
    # Define configurations for other letters
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
    
    # Draw letter 'a' at grid position (1, 1)
    draw_configuration(surface, letter_configs['a'], (0, 0), tile)
    
    pygame.display.flip()
    clock.tick(fps)
