class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        #bucket sort alg:create n buckets,grouping numbers based on their frequencies from 1 to n. 
        #pick the top k numbers from the buckets, starting from n down to 1.

        counts = {}
        for x in nums:
            if x in counts:
                counts[x] += 1
            else:
                counts[x] = 1

        buckets = []
        for i in range(len(nums)+1):
            buckets.append([])

        for x in counts:
            freq = counts[x]
            buckets[freq].append(x)

        result = []
        for x in range(len(buckets)-1,-1,-1):
            for y in buckets[x]:
                result.append(y)
                if len(result) == k:
                    return result
