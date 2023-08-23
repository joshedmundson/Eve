import random
from tkinter import SE 
from Genome import Genome
import numpy as np
from Brain import Brain
from Food import Food
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
                 no_internal_neurons, screen_width, screen_height, genome = None):
        # Initiate positions 
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.position = np.array([random.randint(0, self.screen_width),
                                  random.randint(0, self.screen_height)])
        # Initiate speeds
        self.speed = 3
 
        # Initiate hunger
        self.hunger = 10
        
        # Create brain
        if genome == None:
            self.genome = Genome(10)
        else:
            self.genome = genome
        #print(self.genome.get_genome())
        self.no_sensory_neurons = no_sensory_neurons
        self.no_action_neurons = no_action_neurons
        self.no_internal_neurons = no_internal_neurons
        self.brain = Brain(self.genome, self.no_sensory_neurons, 
                           self.no_action_neurons, self.no_internal_neurons)
        
        #rand = np.random.randint(0,len(self.genome.genome))
        self.colour = '#'+str(self.genome.genome[0][:6])
        self.alive = True

    def move(self,direct=None):
        '''
        Moves the dot based on the output of its brain
        
        Returns:
        None
        '''
        if (direct==None):
            direct = self.position
        direction = self.brain.think(direct)
        new_x = self.position[0] + (self.speed * direction[0])
        new_y = self.position[1] + (self.speed * direction[1])
        
        if 0 <= new_x <= self.screen_width:
            self.position[0] = new_x
        
        if 0 <= new_y <= self.screen_height:
            self.position[1] = new_y
    def hungry(self,time,hungrytime = 5):
        '''
        Regulates hunger levels depending on time last eating
        hungry time is the number of ticks before we decrease hunger levels
        Time is the current number of ticks
        
        '''
        #if ((time%hungrytime>0)&(time%hungrytime<50)):
        if (time%hungrytime==0):
            self.hunger=self.hunger-1

            
    def feed(self,food):
        '''
        
        Dot searches for food based on output of brain and food location
        Also increases hunger bar when dot consumes food
        
        '''
        foods = []
        for i in range(len(food)):
            foods.append(food[i].position)
            
        foodloc = np.asarray(foods)
        dist = np.sum((foodloc - self.position)**2,axis=1)
        find = np.argmin(dist)
        food_ = foodloc[find]
        dotpos = self.position
        dire = list(dotpos)
        (dire).extend(food_)
        
        # Sending sensory input to brain based on dot and food location
        self.move(direct=dire)
        
        xfood = list(np.arange(food_[0]-3,food_[0]+3,1))
        yfood = list(np.arange(food_[1]-3,food_[1]+3,1))
        xpos = self.position[0]
        ypos = self.position[1]
        
        if((xpos in xfood) & (ypos in yfood)):
            self.hunger=self.hunger+3
            del food[find]

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
                            int(self.position[1])), 5*(self.hunger/5))