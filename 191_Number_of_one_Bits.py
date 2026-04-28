class Solution:
    def hammingWeight(self, n):
        count = 0
        
        for _ in range(32):
            count += (n & 1)  # nếu bit cuối là 1 → cộng
            n >>= 1           # dịch phải
        
        return count