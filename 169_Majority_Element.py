class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        candidate = None
        count = 0
        
        for num in nums:
            # Nếu số phiếu về 0, chọn ứng viên mới
            if count == 0:
                candidate = num
            
            # Nếu gặp đúng ứng viên thì cộng phiếu, khác thì trừ phiếu
            if num == candidate:
                count += 1
            else:
                count -= 1
                
        return candidate