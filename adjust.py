from freqs_and_rats import *
from chord_sequence_new import chord_sequence

import numpy.random as ran
from fractions import Fraction

ran.seed(0)

roots = []
ratios = []
durations = []

for n in range(10):
    x = 1+ran.random()
    a = Fraction(x).limit_denominator(64)
    b = Fraction(x).limit_denominator(32)
    print(a,b)
    roots += [440,440]
    ratios += [(1,a),(1,b)]
    durations += [2.,2.]

chord_sequence(roots,ratios,durations,'deserts')

