import math
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def getDays(capacity):

            total_days_req = 0
            
            n = len(weights)

            cur_cap = 0

            for i in range(n):

                cur_cap += weights[i]

                if cur_cap > capacity :

                    total_days_req += 1

                    cur_cap = weights[i]

                if i == n - 1:

                    if cur_cap :
                        
                        total_days_req += 1
        
            return total_days_req
        
        n = len(weights)

        left = max(weights)

        right = sum(weights)

        mn = right

        while left <= right:

            cap = (left + right)//2

            days_req = getDays(cap)

            print(cap,days_req)

            if days_req <= days:

                mn = cap

                # we want minimum weight capacity of the ship

                right = cap - 1
            
            elif days_req > days:

                left = cap + 1
        
        return mn