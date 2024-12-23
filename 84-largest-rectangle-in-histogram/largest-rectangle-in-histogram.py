class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        n = len(heights)
        
        def getNSEtoR(arr): # get nearest smaller ele to right 

            st = []

            res = [-1 for i in range(n)]

            for i in reversed(range(n)):

                if not st :

                    res[i] = -1
                
                elif st and st[-1][0] < arr[i]:

                    res[i] = st[-1][1]
                
                elif st and st[-1][0] >= arr[i]:

                    while st and st[-1][0] >= arr[i]:

                        st.pop()
                    
                    if st :

                        res[i] = st[-1][1]
                    
                    else:

                        res[i] = -1
                    
                st.append((arr[i], i))
            

            return res
        
        def getNSEtoL(arr): # get nearest smaller ele to the left

            st = []

            res = [-1 for i in range(n)]

            for i in range(n):

                if not st :

                    res[i] = -1
                
                elif st and st[-1][0] < arr[i]:

                    res[i] = st[-1][1]
                
                elif st and st[-1][0] >= arr[i]:

                    while st and st[-1][0] >= arr[i]:

                        st.pop()
                    
                    if st :

                        res[i] = st[-1][1]
                    
                    else:

                        res[i] = -1
                    
                st.append((arr[i], i))
            

            return res
        
        nSEtoR_arr = getNSEtoR(heights)

        nSEtoL_arr = getNSEtoL(heights)

        maxi_area_possible = 0

        for i in range(n):

            right_ind = nSEtoR_arr[i] if nSEtoR_arr[i] != -1 else n

            left_ind = nSEtoL_arr[i]

            cur_max_area = (right_ind - left_ind - 1) * heights[i]

            maxi_area_possible = max(maxi_area_possible, cur_max_area)
        
        return maxi_area_possible
