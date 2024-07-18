class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_jumps = 0
        for n in nums:
            if max_jumps < 0:
                return False
            elif max_jumps < n:
                max_jumps = n
            max_jumps -= 1

        return True

# beats 57.90% runtime and 54.65% memory
# https://leetcode.com/problems/jump-game/submissions/1240031314/
