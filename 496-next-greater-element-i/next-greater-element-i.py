from collections import defaultdict
class Solution:

    def getIndex(self,ele,nums2,n):

        for i in range(n):
 
            if nums2[i] == ele:

                return i

    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        n1 = len(nums1)

        n2 = len(nums2)

        hashMap = defaultdict(int)

        stack = []

        for i in reversed(range(n2)):

            curEle = nums2[i]

            if not stack:

                hashMap[curEle] = -1 

                stack.append(curEle)
            
            elif stack[-1] > curEle:

                hashMap[curEle] = stack[-1]
            
            else:

                while stack and stack[-1] <= curEle:

                    stack.pop()

                if stack:

                    hashMap[curEle] = stack[-1]

                else:

                    hashMap[curEle] = -1

            stack.append(curEle)

        nge = [hashMap[x] for x in nums1]

        return nge
        


        

                
                    
                





