class Solution(object):
    def toGoatLatin(self, sentence):
        vowels = set("aeiouAEIOU")
        words = sentence.split()
        result = []
        
        for i, word in enumerate(words):
            if word[0] in vowels:
                word += "ma"
            else:
                word = word[1:] + word[0] + "ma"
            
            word += "a" * (i + 1)
            result.append(word)
            
        return " ".join(result)