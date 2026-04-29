class Solution:
    def findComplement(self, num):
        mask = 1
        
        # tạo mask dạng 111...111
        while mask <= num:
            mask <<= 1
        
        mask -= 1
        
        return num ^ mask