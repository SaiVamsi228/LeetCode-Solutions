class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        newNums = nums + nums

        n = len(newNums)

        stack = []

        nge = [-1 for i in range(n//2)]

        for i in reversed(range(n)):

            curEle = newNums[i]

            if not stack:

                if i < n//2:
                    
                    nge[i] = -1

            elif stack[-1] > curEle:

                if i < n//2:
                    
                    nge[i] = stack[-1]

            else:

                while stack and stack[-1] <= curEle:

                    stack.pop()

                if stack:
                    
                    if i < n//2:
                        
                        nge[i] = stack[-1]

                else:
                    
                    if i < n//2:

                        nge[i] = -1
            
            stack.append(curEle)

        return nge




            

            