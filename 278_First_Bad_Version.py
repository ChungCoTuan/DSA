class Solution:
    def firstBadVersion(self, n):
        left, right = 1, n
        
        while left < right:
            mid = (left + right) // 2
            
            if isBadVersion(mid):
                right = mid   # có thể là bad đầu tiên
            else:
                left = mid + 1  # bỏ qua bên trái
        
        return left