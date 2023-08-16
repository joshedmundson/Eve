from Genome import Genome 
from Brain import Brain 
import random
import numpy as np

# Test the genome generation works
genome = Genome(8)

print("Generating Genome: ")
print(genome.get_genome())

print("Mutating Genome")
genome.mutate(1/10)
print(genome.get_genome())

# Testing Brain functionality
print("Creating brain and printing matrix cortex")
brain = Brain(genome, 2, 2, no_internal_neurons=2)
print(brain.cortex)

# Test the brain's ability to process information 
sensory_inputs = np.array([1,7])
print(brain.think(sensory_inputs))
