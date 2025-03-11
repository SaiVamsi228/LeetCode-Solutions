class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        
        g.sort()

        s.sort()

        content_children = 0

        n1 = len(g)

        n2 = len(s)

        i = n1 - 1
        
        j = n2 - 1

        while i >= 0 and j >= 0:

            if s[j] >= g[i]:

                content_children += 1

                j -= 1

                i -= 1
            
            else:

                i -= 1
        
        return content_children