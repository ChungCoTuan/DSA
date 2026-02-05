class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        if not timeSeries:
            return 0
        
        total_time = 0
        for i in range(len(timeSeries) - 1):
            total_time += min(duration, timeSeries[i+1] - timeSeries[i])
            
        total_time += duration
        return total_time