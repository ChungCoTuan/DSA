class Solution:
    def intersection(self, nums1, nums2):
        set1 = set(nums1)
        res = set()
        
        for num in nums2:
            if num in set1:
                res.add(num)
        
        return list(res)