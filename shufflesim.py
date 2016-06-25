""" The lecture did not provide an example implementation of shuffling for the fictitious 'Sneetches' example he spoke of.
    This is my attempt at working a solution based on his excellent explanation of Shuffling.

    Shuffling, is the difference statistically significant (not due to chance)?
    * Is the difference between the test results of star and non-star bellied 'Sneetches' significant?
    * Unlike the coin toss we don't have a generative model we can use
    * How do we make the test scores the simulation? Solution: Shuffling

    Idea: Simulate the distribution by shuffling the labels repeatedly and computing the desired statistic.

    Motivation: If the labels really don't matter, then switching them shouldn't change the results!

    1. Shuffle labels
    2. Rearrange
    3. Compute means

    A difference of 6.6 is not significant at p = 0.05

    Notes on Shuffling:
    * Works when the Null Hypothesis assumes two groups are equivalent
    * Like all methods, it will only work if your samples are representative - always be
      careful about selection biases!
    * Needs care for non-independent trials.  Good discussion in Simon's Resampling: The New Statistics
"""
from numpy.random import shuffle
import numpy as np
import pylab as pl
import scipy.stats as stats

star_belly_scores = [84, 72, 57, 46, 63, 76, 99, 91]

regular_belly_scores = [81, 69, 74, 61, 56, 87, 69, 65, 66, 44, 62, 69]

number_of_simulations = 10000

population = star_belly_scores + regular_belly_scores

modeled_score_diffs = []
for i in range(number_of_simulations):
    shuffle(population) #shuffles in-place
    mean_of_sample_stars = np.mean(population[0:8])
    mean_of_sample_regulars = np.mean(population[8:])

    modeled_score_diffs.append(mean_of_sample_stars - mean_of_sample_regulars)

#fit = stats.norm.pdf(modeled_score_diffs, np.mean(modeled_score_diffs), np.std(modeled_score_diffs))
#pl.plot(modeled_score_diffs, fit, '-o')
pl.hist(modeled_score_diffs, normed=True)
pl.show()

# N>6.6 / Ntot
samples_greater_than_original_diff = [x for x in modeled_score_diffs if x > 6.6]
percent_of_samples_greater_than_target = len(samples_greater_than_original_diff) / len(modeled_score_diffs)
print("N>6.6 / Ntot = ", percent_of_samples_greater_than_target)

if percent_of_samples_greater_than_target > 0.05:
    print("A difference of 6.6 is not significant at p = 0.05")
