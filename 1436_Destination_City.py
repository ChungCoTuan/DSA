class Solution(object):
    def destCity(self, paths):
        return (set(path[1] for path in paths) - set(path[0] for path in paths)).pop()