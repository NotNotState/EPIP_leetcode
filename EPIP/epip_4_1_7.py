import collections

def valid_sudoku(board:list[list[int]]) -> bool:

    n = len(board[0])
    rows = collections.defaultdict(set) # any key, init with values of type SET
    cols = collections.defaultdict(set)
    cubes = collections.defaultdict(set) # key here = (row, col) tuples

    for row in range(n):
        for col in range(n):

            if board[row][col] == ".": #or 0
                continue

            if ( board[row][col] in rows[row] or
                 board[row][col] in cols[col] or
                 board[row][col] in cubes[(row // 3, col // 3)]):
                return False
            
            rows[row].add(board[row][col])
            cols[col].add(board[row][col])
            cubes[(row // 3, col // 3)].add(board[row][col])

    return True

if __name__ == "__main__":
    print(4 // 3)