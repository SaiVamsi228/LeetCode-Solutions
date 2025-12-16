class Solution:
    def countSubstrings(self, s: str) -> int:
        
        def isPalindrome(string):
            
            return string == string[::-1]
        
        n = len(s)
        
        cnt = 0
        
        for i in range(n):
            
            for j in range(i,n):
                
                if isPalindrome(s[i:j+1]):
                    
                    cnt += 1
        
        return cnt