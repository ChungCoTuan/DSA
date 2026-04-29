from collections import Counter

class Solution:
    def findLHS(self, nums):
        freq = Counter(nums)
        res = 0
        
        for x in freq:
            if x + 1 in freq:
                res = max(res, freq[x] + freq[x + 1])
        
        return res