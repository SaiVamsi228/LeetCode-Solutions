class Solution:
    def isValid(self, s: str) -> bool:
        
        st = []

        for char in s:

            if char in "([{":

                st.append(char)
            
            else:

                if not st:

                    return False

                if char == ")" and st[-1] == "(":

                    st.pop()
                
                elif char == "]" and st[-1] == "[":

                    st.pop()
                
                elif char == "}" and st[-1] == "{":

                    st.pop()
                
                else:

                    return False
        
        if st:

            return False
        
        return True
                
