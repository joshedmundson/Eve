from re import I
import pygame
import random
from Dot import Dot
import Death

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
start_time = True

i = 0
while running:
    for event in pygame.event.get():
        #print(clock.get_time()) 
        if event.type == pygame.QUIT:
            running = False

    screen.fill(white)
    pygame.draw.line(screen, (0, 0, 0), (width/2, 0), (width/2, height), width=4)
    
    # Move and display dots
    if start_time:
        print('start counting')
        time_since_enter = pygame.time.get_ticks() - start_time
        message = 'Milliseconds since enter: ' + str(time_since_enter)
        print(message)
        
        if (time_since_enter>2000):
            print('5 secs kill')
            dots = Death.kill_left(dots)
            
        if (time_since_enter>3000):
            print('new life')
            dots = Death.create_life(dots,num_dots)
            
        if (time_since_enter>8000):
            print('bye')
            running = False
    for dot in dots:
        #print(i)
        #i=+1
        dot.move()
        dot.display(screen)
    
    pygame.display.flip()
    clock.tick(60)  # Limit frame rate to 60 FPS
    

    
    
pygame.quit()
