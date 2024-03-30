import pygame
import time

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
          [0,1,1,1]],
    'd': [[1,1,1,0],
          [1,0,0,1],
          [1,0,0,1],
          [1,0,0,1],
          [1,1,1,0]]   
}
 
def draw_configuration(surface, config, pos, tile_size):
    for y, row in enumerate(config):
        for x, value in enumerate(row):
            if value == 1:
                rect = pygame.Rect((pos[0] + x) * tile_size, (pos[1] + y) * tile_size, tile_size, tile_size)
                pygame.draw.rect(surface, pygame.Color('white'), rect)
 
pygame.init()
 
res = width, height = 1000, 700
tile = 5
w, h = width // tile, height // tile
fps = 10 
surface = pygame.display.set_mode(res)
clock = pygame.time.Clock()

# Text input box
input_box = pygame.Rect(10, height - 40, width - 20, 30)
font = pygame.font.Font(None, 32)
text = ''
color_inactive = pygame.Color('lightskyblue3')
color_active = pygame.Color('dodgerblue2')
color = color_inactive

active = False

final_grid = []

# Main loop
while True:
    surface.fill(pygame.Color('black'))
    
    # Draw grid lines
    for x in range(0, width, tile):
        pygame.draw.line(surface, pygame.Color('dimgray'), (x, 0), (x, height))
    for y in range(0, height, tile):
        pygame.draw.line(surface, pygame.Color('dimgray'), (0, y), (width, y))
    
    # Draw letters
    current_x = 1
    for letter in text:
        if letter == ' ':
            # Add space equivalent to one box width
            current_x += 1
        else:
            draw_configuration(surface, letter_configs[letter], (current_x, 1), tile)
            current_x += len(letter_configs[letter][0]) + 1  # Add gap of one grid box
    
    # Render text input box
    txt_surface = font.render(text, True, color)
    pygame.draw.rect(surface, color, input_box, 2)
    surface.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
    
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
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
                    # Clear the white pixels and store cell configuration in final_grid
                    final_grid = []
                    for y in range(h):
                        row = []
                        for x in range(w):
                            cell_rect = pygame.Rect(x * tile, y * tile, tile, tile)
                            if surface.get_at(cell_rect.topleft) == pygame.Color('white'):
                                row.append(1)
                                pygame.draw.rect(surface, pygame.Color('black'), cell_rect)
                                
                                print('cleared')
                              
                            else:
                                row.append(0)
                        final_grid.append(row)
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode
    # Display the final grid stored in final_grid
    for y in range(h):
        for x in range(w):
            if final_grid and final_grid[y][x] == 1:
                rect = pygame.Rect(x * tile, y * tile, tile, tile)
                pygame.draw.rect(surface, pygame.Color('white'), rect)
                print('renderedfinalgrid')
    
    pygame.display.flip()
    clock.tick(fps)
