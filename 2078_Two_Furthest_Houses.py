class Solution(object):
    def maxDistance(self, colors):
        n = len(colors)
        res = 0
        for i in range(n):
            if colors[i] != colors[0]:
                res = max(res, i)
            if colors[i] != colors[n - 1]:
                res = max(res, n - 1 - i)
        return res