This repo contains multiple files and each is explained in some detail below

## bandits.py 
- this only contains the bandit class that is necessary for other files to function properly

## greedy.py
- implements the greedy algorithm.
- And plots the cumulative reward average of 1000 iterations averaged over 100 runs

## epsilon_greedy.py
- implements the epsilon greedy algorithm
- And plots the cumulative reward average of 1000 iterations averaged over 100 runs for 5 values of epsilon.
- And plots the cumalative reward average at 1000-th step for epsilon between 0 and 1. (each averaged over 20 runs)
- And prints the optimal epsilon

## optimistic_greedy.py
- implements the optimistic greedy algorithm.
- And plots the cumulative average of rewards as the number of iterations increases for an optimistic greedy with Q_1 = 10 and a non-optimistic epsilon = 0.1 (both averaged over 20 runs)

## UCB.py
- implements the upper confidence bound algorithm
- And plots the cumulative reward average of 1000 iterations averaged over 100 runs for 3 values of c.

## MDP_environments.py
- prints the state space of slippery bandit walk
- prints the state space of frozen lake grid walk

## Final_Project (Reinforcement Learning Based Trading Agent)
- implements a Q-learning based trading agent on real stock market data
- uses historical closing prices downloaded via `yfinance`
- defines a custom trading environment with actions: Hold, Buy, Sell
- trains the agent using an epsilon-greedy policy with epsilon decay
- evaluates the trained agent on the same price series without exploration
- prints the final portfolio value after training
- compares performance against a Buy-and-Hold baseline strategy
