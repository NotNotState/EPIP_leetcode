#include <iostream>
#include <string>
#include <vector>
#include <unordered_map>
#include <unordered_set>

bool hasDuplicated(std::vector<int>& nums){
    std :: unordered_map<int, int> hashMap;

    for (const auto& num : nums) {

        if (hashMap.count(num) == 0){
            hashMap[num] = 0;
        } else {
            return true;
        }

    }


    return false;
}

bool hasDuplicateV2(std::vector<int>& nums){
    return (
            std :: unordered_set<int>(nums.begin(), nums.end()).size() < nums.size()
        );
}

int main() {

    //std::cout << "Helloooooooow" << std::endl;

    std::vector<int> nummies = {1, 2, 3, 3};

    std::cout << hasDuplicated(nummies) << std::endl;
    std::cout << hasDuplicateV2(nummies) << std::endl;

    return 0;
}