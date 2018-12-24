import random
genes = int(input("please enter the number of genes : "))


def pmx(parent1, parent2):
    
    # if the number of genes are equal for both of parents
    if len(parent1) == len(parent2):
        genes = len(parent1)
        
        # choose two random points for partitioning parents
        points_2 = sorted(random.sample(range(1, genes), 2))
        print("the selected points are :", points_2, "\n")
        
        # initialization 
        child1 = [0 for i in range(genes)]
        child2 = [0 for j in range(genes)]
        
        # copy the alleles between two points from Parents to the Childs
        child1[points_2[0]:points_2[1]] = parent1[points_2[0]:points_2[1]]
        child2[points_2[0]:points_2[1]] = parent2[points_2[0]:points_2[1]]
        
        #right side of parent2
        m = 0
        for k in range(0, genes - points_2[1]):
            if parent2[points_2[1] + k] in child1[points_2[0]:points_2[1]]:
                pass
            else:
                child1[points_2[1] + m] = parent2[points_2[1] + k]
                m += 1
            if points_2[1] + m == genes:
                m = m - genes
        
        #left side of parent2
        for k in range(0, points_2[1]):
            if parent2[k] in child1[points_2[0]: points_2[1]]:
                pass
            elif points_2[1] + m != genes:
                child1[points_2[1] + m] = parent2[k]
                m += 1
            if points_2[1] + m == genes:
                m = m - genes

        #right side of parent1
        n = 0
        for k in range(0, genes - points_2[1]):
            if parent1[points_2[1] + k] in child2[points_2[0]: points_2[1]]:
                pass
            else:
                child2[points_2[1] + n] = parent1[points_2[1] + k]
                n += 1
            if points_2[1] + n == genes:
                n = n - genes
        
        #left side of parent1
        for k in range(0, points_2[1]):
            if parent1[k] in child2[points_2[0]: points_2[1]]:
                pass
            elif points_2[1] + n != genes:
                child2[points_2[1] + n] = parent1[k]
                n += 1
            if points_2[1] + n == genes:
                n = n - genes
        print("parent1 :", parent1)
        print("parent2 :", parent2, "\n\n")
        print("the selected points are :", points_2, "\n\n")
        print("child1: ", child1)
        print("child2: ", child2)
        return child1, child2
    else:
        print("genes aren't equal")


#pmx(random.sample(range(0, genes), genes), random.sample(range(0, genes), genes))
