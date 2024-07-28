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
def heapify(nums, n ,i):
    largest = i
    left = 2*i + 1
    right = 2*i + 2
    if left<n and nums[i] < nums[left]:
        largest = left
    if right<n and nums[largest] < nums[right]:
        largest = right
    if largest != i:
        nums[i], nums[largest] = nums[largest], nums[i]
        heapify(nums, n, largest)

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n//2-1, -1, -1):
            heapify(nums, n, i)

        for i in range(n-1, 0, -1):
            nums[i], nums[0] = nums[0], nums[i]
            heapify(nums, i, 0)

        return nums

# beats 13.29% memory and 98.06% memory
# https://leetcode.com/problems/sort-an-array/submissions/1333011741/
