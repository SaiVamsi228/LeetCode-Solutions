class Solution:
    def isValid(self, s: str) -> bool:
        
        st = []

        for char in s:

            if char in "([{":

                st.append(char)
            
            else:
                
                if not st:

                    return False
                    
                prev = st.pop()

                if char == ")" and prev =="(":

                    continue
                
                elif char == "]" and prev == "[":

                    continue
                
                elif char == "}" and prev == "{":

                    continue
                
                else:

                    return False

        if st :

            return False

        return True