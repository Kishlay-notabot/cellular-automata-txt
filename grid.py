import pygame

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
    # Other letter configurations...
}

def draw_configuration(surface, config, pos, tile_size):
    for y, row in enumerate(config):
        for x, value in enumerate(row):
            if value == 1:
                rect = pygame.Rect((pos[0] + x) * tile_size, (pos[1] + y) * tile_size, tile_size, tile_size)
                pygame.draw.rect(surface, pygame.Color('white'), rect)

def export_grid_state(grid, file_name):
    with open(file_name, 'w') as file:
        for row in grid:
            file.write(' '.join(map(str, row)) + '\n')

pygame.init()

res = width, height = 1000, 700
tile = 5
w, h = width // tile, height // tile
fps = 10 
surface = pygame.display.set_mode(res)
clock = pygame.time.Clock()

grid = [[0] * w for _ in range(h)]  # Initialize the grid with zeros

# Text input box
input_box = pygame.Rect(10, height - 40, width - 20, 30)
font = pygame.font.Font(None, 32)
text = ''
color_inactive = pygame.Color('lightskyblue3')
color_active = pygame.Color('dodgerblue2')
color = color_inactive
active = False

# Button
button = pygame.Rect(width // 2 - 50, height - 80, 100, 50)
button_text = font.render('Render', True, (255, 255, 255))

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
            current_x += 1
        else:
            draw_configuration(surface, letter_configs[letter], (current_x, 1), tile)
            current_x += len(letter_configs[letter][0]) + 1

    # Render text input box
    txt_surface = font.render(text, True, color)
    pygame.draw.rect(surface, color, input_box, 2)
    surface.blit(txt_surface, (input_box.x + 5, input_box.y + 5))

    # Render button
    
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
                    text = text.lower()
                    export_grid_state(grid, 'grid_state.txt')  # Save grid state to file
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode

    pygame.display.flip()
    clock.tick(fps)
