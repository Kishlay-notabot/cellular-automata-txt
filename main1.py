import pygame
import numpy as np
import pygame_widgets
from pygame_widgets.slider import Slider 
from pygame_widgets.textbox import TextBox 

# letter_configurations:
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
    new_board = np.zeros((height,width), dtype=int)
    for y in range(height):
      for x in range(width):
        neighbours = 0
        for dy in [-1,0,1]:
            for dx in [-1,0,1]:
                if dy==0 and dx==0:
                    continue
                ny, nx = y +dy, x+dx 
                if 0 <= ny <height and 0 <= nx < width: 
                    neighbours += board[ny, nx]
                    if board[y,x] ==1:
                        new_board[y,x] = 1 if neighbours ==2 or neighbours == 3 else 0
                    else:
                        new_board[y,x] = 1 if neighbours == 3 else 0
    return new_board



pygame.init()
# pygame initialized............................

res = width, height = 1400, 700
viewport_left = 1200, 700
tile = 10
fps = 60 
simulation_speed = 60
surface_full = pygame.display.set_mode(res)
viewport_surface_left = pygame.Surface(viewport_left)
viewport_surface_left.fill((0,0,0)) # gray
clock = pygame.time.Clock()
viewport_right = 200, 700
viewport_surface_right = pygame.Surface(viewport_right)
viewport_surface_right.fill((255,255,255)) #white
# both surfaces initialised
# width and height properties :

left_width = viewport_surface_left.get_width()
left_height = viewport_surface_left.get_height()

# grid
def draw_grid(surface, width, height, tile_size):
      for x in range(0, width, tile):
            pygame.draw.line(surface, pygame.Color('dimgray'), (x,0), (x, height))
      for y in range(0, height, tile):
            pygame.draw.line(surface, pygame.Color('dimgray'),(0,y),(width, y))
      surface.blit(surface, (0,0))
# draw cells
board = np.zeros((left_height, left_width), dtype=int)
def draw_cells():
      for y in range(left_height):
            for x in range(left_width):
                  if board[y,x] == 1:
                        rect = pygame.Rect(x*tile, y*tile,tile,tile) # this todo
                        pygame.draw.rect(viewport_surface_left, pygame.Color('white'), rect)
                        # print('cell added')
# cell variables
current_x = 10
current_y = 10
text = ''

#inputbox
rect_x = 10
rect_y = 645  
rect_width = 1180
rect_height = 40
rect_color_active = (255,105,180)
rect_color_inactive = (255,0,0)
rect_color = rect_color_inactive
active = False
font = pygame.font.Font(None, 32)

rect = pygame.Rect(rect_x, rect_y, rect_width, rect_height)
rect_surface = pygame.Surface((rect_width, rect_height), pygame.SRCALPHA)

# font render on textbox





# main loop
running = True
while running:
      draw_grid(viewport_surface_left, left_width, left_height, tile)
      draw_cells()
      surface_full.blit(viewport_surface_left, (0, 0))
      surface_full.blit(viewport_surface_right,(1200,0))
      # pygame.draw.rect(viewport_surface_left, rect_color, rect, 2)
      rect_surface.fill((0, 0, 0, 0))  # Transparent background
      pygame.draw.rect(rect_surface, rect_color, (0, 0, rect_width, rect_height), 2)
      txt_surface = font.render(text, True, rect_color_active)
      rect_surface.blit(txt_surface, (5, 5))
      surface_full.blit(rect_surface, (rect_x, rect_y))

      


# keystrokes
      for event in pygame.event.get():
            if event.type == pygame.QUIT:
                  running = False
                  pygame.quit()
                  exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                  if rect.collidepoint(event.pos):
                        active = not active
                        rect_color = rect_color_active if active else rect_color_inactive
                  else:
                        active = False
                        rect_color = rect_color_inactive
            # appending
            if event.type == pygame.KEYDOWN:
                  if active:
                        if event.key == pygame.K_RETURN:
                              for letter in text:
                                    if letter == ' ':
                                          current_x += 1
                                    else:
                                          config = letter_configs.get(letter.lower(), [])
                                          for y, row in enumerate(config):
                                                for x, value in enumerate(row):
                                                      board[current_y + y - 1, current_x + x -1] = value
                                          current_x += len(config[0])+1
                              text = ''
                        elif event.key == pygame.K_BACKSPACE:
                              text = text[:-1]
                        else:
                              text += event.unicode

                              
      board = update_board(board, left_width, left_height)                        
      pygame.display.flip()
      clock.tick(fps)