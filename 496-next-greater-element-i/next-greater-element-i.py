class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        n2 = len(nums2)
        
        res = [-1]*n2
        
        stack = []
        
        for i in reversed(range(n2)):
            
            if not stack:
                
                res[i] = -1
            
            elif stack and stack[-1] > nums2[i]:
                
                res[i] = stack[-1]
                
            elif stack and stack[-1] <= nums2[i]:
                
                while stack and stack[-1] <= nums2[i]:
                    
                    stack.pop()
                
                if not stack:
                    
                    res[i] = -1
                
                else:
                    
                    res[i] = stack[-1]
                
            stack.append(nums2[i])
        
        n1 = len(nums1)
        
        final_res = [-1]*n1

        for i in range(n1):

            ind = nums2.index(nums1[i])

            final_res[i] = res[ind]
        
        return final_res
        