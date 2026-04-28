class Solution:
    def isHappy(self, n):
        seen = set()
        
        while n != 1:
            if n in seen:
                return False  # bị lặp
            
            seen.add(n)
            
            # tính tổng bình phương chữ số
            total = 0
            while n > 0:
                digit = n % 10
                total += digit * digit
                n //= 10
            
            n = total
        
        return True