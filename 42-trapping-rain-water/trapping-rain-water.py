class Solution:
    def trap(self, height: List[int]) -> int:
        
        water_trapped = 0

        n = len(height)

        left , right = 0, n - 1

        max_left, max_right = 0,0

        while left <= right:

            if height[left] <= height[right]:
                
                if max_left <= height[left]:

                    # we cant store any water

                    water_trapped += 0

                    max_left = height[left]

                else:

                    # water store depends on max_left

                    water_trapped += max_left - height[left] 
                
                left += 1
            
            elif height[left] > height[right]:

                if height[right] >= max_right:

                    # no water is trapped

                    water_trapped += 0

                    max_right = height[right]
                
                else:

                    # water trapped depends on max_right

                    water_trapped += max_right - height[right] 
                
                right -= 1

        return water_trapped

                

