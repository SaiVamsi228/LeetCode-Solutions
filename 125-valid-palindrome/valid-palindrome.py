class Solution:
    def isPalindrome(self, s: str) -> bool:

        newStr = []

        for char in s:

            if char.isalnum():

                newStr.append(char)
        
        newStr = "".join(newStr)

        s = newStr

        i = 0

        j = len(s) - 1

        while i < j :

            if s[i].lower() != s[j].lower():

                return False

            i += 1 

            j -= 1
        
        return True