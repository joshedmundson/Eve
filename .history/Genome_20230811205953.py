import random

class Genome:
    
    def __init__(self, no_genes):
        self.genome = [] 

    def generate_gene(self):
        gene = ''.join(random.choice('0123456789ABCDEF') for _ in range(8))