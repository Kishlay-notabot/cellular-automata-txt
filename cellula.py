# shader for cellular automation
import pygame 
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
img = pygame.image.load('image.png')

while True:
    screen.fill((0,0,0))
    screen.blit(img, pygame.mouse.get_pos())
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.flip()
    clock.tick(60)