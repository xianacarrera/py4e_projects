''' 
    Author: Xiana Carrera Alonso
    Date: 24/08/2020
    This is a program made for the 'Scientific Computing with Python' course of freeCodeCamp.
    This code corresponds to the fifth and last assigment, 'Probability Calculator'.
    The purpose of the code is to empirically approximate the probability of drawing a
    certain group of balls randomly from a hat, with no replacement.
    Complete instructions for this assigment can be found at
    https://repl.it/@freeCodeCamp/fcc-probability-calculator#README.md
'''

import copy
import random

class Hat:
    
    def __init__(self, **kwargs):    # Any number of ball types can be passed
        if sum(kwargs.values()) == 0:
            print("Error: Hats must have at least one ball")
            quit() 
        
        self.contents = []    
        for arg in kwargs:
            times = kwargs[arg]
            self.contents += times * [arg]   # Even repeated types are added to the list
    
    def draw(self, n):
        if n >= len(self.contents):
            return self.contents        # Returns the entire list
        
        removed = []
        for i in range(n):
            ind = random.randint(0, len(self.contents) - 1)
            removed.append(self.contents[ind])
            self.contents.pop(ind)      # No replacement
        
        return removed
        

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    
    wins = 0
    for i in range(num_experiments):
        fake_hat = copy.deepcopy(hat)   # A copy is needed in order not to modify hat, so that the experiment can be repeated
        dr_balls = fake_hat.draw(num_balls_drawn)
        
        flag = True
        for ball_type in expected_balls:
            for j in range(expected_balls[ball_type]):  # Number of desired balls from the type
                try:
                    dr_balls.remove(ball_type)
                except:         # There was no such ball in dr_balls
                    flag = False        # Failed experiment
                    break
            if not flag: break      # No need for continuing with the current experiment
            
        if flag: wins += 1      # All expected_balls were on dr_balls
    
    return wins / num_experiments    # Probability (number between 0 and 1)


hat = Hat(blue = 4, red = 2, green = 6)
probability = experiment(hat = hat,expected_balls = {"blue": 2, "red": 1},
    num_balls_drawn = 4, num_experiments = 3000)
print("Probability:", probability)
