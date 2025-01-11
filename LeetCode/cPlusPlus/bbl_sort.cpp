#include <iostream>

void bbl_sort(int *arry, int size){

    int i = 0, j = size-1;

    while (i <= j) {
        if (i == j){
            i = 0;
            j--;
        }

        if (arry[i] > arry[i+1]) {
            int temp = arry[i];
            arry[i] = arry[i+1];
            arry[i+1] = temp;
        }   

        i++;
    }

}

void bbl_sort_v2(int *arry, int size){
    //samething as above but with for loops
    for (int i = 0; i<size; ++i){
        for(int j = 0; j < size - 1 - i; ++j){//we decrement the limit by i (or 1) each time, the outer loop is there solely for this poirpose
            if (arry[j] > arry[j+1]){
                int temp = arry[j];
                arry[j] = arry[j+1];
                arry[j+1] = temp;
            }
        }
    }

}

int main(){
    
    int test[10] = {100,-99,44,8,7,101,48,37,57,88};
    int length = sizeof(test) / sizeof(test[0]);

    //bbl_sort(test, length);
    bbl_sort_v2(test, length);

    for (const auto& num : test){
        std::cout << num << " ";
    }

    return 0;
}