import numpy as np


def uniform(child):

    genes = len(child)
    #random binary mask
    mask = np.random.choice([0, 1], size=(genes,))
    for i in range(0,genes):
        if mask[i] == 1 :
            child[i] = int(not(child[i]))
        else:
            pass
    print("mask : ",mask)
    return child

print(uniform([1,0,1,1,1,0,0,1,1,1,1,1,0]))
