import random
import numpy as np 

class Brain:
    '''
    Class that allows for the creation of a brain - a neural network that
    allows for the processing of information and the generation of actions.
    
    Attributes:
    genome (Genome): The genome that the brain is created from
    no_sensory_neurons (int): The number of sensory neurons in the brain
    no_action_neurons (int): The number of action neurons in the brain
    no_internal_neurons (int): The number of internal neurons in the brain
    no_cortex_rows (int): The number of rows in the cortex matrix
    no_cortex_cols (int): The number of columns in the cortex matrix
    cortex (np.array): The matrix that represents the brain
    
    Methods:
    initialise_neural_connections: Initialises the neural connections in the
    brain
    decode_gene: Decodes a gene into an input neuron, output neuron and weight
    connect_neurons: Connects two neurons with a weight
    think: Processes sensory information and generates an action
    '''
    def __init__(self, genome, no_sensory_neurons,
                 no_action_neurons, no_internal_neurons=2):
        # Initialize the brain
        self.genome = genome 
        self.no_sensory_neurons = no_sensory_neurons
        self.no_action_neurons = no_action_neurons
        self.no_internal_neurons = no_internal_neurons
        # Create the cortex
        self.no_cortex_rows = self.no_action_neurons + self.no_internal_neurons
        self.no_cortex_cols = self.no_sensory_neurons + self.no_internal_neurons
        self.cortex = np.zeros((self.no_cortex_rows, self.no_cortex_cols))
        # Initialise the neural connections
        self.initialise_neural_connections()
        
    def initialise_neural_connections(self):
        '''
        Initialises the neural connections in the brain
        
        Returns:
        None
        '''
        # Iterate through the genome
        for gene in self.genome.genome:
            # Decode the gene
            input_neuron, output_neuron, weight = self.decode_gene(gene)
            # Connect the neurons
            self.connect_neurons(input_neuron, output_neuron, weight)

    def decode_gene(self, gene):
        '''
        Decodes a gene into an input neuron, output neuron and weight
        
        Args:
        gene (str): The gene to be decoded
        
        Returns:
        input_neuron (int): The input neuron
        '''
        input_neuron = int(gene[:2], 16)
        output_neuron = int(gene[2:4], 16)
        sign = -1 if int(gene[4], 16) <= 7 else 1
        weight = sign * int(gene[5:], 16) / (int('fff', 16)/4)
        
        return input_neuron, output_neuron, weight   
    
    def connect_neurons(self, input_neuron, output_neuron, weight):
        '''
        Connects two neurons with a weight by adding an entry to the 
        cortex matrix in the appropriate location
        
        Args:
        input_neuron (int): The input neuron
        output_neuron (int): The output neuron
        weight (float): The weight of the connection
        
        Returns:
        None
        '''
        row_index = output_neuron % self.no_cortex_rows
        column_index = input_neuron % self.no_cortex_cols
        self.cortex[row_index, column_index] = weight
        
    def think(self, sensory_input):
        '''
        Processes sensory information and generates a response
        
        Args:
        sensory_input (np.array): The sensory input to the brain
        
        Returns:
        outputs (np.array): The output of the brain
        '''
        # Step 1: update internal neurons using sensory neurons
        m_1 = self.cortex[self.no_action_neurons : , 
                          : self.no_sensory_neurons]
        #print('M-1',m_1,sensory_input)

        internal_neurons = np.dot(m_1, sensory_input)
        #print('sensory input', sensory_input, 'internal neurons', internal_neurons)
        # Step 2: Update interal neurons using other internal neurons
        m_2 = self.cortex[self.no_action_neurons : , 
                          self.no_sensory_neurons : ]
        internal_neurons += np.dot(m_2, internal_neurons)
        #print('M-2',m_2)
        #print('sensory input', sensory_input, 'internal neurons', internal_neurons)

        # Step 3: Update action neurons using all sensory neurons and internal neurons
        m_3 = self.cortex[: self.no_sensory_neurons, 
                          : ]
        
        outputs = np.dot(m_3, np.concatenate((sensory_input, internal_neurons)))
        #print('M-3',m_3)
        #print('sensory input', sensory_input, 'output', outputs)
        #print(np.tanh(outputs))
        # Step 4: Apply tanh as an activation function to the outputs
        return np.tanh(outputs) 
        
    