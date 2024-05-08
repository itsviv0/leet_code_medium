class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int i, product = 1, flag = 1, count = 0;
        vector<int> ans;
        for(i=0; i<nums.size(); i++)
        {
            if(nums[i] != 0)
                product *= nums[i];
            else
                count ++;
        }
        if(count>1)
            product = 0;
        for(i=0; i<nums.size(); i++)
        {
            if(!count)
            {
                if(nums[i] != 0)
                    ans.push_back(product/nums[i]);
                else
                    ans.push_back(product);
            }
            else
            {
                if(nums[i] == 0 && count != nums.size())
                    ans.push_back(product);
                else
                    ans.push_back(0);
            }
        }
        return ans;
    }
};

// beats 15.62% runtime and 10.70% memory
// https://leetcode.com/problems/product-of-array-except-self/submissions/1222105766/
