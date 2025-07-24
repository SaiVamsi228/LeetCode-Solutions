class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        ans = []

        def getAllComb(start,k,target,sb):

            if k < 0 :

                return

            if target == 0 and k == 0:

                ans.append(sb.copy())
                
                return 
            
            for num in range(start,10):

                if num <= target:
                    
                    sb.append(num)

                    getAllComb(num+1,k-1,target - num,sb )

                    sb.pop()
                
        sb = []

        getAllComb(1,k,n,sb)

        return ans