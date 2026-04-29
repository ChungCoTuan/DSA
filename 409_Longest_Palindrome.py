class Solution:
    def longestPalindrome(self, s):
        count = {}
        
        for ch in s:
            count[ch] = count.get(ch, 0) + 1
        
        length = 0
        odd_found = False
        
        for val in count.values():
            if val % 2 == 0:
                length += val
            else:
                length += val - 1
                odd_found = True
        
        if odd_found:
            length += 1
        
        return length