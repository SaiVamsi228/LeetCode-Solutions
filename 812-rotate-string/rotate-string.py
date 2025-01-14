class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        
        if len(s) != len(goal):

            return False
            
        circString = s + s

        isRotated = circString.find(goal) 

        if isRotated == -1 :

            return False
        
        return True
        