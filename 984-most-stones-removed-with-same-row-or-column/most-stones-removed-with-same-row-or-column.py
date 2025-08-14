class UnionFind:

    def __init__(self,n):

        self.parent = [i for i in range(n)]
        self.size = [1 for i in range(n)]
    
    def findUParent(self,node):

        if self.parent[node] == node:

            return node
        
        self.parent[node] = self.findUParent(self.parent[node])

        return self.parent[node]
    
    def unionBySize(self,u,v):

        up_u = self.findUParent(u)

        up_v = self.findUParent(v)

        size_up_u = self.size[up_u]

        size_up_v = self.size[up_v]

        if size_up_u <= size_up_v:

            self.parent[up_u] = up_v

            self.size[up_v] += self.size[up_u]
        
        else:

            self.parent[up_v] = up_u

            self.size[up_u] += self.size[up_v]

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        
        rows = cols = 0

        for r,c in stones:

            rows = max(rows,r+1)

            cols = max(cols,c+1)

        no_of_rows_and_cols = rows + cols
        
        uniq_r_and_cols = set()  

        uf = UnionFind(no_of_rows_and_cols)

        for r,c in stones:

            act_row, act_col = r, rows + c

            uniq_r_and_cols.add(act_row)

            uniq_r_and_cols.add(act_col)
            
            uf.unionBySize(act_row,act_col)
        
        single = 0

        for ele in uniq_r_and_cols:
            
            if uf.findUParent(ele) == ele:

                single += 1

        return len(stones) - single



            





