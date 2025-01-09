def increment_list(A: list[int]) -> None:
    A[-1] += 1 # add 1 to last element in list

    for i in reversed(range(1, len(A))):
        if A[i] != 10:
            break
        #only get here if A[i] == 10
        A[i] = 0
        A[i-1] += 1
    
    if A[0] == 10:
        A[0] = 1
        A.append(0)

if __name__ == "__main__":
    test = [9,9,9]
    increment_list(test)
    print(test)