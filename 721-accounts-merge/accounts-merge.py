class unionFind:
    def __init__(self, n):

        self.parent = [ i for i in range(n)]

        self.size = [ 1 for i in range(n)]

        self.rank = [0 for i in range(n)]

    def findUPar(self, v):

        if self.parent[v] == v:

            return v

        self.parent[v] = self.findUPar(self.parent[v])

        return self.parent[v] 

    def unionByRank(self, u, v):

        up_u = self.findUPar(u)

        up_v = self.findUPar(v)

        rank_up_u = self.parent[up_u]

        rank_up_v = self.parent[up_v]

        if rank_up_u < rank_up_v:

            self.parent[up_u] = up_v
        
        elif rank_up_u > rank_up_v:

            self.parent[up_v] = up_u
        
        else:

            self.parent[up_u] = up_v

            self.rank[up_u] += 1
    
    def unionBySize(self, u, v):

        up_u = self.findUPar(u)

        up_v = self.findUPar(v)

        size_up_u = self.size[up_u]

        size_up_v = self.size[up_v]

        if size_up_u < size_up_v :

            self.parent[up_u] = up_v

            self.size[up_v] += self.size[up_u]

        elif size_up_u > size_up_v :

            self.parent[up_v] = up_u

            self.size[up_u] += self.size[up_v]
        
        else:
            
            self.parent[up_v] = up_u

            self.size[up_u] += self.size[up_v]

class Solution:
    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:

        ds = unionFind(10000)

        n = len(accounts)

        uniqMails = {}

        for i,acc in enumerate(accounts):

            for j in range(1,len(acc)):

                email = acc[j]

                if email in uniqMails:

                    ds.unionBySize(i, uniqMails[email])
                
                else:

                    uniqMails[email] = i
        
        ans = [[] for i in range(n)]

        accNames = ["" for i in range(n)]

        for mail, ind in uniqMails.items():

            up_ind = ds.findUPar(ind)

            if len(ans[up_ind]) == 0:

                accNames[up_ind] = accounts[ind][0]

            ans[up_ind].append(mail)

        temp = []
        
        for ind,acc in enumerate(ans):

            if acc :

                acc.sort()

                temp.append([accNames[ind]]  + acc)
                
        return temp