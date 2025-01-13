#include <iostream>
#include <ostream>
#include <vector>
#include <unordered_map>

std::vector<int> twoSum(std::vector<int>& nums, int target) {
        
        std::unordered_map<int, int> diffs;

        for (int i = 0; i < nums.size() ; i++){

            if ( diffs.find(target - nums[i]) != diffs.end() ){
                return {diffs[target - nums[i]], i};
            }

            //diffs[nums[i]] = i;
            diffs.insert({nums[i], i});
        }

        return {};
    }

int main(){

    std::vector<int> nummies = {3,4,5,7};
    int target = 7;
    std::vector<int> result= twoSum(nummies, target);

    std::cout << result[0] << " " << result[1] << std::endl;

    return 0;
}