from collections import Counter
class Solution:
    def beautySum(self, s: str) -> int:
        
        def getBeauty(t):

            hm = Counter(t)

            highest_freq = max(hm.values())

            least_freq = min(hm.values())
        
            return highest_freq - least_freq
        
        n = len(s)

        beauty_sum = 0
        
        for i in range(n):

            for j in range(i,n):

                beauty_sum += getBeauty(s[i:j+1])
        
        return beauty_sum







