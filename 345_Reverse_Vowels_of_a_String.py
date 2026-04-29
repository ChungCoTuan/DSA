class Solution:
    def reverseVowels(self, s):
        vowels = set("aeiouAEIOU")
        s = list(s)
        
        left, right = 0, len(s) - 1
        
        while left < right:
            # tìm nguyên âm bên trái
            while left < right and s[left] not in vowels:
                left += 1
            
            # tìm nguyên âm bên phải
            while left < right and s[right] not in vowels:
                right -= 1
            
            # swap
            s[left], s[right] = s[right], s[left]
            
            left += 1
            right -= 1
        
        return "".join(s)