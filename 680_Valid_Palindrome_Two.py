class Solution:
    def validPalindrome(self, s):
        left = 0
        right = len(s) - 1
        
        while left < right:
            if s[left] != s[right]:
                # Nếu gặp hai ký tự khác nhau, ta có 2 lựa chọn:
                # 1. Xóa ký tự bên trái: Kiểm tra phần còn lại s[left+1 : right+1]
                # 2. Xóa ký tự bên phải: Kiểm tra phần còn lại s[left : right]
                delete_left = s[left + 1 : right + 1]
                delete_right = s[left : right]
                
                # Kiểm tra xem một trong hai chuỗi con có đối xứng không
                return delete_left == delete_left[::-1] or \
                       delete_right == delete_right[::-1]
            
            left += 1
            right -= 1
            
        return True