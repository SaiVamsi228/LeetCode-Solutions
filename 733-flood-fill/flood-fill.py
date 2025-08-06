from collections import deque
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        q = deque()

        visited = set()

        q.append((sr,sc))

        visited.add((sr,sc))

        m = len(image)

        n = len(image[0])

        initial_color = image[sr][sc]

        image[sr][sc] = color

        dr = [0,0,1,-1]

        dc = [1,-1,0,0]

        def isValid(row, col, m , n ):

            return 0 <= row < m and 0 <= col < n 

        while q:

            r,c = q.popleft()

            for i in range(4):

                new_row, new_col = r + dr[i], c + dc[i]

                if isValid(new_row,new_col,m,n):

                    if (new_row,new_col) not in visited:

                        visited.add((new_row,new_col))

                        if image[new_row][new_col] == initial_color:
                            
                            image[new_row][new_col] = color

                            q.append((new_row,new_col))
        
        return image


                    