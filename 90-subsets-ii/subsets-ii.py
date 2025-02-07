class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        ans = set()

        def getSubset(n,subset):

            if n == 0:

                ans.add(tuple(subset.copy()))

                return
            
            notTake = getSubset(n-1,subset)
            
            subset.append(nums[n-1])

            take = getSubset(n-1,subset)

            subset.pop()
        

        nums.sort()

        n = len(nums)

        getSubset(n,[])

        return list(ans)


            
                
        