class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        
        def getNGELInd(nums,n):

            st = []

            ngl = [-1 for i in range(n)]

            for i in range(n):

                if not st:

                    st.append(i)
                
                elif st and nums[st[-1]] > nums[i]:

                    ngl[i] = st[-1]

                    st.append(i)
                
                elif st and nums[st[-1]] <= nums[i]:

                    while st and nums[st[-1]] < nums[i] :

                        st.pop()
                    
                    if st :

                        ngl[i] = st[-1]
                    
                    else:

                        ngl[i] = -1
                    
                    st.append(i)
            
            return ngl
                    

        def getNGRInd(nums,n):

            st = []

            ngl = [n for i in range(n)]

            for i in reversed(range(n)):

                if not st:

                    st.append(i)
                
                if st and nums[st[-1]] > nums[i]:

                    ngl[i] = st[-1]

                    st.append(i)
                
                elif st and nums[st[-1]] <= nums[i]:

                    while st and nums[st[-1]] <= nums[i] :

                        st.pop()
                    
                    if st :

                        ngl[i] = st[-1]
                    
                    else:

                        ngl[i] = n
                    
                    st.append(i)
            
            return ngl

        n = len(nums)

        ngr = getNGRInd(nums,n)
        ngl = getNGELInd(nums,n)

        ans = []

        for curInd in range(n):

            if curInd - k + 1 >= 0 :

                lB = curInd - k + 1
            
            else:

                lB = 0

            if curInd + k - 1 >= 0 :

                rB = curInd + k - 1
            
            else:

                rB = n - 1
            
            newNglInd = ngl[curInd] if ngl[curInd] >= lB else lB - 1

            newNgrInd = ngr[curInd] if ngr[curInd] <= rB else rB + 1

            length = newNgrInd - newNglInd - 1  

            freqCurInd = length - k + 1
        
            for _ in range(freqCurInd):

                ans.append(nums[curInd])
        
        return ans

            
            




