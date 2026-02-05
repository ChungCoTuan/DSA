class Solution(object):
    def capitalizeTitle(self, title):
        return " ".join(word.lower() if len(word) < 3 else word.capitalize() for word in title.split())