class Solution:
    def findRelativeRanks(self, score):
        n = len(score)
        
        # lưu index ban đầu
        indexed = [(s, i) for i, s in enumerate(score)]
        
        # sort giảm dần theo điểm
        indexed.sort(reverse=True)
        
        res = [""] * n
        
        for rank, (s, i) in enumerate(indexed):
            if rank == 0:
                res[i] = "Gold Medal"
            elif rank == 1:
                res[i] = "Silver Medal"
            elif rank == 2:
                res[i] = "Bronze Medal"
            else:
                res[i] = str(rank + 1)
        
        return res