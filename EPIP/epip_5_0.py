def parity_partition(nummies: list[int]) -> list[int]:
    even_index, odd_index = 0, len(nummies)-1

    while even_index < odd_index:

        if nummies[even_index] % 2 == 0:
            even_index += 1
        else:
            nummies[even_index], nummies[odd_index] = nummies[odd_index], nummies[even_index]
        
        odd_index -= 1
    
    return nummies

if __name__ == "__main__":
    test = [1, 2, 4, 3]

    print(parity_partition(test))