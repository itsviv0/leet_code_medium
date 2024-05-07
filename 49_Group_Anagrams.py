class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        groupAngs = dict()

        for string in strs:
            countLetter = [0]*26
            for letter in string:
                countLetter[ord(letter) - ord('a')] += 1

            key = tuple(countLetter)
            if key not in groupAngs:
                groupAngs[key] = []
    
            groupAngs[key].append(string)

        return groupAngs.values()

# beats 44.06% runtime and 25.22% memory
# https://leetcode.com/problems/group-anagrams/submissions/1222079342/
