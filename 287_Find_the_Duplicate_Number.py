class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]
        # traverse like a linked list
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        # move by one step ahead only for both the pointers
        slow = nums[0]
        while slow!= fast:
            slow = nums[slow]
            fast = nums[fast]
        
        return fast

# beats 85.15% runtime and 98.39% memory
# https://leetcode.com/problems/find-the-duplicate-number/submissions/1266555787/
