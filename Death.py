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
                       
    