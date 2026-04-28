class Solution:
    def summaryRanges(self, nums):
        res = []
        i = 0
        n = len(nums)
        
        while i < n:
            start = nums[i]
            
            # đi hết đoạn liên tiếp
            while i + 1 < n and nums[i] + 1 == nums[i + 1]:
                i += 1
            
            # nếu chỉ có 1 số
            if start == nums[i]:
                res.append(str(start))
            else:
                res.append(str(start) + "->" + str(nums[i]))
            
            i += 1
        
        return res