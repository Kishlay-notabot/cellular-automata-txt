# shader for cellular automation
import pygame 
import sys
import moderngl
import array
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
ctx = moderngl.create_context()
quadb = ctx.buffer(data=array(f'[

]'))
while True:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.flip()
    clock.tick(60)