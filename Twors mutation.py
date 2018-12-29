import random
def twors(child):
    rand = random.sample(range(0,int(len(child)-1/2)),2)
    child[rand[0]], child[rand[1]] = child[rand[1]], child[rand[0]]
    return child
#print("child : ",[1,2,3,4,5,6,7,8,9,10,11,12,13])
#print("the mutated child is : ",twors([1,2,3,4,5,6,7,8,9,10,11,12,13]))
