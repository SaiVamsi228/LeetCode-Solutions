class Solution:
    def trap(self, height: List[int]) -> int:
        
        def get_abs_greatest_to_left_ind(height):

            agl = [-1 for i in range(n)]

            mx = -1

            for i in range(n):

                agl[i] = mx

                if mx == -1 or height[i] > height[mx]:

                    mx = i
            
            return agl
                

        def get_abs_greatest_to_right_ind(height):

            agr = [n for i in range(n)]

            mx = n

            for i in reversed(range(n)):

                agr[i] = mx

                if mx == n or height[i] > height[mx]:

                    mx = i 
            
            return agr
        
        
        n = len(height)

        water_trapped = 0

        agl = get_abs_greatest_to_left_ind(height)

        agr = get_abs_greatest_to_right_ind(height)

        print(agl,agr)

        for ind,h in enumerate(height):

            left_tallest_ind = agl[ind]

            right_tallest_ind = agr[ind]

            if left_tallest_ind == -1 or right_tallest_ind == n:

                water_trapped += 0
            
            else:

                min_height_building = min(height[left_tallest_ind],height[right_tallest_ind]) 

                if min_height_building < h:

                    water_trapped += 0

                else:
                    
                    water_trapped += min_height_building - h 

        return water_trapped