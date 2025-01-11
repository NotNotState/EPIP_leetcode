import random as rand
import math
"""
Given two crystal balls that will break if dropped from a high enought distance. Determine the 
exact spote in which they will break in the most optimized way
"""

def find_crystal_ball(floors : [bool]) -> int:
    incr = int(math.floor(math.sqrt(len(floors)))) #takes int(floor())

    i = incr

    while i < len(floors):
        
        if floors[i]:
            break

        i+=incr
    
    i -= incr
    j = 0

    while i < len(floors) and j <= incr:

        if floors[i]:
            return i-1 if not floors[0] else i

        i+=1
        j+=1

    return -1


if __name__ == "__main__":
    test = ([0] * rand.randint(0,10)) + ([1] * rand.randint(0,10))
    #test = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    print(test)
    print(find_crystal_ball(test))
