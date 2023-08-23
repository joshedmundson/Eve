import random
from tkinter import SE 
from Genome import Genome
import numpy as np
from Brain import Brain
import pygame

class Food():


    def __init__(self, screen_width, screen_height):
        # Initiate positions 
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.position = np.array([random.randint(0, self.screen_width),
                                  random.randint(0, self.screen_height)])
        #self.no_food = n
        #rand = np.random.randint(0,len(self.genome.genome))
        self.colour = (0,0,255)


    def display(self, screen):
        '''
        Displays the food on the screen
        
        Args:
        screen (pygame.display): The screen to display the food on
        
        Returns:
        None
        '''
        pygame.draw.rect(screen, self.colour,pygame.Rect(self.position[0]-1, self.position[1]+1,4,4))