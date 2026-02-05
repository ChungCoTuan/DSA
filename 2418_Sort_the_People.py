class Solution(object):
    def sortPeople(self, names, heights):
        return [n for h, n in sorted(zip(heights, names), reverse=True)]