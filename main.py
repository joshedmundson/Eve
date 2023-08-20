from re import I
import pygame
import random
from Dot import Dot
import numpy as np
import csv
import pickle as pkl
from Population import Population

# Initialize pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Evolution Simulation")

# Colors
white = (255, 255, 255)
dot_color = (0, 0, 255)

# Create a Population of Dots
dot_population = Population(1000, 2, 2, 4, width, height, mutprob=1/100)

# Define the cull condition 
def cull_left(dot):
    return dot.position[0] > width/2

# Main loop
running = True
clock = pygame.time.Clock()
start_time = True

dtime = 10000
gen = 0

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
        
        t = time_since_enter
        if ((t%dtime>0)&(t%dtime<50)):
            print('next generation')
            dot_population.next_generation(cull_left)
            
    for dot in dot_population.population:
        #print(i)
        #i=+1
        dot.move()
        dot.display(screen)
    
    pygame.display.flip()
    clock.tick(30)  # Limit frame rate to 60 FPS
    
#keys = pool_evo.keys()
#filename = open('pool_evo.pkl','wb')
#pkl.dump(pool_evo,filename)
#filename.close()
#print(pool_evo['Generation 0'])
"""
with open('Pool_evolution.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=keys)
    writer.writeheader()
    writer.writerows(pool_evo)    
#np.save('pool_evo.txt', pool_evo)   
"""
pygame.quit()
