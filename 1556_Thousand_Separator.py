class Solution(object):
    def thousandSeparator(self, n):
        return "{:,}".format(n).replace(",", ".")