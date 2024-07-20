import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = []

        for num in nums:
            if len(minHeap) < k:
                heapq.heappush(minHeap, num)
            else:
                heapq.heappushpop(minHeap, num)
            
        return heapq.heappop(minHeap)

# beats 75.71% runtime and 52.63% memory
# using the priority queue or heap approach
# https://leetcode.com/problems/kth-largest-element-in-an-array/submissions/1325063562/
