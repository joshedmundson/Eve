from tkinter import SEL
from Dot import Dot
import random

class Population:
    
    def __init__(self, count, no_sensory_neurons, no_action_neurons, 
                 no_internal_neurons, screen_width, screen_height,
                 gene_pool = None, creatures = Dot,
                 mutprob = 1/1000):
        self.count = count
        self.no_sensory_neurons = no_sensory_neurons
        self.no_action_neurons = no_action_neurons
        self.no_interal_neurons = no_internal_neurons
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.creatures = creatures
        self.gene_pool = gene_pool
        self.mutprob = mutprob
        self.population = None
        self.populate()
        
    def populate(self):
        '''
        Populates the population with creatures
        
        Returns:
        None
        '''
        if (self.gene_pool!=None):
            self.population = [self.creatures(self.no_sensory_neurons, self.no_action_neurons,
                                             self.no_interal_neurons, self.screen_width,
                                             self.screen_height, genome=random.choice(self.gene_pool)) 
                              for _ in range(self.count)]
        else:
            self.population = [self.creatures(self.no_sensory_neurons, self.no_action_neurons,
                                             self.no_interal_neurons, self.screen_width,
                                             self.screen_height) 
                              for _ in range(self.count)]

    def cull(self, cull_condition_function):
        '''
        Culls the population based on a condition
        
        Args:
        cull_condition_function (function): A function that takes a creature and returns a boolean
        
        Returns:
        None
        '''
        self.population = [creature for creature in self.population if cull_condition_function(creature)]
        
    def reproduce(self):
        '''
        Reproduces the population using the gene pool the current population
        
        Returns:
        None
        '''
        self.gene_pool = [creature.genome for creature in self.population]
        for gene in self.gene_pool:
            gene.mutate(self.mutprob)
        self.populate()
        
    def next_generation(self, cull_condition_function):
        self.cull(cull_condition_function)
        self.reproduce()
        

