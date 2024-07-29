class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        change = False

        while left <= right:
            if s[left] != s[right]:
                if change:
                    return False
                change = True
                
                skipLeft = s[left+1:right+1]
                skipRight = s[left:right]
                return skipLeft == skipLeft[::-1] or skipRight == skipRight[::-1]

            left += 1
            right -= 1
    
        return True

# beats 92.56% runtime and 52.30% memory
# https://leetcode.com/problems/valid-palindrome-ii/submissions/1337194410/
