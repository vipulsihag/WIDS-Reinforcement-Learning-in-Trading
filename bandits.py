#This is a helper file.....

import numpy as np
import random

class Bandit:
    def __init__(self, mean=0, stddev=1):
        self.__mean = mean
        self.__stddev = stddev

    '''This method simulates pulling the lever of the bandit and returns the reward'''
    def pullLever(self):
        return np.random.normal(self.__mean, self.__stddev)
    
bandits = [Bandit(random.random()*4-2) for _ in range(10)]

