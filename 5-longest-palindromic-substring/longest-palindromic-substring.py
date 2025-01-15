class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        n = len(s)

        longest_palin_str = ""

        for k in range(n):
            # expanding algo
            # odd length expand attempt

            i,j = k,k

            odd_len_str = ""

            while i >=0 and j < len(s) and s[i] == s[j]:

                odd_len_str = s[i:j+1]

                i -= 1

                j += 1
            
                if len(odd_len_str) > len(longest_palin_str):

                    longest_palin_str = odd_len_str

            # even length expand attempt

            i,j = k,k+1

            even_len_str = ""

            while i >=0 and j < len(s) and s[i] == s[j]:

                even_len_str = s[i:j+1]

                if len(even_len_str) > len(longest_palin_str):

                    longest_palin_str = even_len_str

                i -= 1

                j += 1
            
        
        return longest_palin_str
        

        
        