class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        char_counts = {}
        for char in magazine:
            char_counts[char] = char_counts.get(char, 0) + 1
        for char in ransomNote:
            if char not in char_counts or char_counts[char] <= 0:
                return False
            char_counts[char] -= 1
        
        return True