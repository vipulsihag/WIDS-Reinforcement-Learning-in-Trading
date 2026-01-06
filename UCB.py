import math
import numpy as np
import matplotlib.pyplot as plt
from bandits import bandits

def selectBandit(expectedVal, noOfTimesPulled,time,c):
    for i in range(10):
        if noOfTimesPulled[i] == 0:
            return i
    
    ucbList = [expectedVal[i] + c*math.sqrt(math.log(time)/noOfTimesPulled[i]) for i in range(10)]
    return max(range(10),key=lambda i : ucbList[i])

def run_ucb(bandits, c, noOfIter):
    expectedVal = [0 for _ in range(10)] 
    noOfTimesPulled = [0 for _ in range(10)]
    reward = []
    for time in range(noOfIter):
        toPull = selectBandit(expectedVal, noOfTimesPulled,time,c)
        result = bandits[toPull].pullLever()
        noOfTimesPulled[toPull] += 1
        expectedVal[toPull] += (result - expectedVal[toPull])/noOfTimesPulled[toPull]
        reward.append(result)
    return reward

#Plotting

noOfRuns = 100
noOfIter = 1000
cumAvgReward = [0 for _ in range(noOfIter)]
for c in [0.2,1,5]:
    for _ in range(noOfRuns):
        currReward = run_ucb(bandits,c,noOfIter)
        for i in range(noOfIter):
            cumAvgReward[i] += currReward[i]
            
    for i in range(noOfIter):
        cumAvgReward[i] /= noOfRuns
    cumAvgReward = np.cumsum(cumAvgReward) / [i+1 for i in range(noOfIter)]

    plt.plot(cumAvgReward,label= f"c = {c}")

plt.legend()
plt.show()

