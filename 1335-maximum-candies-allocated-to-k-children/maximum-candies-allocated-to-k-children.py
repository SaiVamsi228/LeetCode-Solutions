class Solution:
    def getChildrenPossible(self,candyCount,k,n,candies):

        noOfChildren = 0

        i = n - 1

        while i>=0 and candies[i] >= candyCount and noOfChildren < k:

            noOfChildren += candies[i] // candyCount
            
            i -= 1

        
        return noOfChildren

    def maximumCandies(self, candies: List[int], k: int) -> int:
        
        n = len(candies)

        maxCandy = 0

        candies.sort()

        mini = candies[0]

        low = 1

        high = candies[-1]

        while low <= high :

            candyCount = (low + high )//2

            if self.getChildrenPossible(candyCount,k,n,candies) >= k :

                maxCandy = candyCount

                low = candyCount + 1
            
            else:

                high = candyCount - 1
        
        return maxCandy
                


