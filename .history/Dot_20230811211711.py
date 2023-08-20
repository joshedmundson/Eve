import random 
import Genome

class Dot():

    def __init__(self, screen):
        self.genome = Genome(4)
        self.x = random.randint(0, screen.get_window_size()[0])
        self.y = random.randint(0, screen.get_window_size()[1])
        self.speed = 1

    def create_brain(self):
        pass 

    def decode_genome(self):
        pass 

    print (0x4)