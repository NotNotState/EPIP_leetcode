#include <iostream>
#include <string>
#include <utility>
#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <map>

bool isValidSudoku(std::vector< std::vector<char> >& board) {
        int lim = 9;
        // board[row][col]
        // std::vector<int> nummies = {1, 2, 3, 4, 5, 6, 7, 8, 9};
        std :: unordered_map< int, std::unordered_set<char> > rows, cols;
        std :: map<std::pair<int, int>, std::unordered_set<char> > squares;

        for (int r = 0; r < lim ; r++){
            for (int c = 0; c < lim; c++){
                
                if (board[r][c] == '.'){continue;}
                
                std::pair<int,int> sqrKey = {r/3, c/3};

                if (
                    (rows[c].count(board[r][c])) ||
                    (cols[r].count(board[r][c])) ||
                    (squares[sqrKey].count(board[r][c]))
                ) {
                    return false;
                }

                rows[r].insert(board[r][c]);
                cols[c].insert(board[r][c]);
                squares[sqrKey].insert(board[r][c]);

            }
        }

        return true;
    }



int main() {
    int a = 4, b = 2;

    std::cout << (1 / b) << std::endl;


    return 0;
}