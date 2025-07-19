class Solution:
    def myAtoi(self, s: str) -> int:
        
        ans = 0

        i = 0

        s = s.lstrip()

        if not s:
            return 0

        n = len(s)

        neg = False

        i = 0

        if s[0] == "-" :

            neg = True

            i += 1
        
        elif s[0] == "+":

            neg = False

            i += 1
        
        while i < n and s[i].isnumeric():

            ans = ans * 10 + int(s[i])

            i += 1
        

        if neg:

            ans = - ans
        
        MINI = -2**31 

        MAXI = 2**31-1

        ans = max(MINI,ans)

        ans = min(MAXI,ans)

        return ans

