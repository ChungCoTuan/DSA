class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        jewels_set = set(jewels)
        return sum(s in jewels_set for s in stones)