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
res = width, height = 1400, 700
viewport_left = 1200, 700
tile = 10
w, h = width //tile, height // tile
fps = 60 
simulation_speed = 60
surface_full = pygame.display.set_mode(res)
viewport_surface_left = pygame.Surface(viewport_left)
viewport_surface_left.fill((0,0,0)) # gray
clock = pygame.time.Clock()
viewport_right = 200, 700
viewport_surface_right = pygame.Surface(viewport_right)
viewport_surface_right.fill((255,255,255)) #white
#inputbox
rect_x = 10
rect_y = 645  
rect_width = 1180
rect_height = 40
rect_color = (255, 0, 0)  # Red color
rect = pygame.Rect(rect_x, rect_y, rect_width, rect_height)




# main loop
running = True
while running:
      surface_full.blit(viewport_surface_left, (0, 0))
      surface_full.blit(viewport_surface_right,(1200,0))
      pygame.draw.rect(viewport_surface_left, rect_color, rect, 2)
      


# keystrokes
      for event in pygame.event.get():
            if event.type == pygame.QUIT:
                  running = False
      pygame.display.flip()
      clock.tick(fps)