class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        def get_nge(nums):
            
            n = len(nums)

            nge = [-1 for i in range(n)]

            st = []

            for i in reversed(range(n)):

                if not st:

                    st.append(i)
                
                elif st and nums[st[-1]] > nums[i]:

                    nge[i]  = st[-1]

                    st.append(i)
                
                elif st and nums[st[-1]] <= nums[i]:

                    while st and nums[st[-1]] <= nums[i]:
                        
                        st.pop()
                    
                    if not st:

                        nge[i] = -1
                    
                    else:

                        nge[i] = st[-1]
                    
                    st.append(i)
            
            return nge
        
        nge = get_nge(nums2)

        n = len(nums1)

        ans = [ -1 for i in range(n)]

        for i in range(n):

            ind = nums2.index(nums1[i])
            
            nge_ind = nge[ind]

            if nge_ind == -1 :

                ans[i] = -1
            
            else:
                
                ans[i] = nums2[nge_ind]

        return ans


                
