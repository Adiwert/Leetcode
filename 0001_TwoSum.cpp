#include <unordered_map>
#include <vector>

using namespace std;

class Solution {
public:
// vector<int>& nums: This is a reference to a vector of integers that contains the list of numbers.
// int target: This is the integer value that the sum of two numbers from nums should equal.
// unordered_map<int, int> numMap: This is a hash map (or dictionary) that maps a number (int) to its index (int) in the nums array.
    vector<int> twoSum(vector<int>& nums, int target) {         // Create an unordered_map to store previously seen numbers and their indices
        unordered_map<int, int> numMap;

        for(int i = 0; i < nums.size(); i++) {                  // Iterate through the input array

            int complement = target - nums[i];                  // Calculate the complement (target - current number)
            if (numMap.find(complement) != numMap.end()) {      // Check if the complement exists in the map
                return {numMap[complement], i};                 // Add the current number and its index to the map
            }
            numMap[nums[i]] = i;
        }

        // No solution found, return an empty vector
        return {};
    }
};