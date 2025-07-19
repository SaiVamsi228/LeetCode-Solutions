class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        m = len(nums1)

        n = len(nums2)

        N = m + n

        i = j = k = 0

        ind1 = N//2 - 1

        ind2 = N//2

        while i < m and j < n:

            if k == ind1:

                ind1_ele = min(nums1[i],nums2[j])
            
            if k == ind2 :

                ind2_ele = min(nums1[i],nums2[j])

            if nums1[i] < nums2[j]:
                
                i += 1

            else:
                
                j += 1

            k += 1

        while i < m:
            
            if k == ind1:

                ind1_ele = nums1[i]
            
            if k == ind2 :

                ind2_ele = nums1[i]

            i += 1
            k += 1


        while j < n:
            
            if k == ind1:

                ind1_ele = nums2[j]
            
            if k == ind2 :

                ind2_ele = nums2[j]

            j += 1

            k += 1
        
        if N%2 == 0:

            return (ind1_ele + ind2_ele)/2
        
        return ind2_ele

        






        

