class Solution:

    def getIndex(self,ele,nums2,n):

        for i in range(n):

            if nums2[i] == ele:

                return i

    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        n1 = len(nums1)

        n2 = len(nums2)

        ngeArr = [-1 for i in range(n1)]

        for i in range(n1):

            index = self.getIndex(nums1[i],nums2,n2)

            for j in range(index+1, n2):

                if nums2[j] > nums2[index]:

                    ngeArr[i] = nums2[j]

                    break

        return ngeArr




