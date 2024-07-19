class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        length = len(nums)
        freqMap = dict()
        for num in nums:
            if num not in freqMap:
                freqMap[num] = 1
            else:
                freqMap[num] += 1

        # making a list of length n to store the keys at the frequencies
        ansFreq = [0] * (length+1) 
        for num, freq in freqMap.items():
            if ansFreq[freq] == 0:
                ansFreq[freq] =  [num]
            else:
                ansFreq[freq].append(num)
            
        # making an array of top k elements
        kMaxElements = []
        for i in range(length, -1, -1):
            if ansFreq[i] != 0:
                kMaxElements.extend(ansFreq[i])
            if k == len(kMaxElements):
                return kMaxElements

# beats 90.53% runtime and 39.36% memory
# https://leetcode.com/problems/top-k-frequent-elements/submissions/1242430062/
