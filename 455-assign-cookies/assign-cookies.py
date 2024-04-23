class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        i , j = 0, 0

        n1 , n2 = len(g), len(s)
        
        content_children = 0

        while i<n1 and j<n2:

            if s[j] >= g[i]:

                content_children += 1

                i += 1
            
            j+=1

        
        return content_children
        