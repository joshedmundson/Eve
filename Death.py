import random
import numpy as np 
from Genome import Genome 
from Brain import Brain 
from Dot import Dot

print("I am become death, destroyer of worlds.")

def kill_left(dots):
    if (dots!=list):
        oglen = len(dots)
        deaddots = []
        for i in range(oglen):
            #print(i,oglen)
            dotself = dots[i].__dict__
            xpos = dotself['position'][0]
            ypos = dotself['position'][1]
            width = dotself['screen_width']
            height = dotself['screen_height']
            
            half = width/2
            if (xpos<=half):
                deaddots.append(i)
                
        #survivors = [ele for ele in dots if ele not in unwanted_num]
        for ele in sorted(deaddots, reverse = True):
            del dots[ele]
        #for i in deaddots:
        #    dots.remove(dots[i]):
        #dots.remove(dots[i])
        
    return dots

def gene_pool(dots):
    if (dots!=list):
        oldpool = []
        newpool = []
        gene_evolution = {}
        ndots = len(dots)
        
        for i in range(ndots):
            dotself = dots[i].__dict__
            genomes_ = dotself['genome'].__dict__
            genomes = genomes_['genome']
            
            oldpool.extend(genomes)
    return oldpool


def create_life(dots,n,pool,mutprob = 10/10):
    if (dots!=list):
        ndots = n
        nsurvive = len(dots)
        ncreate = ndots - nsurvive
        newdots = []
        newpool = []
        
        dotself = dots[0].__dict__
        width = dotself['screen_width']
        height = dotself['screen_height']
        nsense = dotself['no_sensory_neurons']
        nact = dotself['no_action_neurons']
        nint = dotself['no_internal_neurons']
        #genome = dotself['genome'].__dict__['genome']
        
        # create genome object to store the genomes of all creatures
        # to be mutated simultaneously. Since the Genome class is the
        # only thing that can mutate, requiring a genome object, we 
        # have to turn the entire gene pool into a genome object, with
        # the number of genes equal to the number of survivors times
        # the number of genes within a creature
        
        genomelen = dotself['genome'].__dict__['no_genes']
        allgenomes = Genome(nsurvive*genomelen)
        
        allgenomes.genome = pool
        #print(allgenomes.genome[:10])
        allgenomes.mutate(mutprob)
        #print(allgenomes.genome[:10])
        #newdots = [Dot(nsense, nact, nint, width, height) for _ in range(ncreate)]
        newpool = allgenomes.genome
        
        for i in range(ncreate):
            geninds = np.random.randint(0,len(newpool),size=4)
            newgens = list(np.array(newpool)[geninds])
            newdot = Dot(nsense,nact,nint,width,height,genomes=newgens)
            
            newdots.append(newdot)
            """
            dotself = dots[i].__dict__
            genomes_ = dotself['genome'].__dict__
            genomes = genomes_['genome']

            # Test the genome generation works
            genome = Genome(4)
            genome.genome = new
            #print("Generating Genome: ")
            #print(genome.get_genome())

            print("Mutating Genome")
            genome.mutate(10/10)
            print(genome.get_genome())
            """
        dots.extend(newdots)
        

    return dots