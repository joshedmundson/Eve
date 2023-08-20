import random 

class Dot():

    def __init__(self, screen):
        self.genome = Genome()
        self.x = random.randint(0, screen.get_window_size()[0])
        self.y = random.randint(0, screen.get_window_size()[1])
        self.speed = 1