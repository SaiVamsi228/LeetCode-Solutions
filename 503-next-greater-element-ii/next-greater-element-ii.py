class Solution:
    def getNGR(self, nums, n) :
        
        ngr = [-1 for i in range(n)]
        
        stack = []
        
        for i in reversed(range(n)):
            
            if not stack:
                
                ngr[i] = -1
            
            elif stack and stack[-1] > nums[i]:
                
                ngr[i] = stack[-1]
                
            elif stack and stack[-1] <= nums[i]:
                
                while stack and stack[-1] <= nums[i]:
                    
                    stack.pop()
                
                if not stack:
                    
                    ngr[i] = -1
                
                else:
                    
                    ngr[i] = stack[-1]
                
            stack.append(nums[i])
        
        return ngr

    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        circArr = nums + nums

        n = 2 * len(nums)

        ngrCircArr = self.getNGR(circArr,n)

        res = ngrCircArr[:n//2]
        
        return res