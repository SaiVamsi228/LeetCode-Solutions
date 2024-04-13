class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        n = len(nums)

        post = []
        negt = []

        for num in nums:

            if num>0:
                post.append(num)
            
            else:
                negt.append(num)

        new_arr = []

        flag = True

        i = 0
        flag = True

        while i<n//2:

            if flag:

                new_arr.append(post[i])

                flag = False
            
            else:

                new_arr.append(negt[i])

                flag = True

                i+=1
        
        nums[:] = new_arr

        return nums