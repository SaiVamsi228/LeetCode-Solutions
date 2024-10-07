from sys import maxsize
class Solution:
    def minLength(self, s: str) -> int:

        stack = []

        for i in range(len(s)):

            char = s[i]

            if not stack:

                stack.append(char)
            
            elif char == "D" and stack[-1] == "C" :

                stack.pop()
            
            elif char == "B" and stack[-1] == "A":

                stack.pop()
            
            else:

                stack.append(char)
        
        return len(stack)