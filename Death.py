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
                       
def create_life(dots,n):
    if (dots!=list):
        oglen = n
        newlen = len(dots)
        ncreate = n - len(dots)
        dotself = dots[0].__dict__
        width = dotself['screen_width']
        height = dotself['screen_height']
        nsense = dotself['no_sensory_neurons']
        nact = dotself['no_action_neurons']
        nint = dotself['no_internal_neurons']
            
        newdots = [Dot(nsense, nact, nint, width, height) for _ in range(ncreate)]
        dots.extend(newdots)
    return dots