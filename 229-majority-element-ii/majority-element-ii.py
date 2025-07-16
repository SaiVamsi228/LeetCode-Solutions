class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        f1,f2 = 0, 0

        e1, e2 = None, None

        n = len(nums)

        for i in range(n):

            if f1 == 0 and nums[i] != e2:

                f1 = 1

                e1 = nums[i]
            
            elif f2 == 0 and nums[i] != e1:

                f2 = 1

                e2 = nums[i]

            elif nums[i] == e1 :

                f1 += 1
            
            elif nums[i] == e2:

                f2 += 1
            
            else:

                f1 -= 1

                f2 -= 1
        
        cnt1, cnt2 = 0, 0

        for i in range(n):

            if nums[i] == e1 :

                cnt1 += 1
            
            if nums[i] == e2:

                cnt2 += 1
        
        if cnt1 > n//3 and cnt2 > n//3:

            return [e1,e2]
        
        elif cnt1 > n//3:

            return [e1]
        
        elif cnt2 > n//3:
            
            return [e2]
        
        return []




            
            
