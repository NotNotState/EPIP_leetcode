#include <iostream>
#include <cmath>

int crystal_balls(bool *arry, int size){

    int jump = (int) sqrt( (double) size );

    int i = jump;

    for ( ; i < size ; i++){
        if (arry[i]){break;}
    }

    i = i - jump;
    int j = 0;

    for (; i < size && j <= jump; ++j,++i){
        if (arry[i]){return i;}
    }

    return -1;
}


int main() {

    bool arry[10] = {0,0,0,1,1,1,1,1,1,1};
    int length = sizeof(arry) / sizeof(arry[0]);

    int res = crystal_balls(arry, length);

    std::cout << res << std::endl;

    return 0;
}