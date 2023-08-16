from re import I
import pygame
import random
from Dot import Dot

# Initialize pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Evolution Simulation")

# Colors
white = (255, 255, 255)
dot_color = (0, 0, 255)

# Create a list of dots
num_dots = 1000
dots = [Dot(2, 2, 2, width, height) for _ in range(num_dots)]

# Main loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill(white)
    pygame.draw.line(screen, (0, 0, 0), (width/2, 0), (width/2, height), width=4)
    
    # Move and display dots

    for dot in dots:
        dot.move()
        dot.display(screen)
    
    pygame.display.flip()
    clock.tick(60)  # Limit frame rate to 60 FPS
pygame.quit()
