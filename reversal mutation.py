import random


def reverse(child):


    rand = random.sample(range(0, len(child)-1), 2)
    rand.sort()
    rev = child[rand[0]:rand[1]]
    child[rand[0]:rand[1]] = rev[::-1]
    return child

print(reverse([1, 2, 3, 4, 5, 6, 7, 8, 9]))