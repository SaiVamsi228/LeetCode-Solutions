class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        
        st = []

        n = len(num)

        for i in range(n):

            if not k or not st:

                st.append(num[i])
            
            elif st and st[-1] < num[i]:

                st.append(num[i])
            
            elif st and st[-1] >= num[i]:

                # st[-1] > then only pop else we dont know there may be other number that we need to remove ahead

                while k > 0 and st and st[-1] > num[i]:
                    
                    k -= 1

                    st.pop()
                
                st.append(num[i])
        
        while st and k > 0:

            st.pop()

            k -= 1

        s = "".join(st)

        s = s.lstrip("0")

        if s == "":

            return "0"

        return s
