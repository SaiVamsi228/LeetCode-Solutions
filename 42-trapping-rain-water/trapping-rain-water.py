class Solution:
    def trap(self, height: List[int]) -> int:

        n = len(height)
        
        right_max = [0 for i in range(n)]

        left_max = [0 for i in range(n)]

        maxi = 0

        for i in range(n):

            if height[i] > maxi :

                maxi = height[i]

            left_max[i] = maxi
        
        maxi = 0

        for i in reversed(range(n)):

            if height[i] > maxi:

                maxi = height[i]
            
            right_max[i] = maxi
        
        max_water = [0 for i in range(n)]

        for i in range(n):

            left_tallest = left_max[i]

            right_tallest = right_max[i]

            max_units_possible = min(left_tallest, right_tallest)

            actual_water_filled = max_units_possible - height[i]
            max_water[i] = actual_water_filled
        
        return sum(max_water)
