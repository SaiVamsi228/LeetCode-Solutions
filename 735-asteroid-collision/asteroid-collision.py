class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        stack = []

        for asteroid in asteroids:

            # asteroid moving right

            if asteroid > 0 : 

                stack.append(asteroid)

            # asteroid moving left
            
            # no asteroids on left

            elif not stack:

                stack.append(asteroid)
            
            # some exist on the left
            
            elif stack :

                # the immediate left one is also moving left

                if stack[-1] < 0:

                    stack.append(asteroid)
                
                # the immediate left one is moving right

                # opp dir collision should occur
                else:
                    # the left one is bigger => my asteroid explodes

                    if abs(stack[-1]) > abs(asteroid):

                        continue
                    
                    # if left one is smaller
                    
                    elif abs(stack[-1]) <= abs(asteroid):

                        # while left is moving right and is smaller than my current

                        # => keep exploding left ones

                        while stack and stack[-1] > 0 and abs(stack[-1]) < abs(asteroid):

                            stack.pop()
                        
                        # if left one is moving right and same size => both must explode
                        if stack and stack[-1] > 0 and abs(stack[-1]) == abs(asteroid):

                            stack.pop()

                        # if left is moving right and left is bigger => my current one explodes
                        elif stack and stack[-1] > 0 and abs(stack[-1]) > abs(asteroid):

                            continue
                        
                        # if left is moving left 
                        else:
                            
                            stack.append(asteroid)
                
        return stack 


        