class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        cnt = 0

        mn = 0
        
        for char in s:

            if char == "(":

                cnt += 1
            
            else:

                cnt -= 1

            if cnt < 0:

                cnt = 0 

                mn += 1
            
        
        if cnt > 0:

            mn += cnt
        
        return mn