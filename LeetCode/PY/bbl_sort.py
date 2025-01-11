import random as rand

def bbl_sort(arry : list[int]): # random reminder, lists are mutable, so in python any passed mutable object is pass by reference

    i,j = 0, len(arry)-1

    while ( not (i > j) ): # better way to do this? 

        if i == j:
            i = 0
            j -= 1

        if arry[i] > arry[i+1]:
            arry[i], arry[i+1] = arry[i+1], arry[i]

        i+=1


if __name__ == "__main__":
    test = [rand.randint(-100,100) for i in range(rand.randint(0,100))]

    bbl_sort(test)

    print(test)