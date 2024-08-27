class Solution:
    def checkAndSwap(self,nums,n1, n2):
        
        s1 = str(n1)
        
        s2 = str(n2)
        
        i = 0
        
        m = len(s1) 
        
        n = len(s2)
        
        if s1 == s2 : return True
        
        if n < m :
            
            s2 = "0" * (m-n) + s2
            
            n = m
        
        elif m < n :
            
            s1 = "0" * (n-m) + s1
            
            m = n       
        
        
        notEqual = 0
        
        for i in range(m):

            if s1[i] != s2[i]: notEqual += 1
        
        return sorted(s1) == sorted(s2) and notEqual <= 2
                
            
    def countPairs(self, nums: List[int]) -> int:
        
        n = len(nums)
        
        cnt = 0
        
        for i in range(n):
            
            for j in range(i+1,n):
                
                if self.checkAndSwap(nums,nums[i], nums[j]):
                    
                    
                    cnt += 1
        
        return cnt
                