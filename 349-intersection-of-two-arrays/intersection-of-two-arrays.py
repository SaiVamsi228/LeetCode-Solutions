class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        st = set()

        a = sorted(nums1)

        b = sorted(nums2)

        m = len(a)

        n = len(b)

        i = j = 0

        while i < m and j < n :

            if a[i] < b[j]:

                i += 1
            
            elif a[i] > b[j]:

                j += 1
            
            else:

                st.add(a[i])

                i += 1

                j += 1
        
        res = list(st)
        
        return res