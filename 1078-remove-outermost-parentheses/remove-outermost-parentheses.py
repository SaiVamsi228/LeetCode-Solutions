class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        
        res = []

        stack = []

        for char in s:

            if char == "(":

                if len(stack) == 0:

                    stack.append(char)
                
                else:

                    stack.append(char)

                    res.append(char)
            
            elif char == ")":

                if len(stack) == 1:

                    stack.pop()
                
                else:

                    stack.pop()

                    res.append(char)
        
        return "".join(res)
                
                


                


            