class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        st = []

        n = len(asteroids)

        for i in range(n):

            curr = asteroids[i]

            if not st:

                st.append(curr)
            
            elif st and ((st[-1] > 0 and curr > 0 ) or (st[-1] < 0 and curr < 0) or (st[-1] < 0 and curr > 0)):
                # same dir no collision

                st.append(curr)

            elif curr < 0 and st and st[-1] > 0 :
                
                isCurrDes = False

                while st and st[-1] > 0 and abs(st[-1]) <= abs(curr):
                    
                    if abs(st[-1]) == abs(curr):

                        isCurrDes = True

                        # can destroy only one of same size

                        st.pop()

                        break

                    st.pop()

                if st:

                    if st[-1] > 0 and abs(st[-1]) > abs(curr):

                        isCurrDes = True
                
                if not isCurrDes:

                    st.append(curr)
        
        return st
            


            
            
                
            
        return st
