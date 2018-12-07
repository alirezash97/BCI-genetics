import random


def pms(child,p):
    for i in range(0,len(child)):
        if random.uniform(0, 1) < p:
            rand = random.choice(range(0, i) or range(i+1, len(child)))
            print(rand)
            child[i], child[rand] = child[rand], child[i]
        else:
            pass
    return child
print(pms([1,2,3,4],0.9))