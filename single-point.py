import random


genes = int(input("please enter the number of genes : "))


def n_points(parent1, parent2):
    n = 1
    if len(parent1) == len(parent2):
        genes = len(parent1)
        selected_point = random.sample(range(1, genes), n)
        print("the selected point are :", selected_point, "\n")
        child1 = [0 for i in range(genes)]
        child2 = [0 for j in range(genes)]
        child1[:selected_point[0]] = parent1[:selected_point[0]]
        child2[:selected_point[0]] = parent2[:selected_point[0]]
        x = 0
        while x < len(selected_point)-1:
            child1[selected_point[x]:selected_point[x+1]] = parent2[selected_point[x]:selected_point[x+1]]
            x += 2
        x = 1
        while x < len(selected_point)-1:
            child1[selected_point[x]:selected_point[x + 1]] = parent1[selected_point[x]:selected_point[x + 1]]
            x += 2
        x = 0
        while x < len(selected_point)-1:
            child2[selected_point[x]:selected_point[x + 1]] = parent2[selected_point[x]:selected_point[x + 1]]
            x += 2
        x = 1
        while x < len(selected_point)-1:
            child2[selected_point[x]:selected_point[x + 1]] = parent1[selected_point[x]:selected_point[x + 1]]
            x += 2
        if len(selected_point) % 2 == 0 :
            child1[selected_point[len(selected_point)-1]:] = parent1[selected_point[len(selected_point)-1]:]
            child2[selected_point[len(selected_point)-1]:] = parent2[selected_point[len(selected_point)-1]:]
        else:
            child1[selected_point[len(selected_point)-1]:] = parent2[selected_point[len(selected_point)-1]:]
            child2[selected_point[len(selected_point)-1]:] = parent1[selected_point[len(selected_point)-1]:]

        print("parent1 :", parent1)
        print("parent2 :", parent2, "\n\n")
        print("the selected points are :", selected_point, "\n\n")
        print("child1: ", child1)
        print("child2: ", child2)
        return child1, child2
    else:
        print("genes aren't equal")


#n_points(random.sample(range(0, genes), genes), random.sample(range(0, genes), genes))
