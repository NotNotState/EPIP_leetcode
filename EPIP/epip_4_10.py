from random import randint

def uniform_random(lower_bound: int, upper_bound: int)-> int:
    num_outcomes = upper_bound - lower_bound + 1 # garuntee number generated on 0 <= (b-a) <= 2^{i+1}-1

    while True:
        result, i = 0, 0 # reset result and counter on each failed attempt

        while (1 << i) < num_outcomes:

            result = (result << 1) | randint(0,1) # left shift 1 and append 0 or 1 (randome gen) to the result i times
            i += 1
        
        if result < num_outcomes: # Check result lies on 0 to (b-a)
            break
    
    return result + lower_bound # return a + result to scale back to [a, b] interval from [a-a, b-a] = [0, b-a]

if __name__ == "__main__":

    res = []
    for k in range(1000):
        res.append(uniform_random(1,6))

    # test theoretical EV of 3.5
    print(sum(res) / len(res))