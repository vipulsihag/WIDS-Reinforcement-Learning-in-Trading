import numpy as np
import matplotlib.pyplot as plt
from bandits import bandits
from epsilon_greedy import run_epsilon_greedy

def bestBandit(expectedValues):
    maxVal = max(expectedValues)
    bestBandits = []
    for i in range(len(expectedValues)):
        if expectedValues[i] == maxVal:
            bestBandits.append(i)
    return bestBandits[np.random.randint(0, len(bestBandits))]

def run_optimistic_greedy(bandits, noOfIterations,q1):
    noOfBandits = len(bandits)
    reward = [0] * noOfIterations
    expectedValue = [q1] * noOfBandits
    noOfTimesPulled = [0] * noOfBandits

    for i in range(noOfIterations):
        toPull = bestBandit(expectedValue)
        r = bandits[toPull].pullLever()
        reward[i] = r

        noOfTimesPulled[toPull] += 1
        expectedValue[toPull] += (r - expectedValue[toPull])*0.5

    return reward

# Plotting the cumulative average of rewards as the number of iterations increases for an optimistic greedy of Q_1 = 10 and a non-optimistic epsilon = 0.1

noOfRuns = 20
noOfIter = 1000
q1 = 10

all_rewards = np.zeros((noOfRuns, noOfIter))

for run in range(noOfRuns):
    all_rewards[run] = run_optimistic_greedy(bandits, noOfIter,q1)

cumulativeRewardAvg = np.cumsum(all_rewards, axis=1) / (np.arange(noOfIter) + 1)
avgCumulativeRewardAvg = cumulativeRewardAvg.mean(axis=0)

for run in range(noOfRuns):
    all_rewards[run] = run_epsilon_greedy(bandits, noOfIter,0.1)

cumulativeRewardAvgEps = np.cumsum(all_rewards, axis=1) / (np.arange(noOfIter) + 1)
avgCumulativeRewardAvgEps = cumulativeRewardAvgEps.mean(axis=0)

plt.plot(avgCumulativeRewardAvg,label= "Optimistic, Q = 10")
plt.plot(avgCumulativeRewardAvgEps,label= "Non-optimistic epsilon, e = 0.1")
plt.legend()
plt.show()