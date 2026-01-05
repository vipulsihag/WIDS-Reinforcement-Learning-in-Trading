import numpy as np
import matplotlib.pyplot as plt
from bandits import bandits

def run_greedy(bandits, noOfIterations):
    noOfBandits = len(bandits)
    reward = [0.0] * noOfIterations
    expectedValue = [0] * noOfBandits
    noOfTimesPulled = [0] * noOfBandits

    for i in range(noOfIterations):
        toPull = bestBandit(expectedValue)
        r = bandits[toPull].pullLever()
        reward[i] = r

        noOfTimesPulled[toPull] += 1
        expectedValue[toPull] += (r - expectedValue[toPull]) / noOfTimesPulled[toPull]

    return reward

def bestBandit(expectedValues):
    maxVal = max(expectedValues)
    bestBandits = []
    for i in range(len(expectedValues)):
        if expectedValues[i] == maxVal:
            bestBandits.append(i)
    return bestBandits[np.random.randint(0, len(bestBandits))]

# plotting rewards at i-th iteration, averaged over 100 runs.
noOfRuns = 100
noOfIter = 1000

all_rewards = np.zeros((noOfRuns, noOfIter))

for run in range(noOfRuns):
    all_rewards[run] = run_greedy(bandits, noOfIter)

cumulativeRewardAvg = np.cumsum(all_rewards, axis=1) / (np.arange(noOfIter) + 1)
avgCumulativeRewardAvg = cumulativeRewardAvg.mean(axis=0)

plt.plot(avgCumulativeRewardAvg)
plt.show()