class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        
        n = len(arr)

        nsl = [-1 for i in range(n)]

        nsr = [n for i in range(n)]

        st = []

        for i in range(n):

            if not st:

                nsl[i] = -1
            
            elif st and st[-1][0] < arr[i]:

                nsl[i] = st[-1][1]
            
            elif st and st[-1][0] >= arr[i]:

                while st and st[-1][0] >= arr[i]:

                    st.pop()
                
                if st :

                    nsl[i] = st[-1][1]
                
                else:

                    nsl[i] = -1
                
            st.append((arr[i],i))
        
        st = []

        for i in reversed(range(n)):

            if not st:

                nsr[i] = n
            
            elif st and st[-1][0] < arr[i]:

                nsr[i] = st[-1][1]
            
            elif st and st[-1][0] >= arr[i]:
                
                # IMP: WE ARE NOT GOING BEYOND DUPLI
                # STOP BEFORE DUPLI WHILE GOING BACK
                while st and st[-1][0] > arr[i]: 

                    st.pop()
                
                if st :

                    nsr[i] = st[-1][1]
                
                else:

                    nsr[i] = n
                
            st.append((arr[i],i))
        
        freq = [0 for i in range(n)]

        for i in range(n):

            cur_ind = i

            r_ind = nsr[i]

            l_ind = nsl[i]

            left = cur_ind - l_ind

            right = r_ind - cur_ind

            freq[i] = left * right
        
        ans = 0

        for i in range(n):

            ans = (ans + freq[i] * arr[i]) % (10**9 + 7)

        return ans
        

        

            
