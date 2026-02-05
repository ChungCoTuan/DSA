class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
        time = 0
        for i, val in enumerate(tickets):
            if i <= k:
                time += min(val, tickets[k])
            else:
                time += min(val, tickets[k] - 1)
        return time
        