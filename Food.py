import random
from tkinter import SE 
from Genome import Genome
import numpy as np
from Brain import Brain
import pygame

class Food():


    def __init__(self, gen,screen_width, screen_height, n=500):
        # Initiate positions 
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.position = np.array([random.randint(0, self.screen_width),
                                  random.randint(0, self.screen_height)])
        self.no_food = n
        #rand = np.random.randint(0,len(self.genome.genome))
        self.colour = (0,0,255)
        self.allfoods = None
        self.seed = gen
        self.spawnlocs = None
        self.distribute()

    def display(self, screen):
        '''
        Displays the food on the screen
        
        Args:
        screen (pygame.display): The screen to display the food on
        
        Returns:
        None
        '''
        pygame.draw.rect(screen, self.colour,pygame.Rect(self.position[0]-1, self.position[1]+1,4,4))
        
    def display_all(self,screen):
        #print('food',self.allfoods)
        for food in self.allfoods:
            pygame.draw.rect(screen,self.colour,pygame.Rect(food[0]-1, food[1]+1,4,4))
            
    def distribute(self,nlocs=4):
        '''
        Distribute food across 4 spawning locations
        '''
        
        np.random.seed(self.seed)
        locs = []
        for i in range(nlocs):
            locs.append(np.array([random.randint(0, self.screen_width),
                                  random.randint(0, self.screen_height)]))        
        R = int(self.screen_height/nlocs)
        R=10000
        #print(R)
        num_points = self.no_food
        self.spawnlocs = locs
        
        #print('locs',locs)
        foods=[]
        xs=[]
        ys=[]
        for i in range(nlocs):
            theta = np.random.uniform(0,2*np.pi, int(num_points/nlocs))
            radius = np.random.uniform(0,R, int(num_points/nlocs)) ** 0.5
            xs.extend(np.round(radius*np.cos(theta)+locs[i][0]))
            ys.extend(np.round(radius*np.sin(theta)+locs[i][1]))
        
        foods_ = []
        foods_.append(xs)
        foods_.append(ys)
        foods = np.transpose(foods_)
        #print('distribute', foods)
        self.allfoods=foods
        
        
        