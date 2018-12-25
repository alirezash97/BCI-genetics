import numpy as np


def sus(rates, individuals):
    sum_ = 0
    j = 0
    new_individuals = np.zeros((len(individuals), ), dtype=int)
    ptr = np.random.uniform(0, 1)
    for i in range(0, len(individuals)):
        sum_ = sum_ + rates[i]
        while sum_ > ptr:
            if not(0 in new_individuals):
                break
            else:
                new_individuals[j] = individuals[i]
                j += 1
                ptr += 1
    return new_individuals


#print(sus([2, 3, 7, 6, 1, 5, 4], [1, 2, 3, 4, 5, 6, 7]))
