class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        
        g.sort()

        s.sort()

        cnt = 0

        m = len(g) 

        n = len(s) 

        i = m - 1

        j = n - 1

        while i >= 0 and j >= 0:

            if s[j] >= g[i] :

                cnt += 1

                j -= 1

                i -= 1
            
            elif s[j] < g[i] :

                i -= 1
        
        return cnt
        




