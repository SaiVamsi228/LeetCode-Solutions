from heapq import heapify, heappush, heappop
class Solution:
    def candy(self, ratings: List[int]) -> int:
        
        n = len(ratings)

        if n == 1:

            return 1
            
        candies = [1 for i in range(n)]

        min_hp = [] # (rating,ind)

        heapify(min_hp)

        for ind in range(n):
            
            rating = ratings[ind]

            heappush(min_hp,(rating,ind))

        min_candies_req = n

        while min_hp:

            rating,ind = heappop(min_hp)

            if ind == 0 :

                if ratings[0] > ratings[1]:

                    candies[ind] = candies[1] + 1 
            
            elif ind == n - 1:

                if ratings[n-1] > ratings[n-2]:

                    candies[ind] = candies[n-2] + 1
            
            else:

                prev, after = candies[ind-1], candies[ind+1]

                mini = 0

                if ratings[ind] == ratings[ind-1] and ratings[ind] == ratings[ind+1]:

                    candies[ind] = after
                
                if ratings[ind] > ratings[ind+1]:

                    mini = candies[ind+1] + 1

                    candies[ind] = mini
                
                if ratings[ind] > ratings[ind-1]:

                    mini = max(candies[ind-1]+1,mini)
                
                    candies[ind] = mini
                
            min_candies_req += candies[ind] - 1
        
        return min_candies_req


                