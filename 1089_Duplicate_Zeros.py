class Solution(object):
    def duplicateZeros(self, arr):
        i = 0
        while i < len(arr) - 1:
            if arr[i] == 0:
                arr.pop()
                arr.insert(i + 1, 0)
                i += 1
            i += 1