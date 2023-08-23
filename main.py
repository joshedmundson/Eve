from re import I
import pygame
import random
from Dot import Dot
from Food import Food
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

# Number of food
nfood = 1000
# Colors
white = (255, 255, 255)
dot_color = (0, 0, 255)

# Create a Population of Dots
gen = 0
dot_population = Population(500, 5, 2, 6, width, height, mutprob=20/100)
#food_pop = [Food(width, height) for _ in range(nfood)]
food_pop = Food(gen,width,height)

# Define the cull condition 
def cull_left(dot):
    return dot.position[0] > width/2
def starve(dot):
    return dot.hunger>1

# Main loop
running = True
clock = pygame.time.Clock()
start_time = True

dtime = 10000
runs = 0

while running:
    runs+=1
    for event in pygame.event.get():
        #print(clock.get_time()) 
        if event.type == pygame.QUIT:
            running = False

    screen.fill(white)
    pygame.draw.line(screen, (0, 0, 0), (width/2, 0), (width/2, height), width=4)
    
    # Move and display dots
    if start_time:
        #print('start counting')
        time_since_enter = pygame.time.get_ticks() - start_time
        message = 'Milliseconds since enter: ' + str(time_since_enter)
        #print(runs)
        #print(message)
        
        t = time_since_enter
        #if ((t%dtime>0)&(t%dtime<200)):
        if (runs%50==0):
            gen+=1
            print('next generation')
            print(runs)
            print('survivors',len(dot_population.population))
            #dot_population.next_generation(cull_left)
            dot_population.reproduce()
            food_pop = Food(gen,width,height)
            #food_pop = [Food(width, height) for _ in range(nfood)]
    
    food_pop.display_all(screen)
    #for fd in food_pop:
        #fd.display(screen)  
        #print(len(food_pop))
    for dot in dot_population.population:

        dot.hungry(runs)
        dot.feed(food_pop)
        
        dot.display(screen)

    dot_population.cull(starve)
    pygame.display.flip()
    clock.tick(20)  # Limit frame rate to 60 FPS
    
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
