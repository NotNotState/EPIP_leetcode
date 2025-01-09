def parity_partition(nummies: list[int]) -> None:
    """
    nummies: unsorted array of ints

    Works on python's pass-by-(OBJECT)-reference (not strictly pass-by-reference) on mutable objects
    Note: re-assignment doesn't modify the passed mutable object, only direct operations on its variable do
    """
    even_index, odd_index = 0, len(nummies)-1

    while even_index < odd_index:

        if nummies[even_index] % 2 == 0:
            even_index += 1
        else:
            nummies[even_index], nummies[odd_index] = nummies[odd_index], nummies[even_index]
            odd_index -= 1

if __name__ == "__main__":
    test = [3, 4, 9, 2, 6, 1]
    parity_partition(test)
    print(test)