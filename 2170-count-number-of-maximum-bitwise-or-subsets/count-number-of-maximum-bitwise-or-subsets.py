class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        
        maxi = -1

        maxiCnt = 0

        def solve(i, curOr, arr):

            nonlocal maxi , maxiCnt

            if i == -1:

                if curOr == maxi:

                    maxiCnt += 1

                elif curOr > maxi :

                    maxi = curOr

                    maxiCnt = 1
                
                return 
            
            take = solve(i-1, curOr | arr[i], arr)

            not_take = solve(i-1, curOr, arr)

            return
        
        n = len(nums)

        solve(n-1, 0, nums)

        # print(maxi,maxiCnt)

        return maxiCnt




