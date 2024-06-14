class Solution:

    def isPair(self,opening,closing):
        
        isPairDict = {"[":"]","(":")","{":"}"}
        
        if isPairDict[opening] == closing:
            
            return True
            
        return False
        
        
    
    def isValid(self, s: str) -> bool:
        
        stack = []

        for char in s:
            
            if char in "[({":
                
                stack.append(char)
            
            elif char in ")]}":
                
                if not self.isEmpty(stack) and self.isPair(self.peek(stack),char):
                    
                    stack.pop()
                
                else:
                    
                    return False
                    
        
        if not self.isEmpty(stack):
            
            return False
            
        return True

    def isEmpty(self,stack):

        return len(stack) == 0

    def peek(self,stack):

        return stack[-1]