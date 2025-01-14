class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        
        st = []
        res = []

        for char in s :

            # if open br
            if char == "(":

                if st:

                    st.append("(")

                    res.append("(")
                
                else:

                    st.append("(")
            
            # if closed br
            else:

                if len(st) > 1 :

                    res.append(")")

                    st.pop()
                
                elif len(st) == 1 :

                    st.pop()
        
        return "".join(res)
            