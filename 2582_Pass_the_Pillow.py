class Solution(object):
    def passThePillow(self, n, time):
        chunks = time // (n - 1)
        remaining = time % (n - 1)
        if chunks % 2 == 0:
            return 1 + remaining
        else:
            return n - remaining