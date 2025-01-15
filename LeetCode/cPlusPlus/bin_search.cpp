#include <iostream>
#include <iterator>
#include <ostream>
#include <string>
#include <vector>
#include <cmath>

int bin_search(std::vector<int>& nums, int target) {
    int lo = 0, hi = nums.size()-1, mid = 0;

    while (lo <= hi) {
        mid = floor( lo + (hi - lo) / 2 );

        std::cout << mid << std::endl;

        if (nums[mid] == target){
            return mid;
        }

        if (nums[mid] < target){
            lo = mid + 1;
        } else {
            hi = mid - 1;
        }

    }

    return -1;
}

int main() {
    std::vector<int> test = {-1,0,3,5,9,12};
    std::cout << bin_search(test, 9) << std::endl;
    return 0;
}