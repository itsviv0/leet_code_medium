class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int curSum = 0;
        int maxSum = INT_MIN;
        int n = nums.size();
        for (int i=0; i<n; i++) {
            curSum += nums[i];
            if (curSum>maxSum)
                maxSum = curSum;
            if (curSum<0)
                curSum = 0; 
        }
        return maxSum;
    }
};

// beats 68.21% runtime and 20.01% memory
// https://leetcode.com/problems/maximum-subarray/submissions/1242449804/
