import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
width, height = 800, 600
screen = pygame.display.set_mode((width, height))

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get mouse position
    x, y = pygame.mouse.get_pos()

    # Normalize x to range 0-1
    normalized_r = x / width

    # Set RGB values
    r = int(normalized_r * 255)
    g = 0
    b = 0

    # Fill the screen with the color
    screen.fill((r, g, b))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
