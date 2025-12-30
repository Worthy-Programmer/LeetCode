#include <vector>
using namespace std;

// Sol1 O(n^2)
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        for (auto i = 0; i < nums.size(); i++) {
            auto n1 = nums[i];
            
            int j = -1;

            for (auto k = i + 1; k < nums.size(); k++) {
                if (nums[k] + n1 == target) {
                    j = k;
                    break;
                }
            }

            if (j!=-1) {
                vector<int> v = {i,j};
                return v ;
            }
        }

        return (vector<int>(2));
    }
}