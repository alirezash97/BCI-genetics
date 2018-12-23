import random


def inorder(child, pm, n):
    points = sorted(random.sample(range(0, len(child)), n))
    for i in range(0, n):
        if random.uniform(0,1) < pm :
            child[points[i]] = int(not(child[points[i]]))
        else:
            pass
    return child
