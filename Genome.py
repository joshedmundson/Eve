import random

class Genome:
    '''
    Class that allows for the creation of a 'genome' - a unique set of 
    hexadecimal numbers that can be used to create a brain.
    
    Attributes:
    no_genes (int): The number of genes in the genome
    genome (list): A list of hexadecimal numbers that make up the genome
    
    Methods:
    generate_gene: Generates a random hexadecimal number
    get_genome: Returns the genome
    mutate: Mutates the genome by changing a random character in a random gene
    '''
    
    def __init__(self, no_genes):
        # Initialize the genome
        self.no_genes = no_genes
        self.genome = [self.generate_gene() for _ in range(self.no_genes)] 

    def generate_gene(self):
        '''
        Generates a random hexadecimal number
        
        Returns:
        gene (str): A random hexadecimal number
        '''
        # Generate a random hexadecimal number
        gene = ''.join(random.choice('0123456789ABCDEF') for _ in range(8))
        
        return gene
   
    def get_genome(self):
        '''
        Returns the genome
        
        Returns:
        genome (list): The genome
        '''
        return self.genome
    
    def mutate(self, prob_mutation):
        '''
        Mutates the genome by changing a random character in a random gene
        
        Args:
        prob_mutation (float): The probability of a mutation occuring
        
        Returns:
        None
        '''
        # Mutate the genome
        for index in range(self.no_genes):
            # Randomly mutate a character in a random gene
            if random.randint(1, 1/prob_mutation) == 1:
                char_index = random.randint(0,7)
                new_char = random.choice('0123456789ABCDEF')
                gene = list(self.genome[index])
                gene[char_index] = new_char 
                self.genome[index] = "".join(gene)