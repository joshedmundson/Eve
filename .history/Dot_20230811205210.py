import random 

class Dot():

    def __init__(self, screen):
        self.genome = Genome()
        self.x = screen.get_window_size()[0]