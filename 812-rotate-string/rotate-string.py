class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        
        n = len(s)

        goal = [x for x in goal]

        arr = [ x for x in s]

        for i in range(n):

            arr.append(arr.pop(0))

            if arr == goal:

                return True
        
        return False