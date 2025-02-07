class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:

        balls = {}

        colors = {}

        dist_cnt = 0

        n = len(queries)

        result = [0 for i in range(n)]

        i = 0
        
        for ball, color in queries:

            if ball in balls and color in colors:

                prev_color = balls[ball]

                if prev_color == color :

                    result[i] = dist_cnt

                    i += 1

                    continue

                # removing previous color
                colors[prev_color] -= 1
                
                # updating distinct cnt
                if colors[prev_color] == 0:

                    del colors[prev_color]

                    dist_cnt -= 1
                
                # increasing color cnt
                colors[color] += 1
                
                # coloring the current ball
                balls[ball] = color

            
            elif ball in balls and color not in colors:

                prev_color = balls[ball]

                # removing previous color
                colors[prev_color] -= 1

                # updating distinct cnt
                if colors[prev_color] == 0:

                    del colors[prev_color]

                    dist_cnt -= 1
                
                # adding color
                colors[color] = 1

                # updating distinct cnt
                dist_cnt += 1
                

                # coloring the ball
                balls[ball] = color

            elif ball not in balls and color in colors:

                # add this ball
                balls[ball] = color

                # increment color count
                colors[color] += 1

            elif ball not in balls and color not in colors:

                # add this ball
                balls[ball] = color

                # add this color

                colors[color] = 1

                dist_cnt += 1
            
            result[i] = dist_cnt

            i += 1
        
        return result