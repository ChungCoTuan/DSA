class Solution:
    def licenseKeyFormatting(self, s, k):
        s = s.replace('-', '').upper()
        
        res = []
        
        # duyệt từ cuối
        for i in range(len(s), 0, -k):
            res.append(s[max(0, i - k):i])
        
        return '-'.join(res[::-1])