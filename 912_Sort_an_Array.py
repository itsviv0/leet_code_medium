# approach 1
import heapq

def heapSort(nums):
    h = []
    for num in nums:
        heapq.heappush(h, num)
    return [heapq.heappop(h) for _ in range(len(h))]

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        sortedArr = heapSort(nums)
        return sortedArr

# beats 84.84% runtime and 36.95% memory
# https://leetcode.com/problems/sort-an-array/submissions/1333022776/?envType=daily-question&envId=2024-07-25

# approach 2
