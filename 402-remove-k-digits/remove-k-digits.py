class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        
        st = []

        n = len(num)

        for i in range(n):

            if not k :

                st.append(num[i])
            
                continue
            
            if not st :

                st.append(num[i])
            
            elif st and st[-1] < num[i]:

                st.append(num[i])
            
            elif st and st[-1] >= num[i]:

                while k and st and st[-1] > num[i]:

                    st.pop()

                    k -= 1
                
                st.append(num[i])
        
        while k and st : # if it doesnt satisfy our cond and still k > 0
            st.pop()

            k -= 1
            
        ans = "".join(st)
        
        ans = ans.lstrip("0")

        if ans == "":

            return "0"

        return ans 