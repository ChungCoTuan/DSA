class Solution:
    def intersect(self, nums1, nums2):
        count = {}
        res = []
        
        # đếm nums1
        for num in nums1:
            count[num] = count.get(num, 0) + 1
        
        # duyệt nums2
        for num in nums2:
            if num in count and count[num] > 0:
                res.append(num)
                count[num] -= 1
        
        return res