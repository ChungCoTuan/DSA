class Solution:
    def divisorGame(self, n):
        # Alice thắng nếu n là số chẵn
        # Alice thua nếu n là số lẻ
        return n % 2 == 0