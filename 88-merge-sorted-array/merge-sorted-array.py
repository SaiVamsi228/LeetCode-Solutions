class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        # Optimal

        i = j = k = 0

        n1 = len(nums1)

        merged_arr = [0 for i in range(n1)]

        while i < m and j < n:

            if nums1[i] <= nums2[j] :

                merged_arr[k] = nums1[i]

                i += 1

                k += 1
            
            else:

                merged_arr[k] = nums2[j]

                j += 1

                k += 1
        
        while i < m :

            merged_arr[k] = nums1[i]

            i += 1

            k += 1
        
        while j < n :

            merged_arr[k] = nums2[j]

            j += 1

            k += 1

        for i in range(n1):

            nums1[i] = merged_arr[i]
        
        return nums1




                

        
        