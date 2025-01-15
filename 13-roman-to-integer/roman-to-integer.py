class Solution:
    def romanToInt(self, s: str) -> int:

        integer_value = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        ans = 0

        n = len(s)

        for i in range(n):

            char = s[i]

            if i == n-1 or integer_value[char] >= integer_value[s[i+1]]:

                ans += integer_value[char]

            elif integer_value[char] < integer_value[s[i + 1]]:

                ans -= integer_value[char]

        
        return ans
            
