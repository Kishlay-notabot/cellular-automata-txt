import pygame
res = width, height = 1000,700
tile = 50
w,h = width//tile, height//tile
fps = 10
pygame.init()
surface = pygame.display.set_mode(res)
clock = pygame.time.Clock()

while True:
    surface.fill(pygame.Color('black'))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    

    [pygame.draw.line(surface, pygame.Color('dimgray'), (x,0),(x,height)) for x in range(0, width, tile)]
    [pygame.draw.line(surface, pygame.Color('dimgray'), (0,y),(width,y)) for y in range(0, height, tile)]

    pygame.display.flip()
    clock.tick(fps)