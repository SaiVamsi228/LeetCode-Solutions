class Solution:
    def romanToInt(self, s: str) -> int:

        integer_value = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        st = []

        n = len(s)

        for i in reversed(range(n)):

            char = s[i]

            if not st:

                st.append(integer_value[char])
            
            elif st and integer_value[char] < st[-1]:

                big = st.pop()

                new = big - integer_value[char]

                st.append(new)
            
            elif st and integer_value[char] >= st[-1]:

                st.append(integer_value[char])
        
        return sum(st)