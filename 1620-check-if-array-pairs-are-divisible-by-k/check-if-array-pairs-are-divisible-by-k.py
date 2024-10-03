from collections import defaultdict
class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        
        if k == 1:

            return True

        mp = defaultdict(int)

        for ele in arr:

            rem = ele % k               
            
            mp[rem] += 1

        for ele in arr:

            rem = ele % k

            if rem == 0:

                if mp[rem] % 2 != 0:

                    return False #as we cannot form pair for the remaining one ele

            elif mp[rem] != mp[k-rem]:

                return False
            
        return True

         