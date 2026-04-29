import math

class Solution:
    def checkPerfectNumber(self, num):
        if num <= 1:
            return False
        
        total = 1  # 1 luôn là ước
        
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                total += i
                if i != num // i:
                    total += num // i
        
        return total == num