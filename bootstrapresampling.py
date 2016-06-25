"""
    Bootstrap Resampling

    Idea:
        Simulate the distribution by drawing samples with replacement.

    Motivation:
        The data estimates its own distribution - we draw random samples from this distribution.

    Notes:
        * Bootstrap Resampling is well-studied and rests on solid theoretical grounds.
        * Bootstrapping often doesn't work well for rank-based statistics (e.g. maximum value)
        * Works poorly with very few samples (N > 20 is a good rule of thumb)
        * As always, be careful about selection biases & non-independent data!
"""
from numpy.random import randint
from numpy import mean, std
import numpy as np

observations = np.array([48,24,51,12,
                        21,41,25,23,
                        32,61,19,24,
                        29,21,23,13,
                        32,18,42,18])
xbar = np.zeros(100000)
for i in range(100000):
    sample = observations[randint(20, size=20)]
    xbar[i] = mean(sample)
print("Height = {h} +- {sd} turtles".format(h=mean(xbar), sd=std(xbar))) #recovers the analytic estimate!
