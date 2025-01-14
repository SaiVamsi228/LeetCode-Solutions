class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        
        cnt = 0

        res = []

        for char in s:

            if char == "(":

                cnt += 1

                if cnt > 1 :

                    res.append("(")
            
            if char == ")":

                cnt -= 1

                if cnt > 0:

                    res.append(")")
        
        return "".join(res)

