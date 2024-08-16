class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        i = j = 0
        Dict = defaultdict(int)
        n = len(s)
        mx = 0
        uniqueCnt = 0
        
        while j < n:
            
            Dict[s[j]] += 1

            if Dict[s[j]] == 1:
                
                uniqueCnt += 1
            
            if uniqueCnt < j-i+1 :
                
                while uniqueCnt < j-i+1 : #trying to move i to make window size == uniqueCnt
                    
                    Dict[s[i]] -= 1
                    
                    if Dict[s[i]] == 0 :
                        
                        uniqueCnt -= 1
                    
                    i += 1
                
                j += 1
            
            elif uniqueCnt == j-i+1 :
                
                mx = max(j-i+1, mx)
                
                j += 1              
                
        return mx 
