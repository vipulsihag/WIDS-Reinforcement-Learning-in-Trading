#Takes some to time to run (~ 8s)

import numpy as np
import matplotlib.pyplot as plt
from bandits import bandits

def epsBandit(expectedValues,epsilon):
    if np.random.random() < epsilon:
        return np.random.randint(0,10)
    maxVal = max(expectedValues)
    bestBandits = []
    for i in range(len(expectedValues)):
        if expectedValues[i] == maxVal:
            bestBandits.append(i)
    return bestBandits[np.random.randint(0, len(bestBandits))]


def run_epsilon_greedy(bandits, noOfIterations, epsilon):
    noOfBandits = len(bandits)

    reward = [0.0] * noOfIterations
    expectedValue = [0.0] * noOfBandits
    noOfTimesPulled = [0] * noOfBandits

    epsBandit_local = epsBandit
    bandits_local = bandits

    for i in range(noOfIterations):
        toPull = epsBandit_local(expectedValue, epsilon)

        r = bandits_local[toPull].pullLever()
        reward[i] = r

        n = noOfTimesPulled[toPull] + 1
        noOfTimesPulled[toPull] = n
        expectedValue[toPull] += (r - expectedValue[toPull]) / n

    return reward

if __name__ == "__main__":
    #this __name__ stuff is done so that importing functions from this file to optimistic_greedy.py doesn't execute the following code.

    fig, axs = plt.subplots(1, 2, figsize=(12, 5))

#Plotting cumulative reward avg for varioous epislon values

    noOfRuns = 100
    noOfIter = 1000

    all_rewards = np.zeros((noOfRuns, noOfIter))
    for i in range(5):
        for run in range(noOfRuns):
            all_rewards[run] = run_epsilon_greedy(bandits, noOfIter,(i+1)/50)

        cumulativeRewardAvg = np.cumsum(all_rewards, axis=1) / (np.arange(noOfIter) + 1)
        avgCumulativeRewardAvgEps = cumulativeRewardAvg.mean(axis=0)
        axs[0].plot(avgCumulativeRewardAvgEps,label = f"e = {(i+1)/50}")

    axs[0].legend()
    axs[0].set_title("Cumulative Reward Avg")

#Finding Optimal Epsilon

    e = 0
    erew = np.zeros(200)
    for i in range(200):
        s = 0
        for _ in range(20):
            s+=sum(run_epsilon_greedy(bandits,1000,e))/1000
        erew[i] = s/20
        e+=0.005

    optimal = np.argmax(erew)/200
    print("Optimal epsilon is : ", optimal)

#Plotting Cumalative reward avg at the 1000-th step for values of epsilon for 0 to 1

    axs[1].plot([i/200 for i in range(200)],erew)
    axs[1].set_title("Cumalative Reward Avg at 1000-th step for various epsilon")

    plt.tight_layout
    plt.show()