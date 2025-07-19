class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        
        res = []

        cnt = 0

        for char in s:

            if char == "(":

                if cnt == 0:

                    cnt += 1
                
                else:

                    cnt += 1

                    res.append(char)
            
            elif char == ")":

                if cnt == 1:

                    cnt -= 1
                
                else:

                    cnt -= 1

                    res.append(char)
        
        return "".join(res)
                
                


                


            