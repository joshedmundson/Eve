import pygame
import random

# Initialize pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Evolution Simulation")

# Colors
white = (255, 255, 255)
dot_color = (0, 0, 255)

# Dot class
class Dot:
    def __init__(self):
        self.x = random.randint(0, width)
        self.y = random.randint(0, height)
        self.speed_x = random.uniform(-2, 2)
        self.speed_y = random.uniform(-2, 2)
    
    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

        if self.x < 0 or self.x > width:
            self.speed_x *= -1
        if self.y < 0 or self.y > height:
            self.speed_y *= -1
    
    def display(self):
        pygame.draw.circle(screen, dot_color, (int(self.x), int(self.y)), 5)

# Create a list of dots
num_dots = 20
dots = [Dot() for _ in range(num_dots)]

# Main loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill(white)
    
    # Move and display dots
    for dot in dots:
        dot.move()
        dot.display()
    
    pygame.display.flip()
    clock.tick(60)  # Limit frame rate to 60 FPS

pygame.quit()
