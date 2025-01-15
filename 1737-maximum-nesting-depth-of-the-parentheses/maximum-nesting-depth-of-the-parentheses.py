class Solution:
    def maxDepth(self, s: str) -> int:
        
        cnt = 0

        n = len(s)

        mx = 0

        for i in range(n):

            char = s[i]

            if char.isnumeric():

                continue
            
            if char == "(":

                cnt += 1
            
            if char == ")":

                cnt -= 1
            
            mx = max(mx, cnt)
        
        return mx
        