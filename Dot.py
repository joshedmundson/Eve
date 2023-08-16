import random 
from Genome import Genome
import numpy as np
from Brain import Brain
import pygame

class Dot():
    '''
    Class that allows for the creation of a dot - a simple digital creature 
    that can move around the screen based its location and any other information
    it receives from its senses.
    
    Attributes:
    position (np.array): The position of the dot on the screen
    speed (int): The speed of the dot
    colour (tuple): The colour of the dot
    genome (Genome): The genome of the dot (used to generate its brain)
    no_sensory_neurons (int): The number of sensory neurons in the dot's brain
    no_action_neurons (int): The number of action neurons in the dot's brain
    no_internal_neurons (int): The number of internal neurons in the dot's brain
    brain (Brain): The brain of the dot
    
    Methods:
    move: Moves the dot based on the output of its brain
    display: Displays the dot on the screen
    '''

    def __init__(self, no_sensory_neurons, no_action_neurons, 
                 no_internal_neurons, screen_width, screen_height):
        # Initiate positions 
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.position = np.array([random.randint(0, self.screen_width),
                                  random.randint(0, self.screen_height)])
        # Initiate speeds
        self.speed = 3
        # Initiate colour 
        self.colour = (random.randint(0, 255), 
                       random.randint(0, 255), 
                       random.randint(0, 255))
        # Create brain
        self.genome = Genome(4)
        self.no_sensory_neurons = no_sensory_neurons
        self.no_action_neurons = no_action_neurons
        self.no_internal_neurons = no_internal_neurons
        self.brain = Brain(self.genome, self.no_sensory_neurons, 
                           self.no_action_neurons, self.no_internal_neurons)

    def move(self):
        '''
        Moves the dot based on the output of its brain
        
        Returns:
        None
        '''
        direction = self.brain.think(self.position)
        new_x = self.position[0] + (self.speed * direction[0])
        new_y = self.position[1] + (self.speed * direction[1])
        
        if 0 <= new_x <= self.screen_width:
            self.position[0] = new_x
        
        if 0 <= new_y <= self.screen_height:
            self.position[1] = new_y

    def display(self, screen):
        '''
        Displays the dot on the screen
        
        Args:
        screen (pygame.display): The screen to display the dot on
        
        Returns:
        None
        '''
        pygame.draw.circle(screen, self.colour, 
                           (int(self.position[0]), 
                            int(self.position[1])), 1)