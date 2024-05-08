class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lpro, rpro = 1, 1
        larr = [0] * len(nums)
        rarr = [0] * len(nums)
        for i in range(len(nums)):
            j = -i-1
            larr[i] = lpro
            rarr[j] = rpro
            lpro *= nums[i]
            rpro *= nums[j]

        for i in range(len(nums)):
            larr[i] = larr[i]*rarr[i]

        return larr

# beats 22.12% runtime and 32.76% memory
# https://leetcode.com/problems/product-of-array-except-self/submissions/1223043536/
