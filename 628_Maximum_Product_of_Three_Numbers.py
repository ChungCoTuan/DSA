class Solution:
    def maximumProduct(self, nums):
        nums.sort()
        
        # case 1: 3 số lớn nhất
        case1 = nums[-1] * nums[-2] * nums[-3]
        
        # case 2: 2 số nhỏ nhất + số lớn nhất
        case2 = nums[0] * nums[1] * nums[-1]
        
        return max(case1, case2)