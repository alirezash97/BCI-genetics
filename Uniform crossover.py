import numpy as np


def uniform_c(parent1, parent2):

    child1 = parent1.copy()
    child2 = parent2.copy()
    if len(parent1) == len(parent2):
        genes = len(parent1)
        mask = np.random.choice([0, 1], size=(genes,))
        for i in range(0, genes):
            if mask[i] == 1:
                child1[i] = parent2[i]
                child2[i] = parent1[i]
            else:
                pass
        print("mask : ", mask)
        return child1, child2


#print(uniform_c([0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1], [1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0]))
