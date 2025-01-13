class Solution:
    def getNGELInd(self, arr, n):

        st = []

        ngl = [-1 for i in range(n)]

        for i in range(n):

            if not st:

                ngl[i] = -1

                st.append(i)
            
            elif st and arr[st[-1]] > arr[i]:

                ngl[i] = st[-1]
            
                st.append(i)
            
            elif st and arr[st[-1]] <= arr[i]:

                while st and arr[st[-1]] < arr[i]: # IF WE SEE DUPLICATE ALSO WE STOP TO OVERCOUNT THE RANGES

                    st.pop()
                
                if st :

                    ngl[i] = st[-1]
                
                else:

                    ngl[i] = -1
                
                st.append(i)
        
        return ngl
                


    def getNGRInd(self, arr, n):
        st = []

        ngr = [n for i in range(n)]

        for i in reversed(range(n)):

            if not st:

                ngr[i] = n

                st.append(i)
            
            elif st and arr[st[-1]] > arr[i]:

                ngr[i] = st[-1]
            
                st.append(i)
            
            elif st and arr[st[-1]] <= arr[i]:

                while st and arr[st[-1]] <= arr[i]:

                    st.pop()
                
                if st :

                    ngr[i] = st[-1]
                
                else:

                    ngr[i] = n
                
                st.append(i)
        
        return ngr

    def getNSELInd(self, arr, n):
        st = []

        nsl = [-1 for i in range(n)]

        for i in range(n):

            if not st:

                nsl[i] = -1

                st.append(i)
            
            elif st and arr[st[-1]] < arr[i]:

                nsl[i] = st[-1]
            
                st.append(i)
            
            elif st and arr[st[-1]] >= arr[i]:

                while st and arr[st[-1]] > arr[i]:

                    st.pop()
                
                if st :

                    nsl[i] = st[-1]
                
                else:

                    nsl[i] = -1
                
                st.append(i)
        
        return nsl

    def getNSRInd(self, arr, n):
        st = []

        nsr = [n for i in range(n)]

        for i in reversed(range(n)):

            if not st:

                nsr[i] = n

                st.append(i)
            
            elif st and arr[st[-1]] < arr[i]:

                nsr[i] = st[-1]
            
                st.append(i)
            
            elif st and arr[st[-1]] >= arr[i]:

                while st and arr[st[-1]] >= arr[i]:

                    st.pop()
                
                if st :

                    nsr[i] = st[-1]
                
                else:

                    nsr[i] = n
                
                st.append(i)
        
        return nsr

    def subArrayRanges(self, nums: List[int]) -> int:
        
        n = len(nums)

        ngl = self.getNGELInd(nums,n)

        ngr = self.getNGRInd(nums,n)

        nsl = self.getNSELInd(nums,n)

        nsr = self.getNSRInd(nums,n)

        ans = 0

        for i in range(n):

            largFreq = (ngr[i] - i) * ( i - ngl[i])  # -1 bcz we are counting cur number twice

            smalFreq = (nsr[i] - i ) * (i - nsl[i] ) 

            ans += (largFreq - smalFreq) * nums[i]
        
        return ans


            
        
