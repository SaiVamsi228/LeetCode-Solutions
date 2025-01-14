class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):

            return False
            
        freq1 = [0 for i in range(26)]

        freq2 = [0 for i in range(26)]

        for char in s:

            freq1[ord(char) - 97] += 1

        for char in t:

            freq2[ord(char) - 97] += 1
        
        for i in range(26):

            if freq1[i] != freq2[i]:

                return False
        
        return True
        
