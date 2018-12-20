import random
# n is the number of random selection for tournament
# m is the number of winner(s)


def tournament(population, n):
    my_tournament = {}
    selected = random.sample(range(1, len(population)+1), n)
    for i in range(0, n):
        my_tournament[selected[i]] = population[selected[i]]

#    print(my_tournament)
    return (max(my_tournament, key=lambda k: my_tournament[k]))


print(tournament({1: [12, [1,0,0,1,0,1,0]], 2: [7, [1,1,1,0,1,0,1]],3: [4, [1,0,0,0,0,1,0]], 4: [3, [0,1,1,0,1,0,1]]},2))