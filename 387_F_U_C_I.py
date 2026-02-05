class Solution(object):
    def firstUniqChar(self, s):
        import collections
        count = collections.Counter(s)
        for i, c in enumerate(s):
            if count[c] == 1:
                return i
        return -1