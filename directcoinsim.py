""" Direct simulation, P of coin toss having 22 or more heads in 30 flips """
from numpy.random import randint

M = 0
number_of_simulations = 100000
for i in range(number_of_simulations):
	trials = randint(2, size=30)
	if (trials.sum() >= 22):
		M += 1

p = M / number_of_simulations

print(p)
