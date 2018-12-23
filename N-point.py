import random

n = int(input("please enter the number of points : "))
genes = int(input("please enter the number of genes : "))


def n_points(parent1, parent2):
    if len(parent1) == len(parent2):
        genes = len(parent1)
        points_n = sorted(random.sample(range(1, genes), n))
        print("the selected points are :", points_n, "\n")
        child1 = [0 for i in range(genes)]
        child2 = [0 for j in range(genes)]
        child1[:points_n[0]] = parent1[:points_n[0]]
        child2[:points_n[0]] = parent2[:points_n[0]]
        x = 0
        while x < len(points_n)-1:
            child1[points_n[x]:points_n[x+1]] = parent2[points_n[x]:points_n[x+1]]
            x += 2
        x = 1
        while x < len(points_n)-1:
            child1[points_n[x]:points_n[x + 1]] = parent1[points_n[x]:points_n[x + 1]]
            x += 2
        x = 0
        while x < len(points_n)-1:
            child2[points_n[x]:points_n[x + 1]] = parent2[points_n[x]:points_n[x + 1]]
            x += 2
        x = 1
        while x < len(points_n)-1:
            child2[points_n[x]:points_n[x + 1]] = parent1[points_n[x]:points_n[x + 1]]
            x += 2
        if len(points_n) % 2 == 0 :
            child1[points_n[len(points_n)-1]:] = parent1[points_n[len(points_n)-1]:]
            child2[points_n[len(points_n)-1]:] = parent2[points_n[len(points_n)-1]:]
        else:
            child1[points_n[len(points_n)-1]:] = parent2[points_n[len(points_n)-1]:]
            child2[points_n[len(points_n)-1]:] = parent1[points_n[len(points_n)-1]:]

        print("parent1 :", parent1)
        print("parent2 :", parent2, "\n\n")
        print("the selected points are :", points_n, "\n\n")
        print("child1: ", child1)
        print("child2: ", child2)
        return child1, child2
    else:
        print("genes aren't equal")


n_points(random.sample(range(0, genes), genes), random.sample(range(0, genes), genes))
