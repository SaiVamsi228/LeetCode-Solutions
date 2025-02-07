class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        
        g.sort()

        s.sort()

        i = 0

        j = 0

        m = len(g)

        n = len(s)

        content_children_cnt = 0

        while i < m and j < n :

            if s[j] >= g[i] :

                content_children_cnt += 1

                i += 1

                j += 1
            
            elif s[j] < g[i]:

                j += 1
            
        
        return content_children_cnt
