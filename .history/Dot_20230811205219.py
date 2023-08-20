import random 

class Dot():

    def __init__(self, screen):
        self.genome = Genome()
        self.x = random.randint(screen.get_window_size()[0]