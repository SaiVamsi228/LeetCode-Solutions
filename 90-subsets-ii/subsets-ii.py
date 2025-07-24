class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        ans = []

        def getAllSubsets(ind,sb):

            ans.append(sb.copy())

            if ind == n :

                return 
            
            for i in range(ind,n):

                if i > ind and nums[i] == nums[i-1]:

                    continue
                
                sb.append(nums[i])

                getAllSubsets(i+1,sb)

                sb.pop()
        

        nums.sort()

        n = len(nums)

        getAllSubsets(0,[])

        return ans
