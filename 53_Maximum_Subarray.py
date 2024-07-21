class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = float('-inf')
        curSum = 0
        for num in nums:
            curSum += num
            if curSum > maxSum:
                maxSum = curSum
            if curSum < 0:
                curSum = 0
    
        return maxSum

# beats 91.59% runtime and 52.44% memory
# https://leetcode.com/problems/maximum-subarray/submissions/1242452271/
