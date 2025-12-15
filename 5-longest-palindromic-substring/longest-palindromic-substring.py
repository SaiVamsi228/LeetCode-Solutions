class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        n = len(s)
        
        if n == 0:
            
            return ""
        
        if n == 1:
            
            return s
        
        mx = 1
        
        left_ind = right_ind = -1
        
        for i in range(n):
            
            cur_len = 1
            
            # odd length
            j = i - 1
            
            k = i + 1
            
            while j >= 0 and k < n :
                
                if s[j] == s[k]:
                    
                    if k - j + 1 > mx:
                
                        mx = k - j + 1
                        
                        left_ind = j
                        
                        right_ind = k
                    
                    j -= 1
                    
                    k += 1
                
                else:
                    
                    break
            
            # even length
            j = i
            
            k = i + 1
            
            while j >= 0 and k < n :
                
                if s[j] == s[k]:
                    
                    if k - j + 1 > mx:
                
                        mx = k - j + 1 
                        
                        left_ind = j
                        
                        right_ind = k
                    
                    j -= 1
                    
                    k += 1
                
                else:
                    
                    break
        
        if left_ind == -1 and right_ind == -1:
            
            return s[0]
            
        return s[left_ind: right_ind + 1]
                 