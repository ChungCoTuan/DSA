class Solution(object):
    def readBinaryWatch(self, turnedOn):
        result = []
        
        for h in range(12):
            for m in range(60):              
                if bin(h).count('1') + bin(m).count('1') == turnedOn:                   
                    time_str = "{}:{:02d}".format(h, m)
                    result.append(time_str)
                    
        return result