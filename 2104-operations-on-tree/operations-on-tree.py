from collections import deque
class LockingTree:

    def __init__(self, parent: List[int]):
        
        self.parent = parent

        self.children = [[] for _ in range(len(parent))]

        for child in range(len(parent)):

            par = parent[child]

            if par != -1:

                self.children[par].append(child)
        
        self.locked = [-1 for i in range(len(parent))]

    def lock(self, num: int, user: int) -> bool:
    
        if self.locked[num] != -1:

            return False
        
        self.locked[num] = user

        return True

    def unlock(self, num: int, user: int) -> bool:
        
        if self.locked[num] == -1 or self.locked[num] != user:

            return False

        self.locked[num] = -1

        return True
        
        

    def upgrade(self, num: int, user: int) -> bool:
        
        # 1. checking if current node is locked
        if self.locked[num] != -1:

            return False
        
        # 2. checking if ancestors are locked

        temp = num
        
        while temp != 0:
            if self.locked[temp] != -1:
                return False
            temp = self.parent[temp]

        if self.locked[temp] != -1:

            return False
            
        # 3. checking if atleast one descendant is locked if so unlock all

        atleast_one_locked = False

        q = deque()

        q.append(num)

        while q :

            node = q.popleft()

            for child in self.children[node]:

                if self.locked[child] != -1:

                    atleast_one_locked = True

                    self.locked[child] = -1
                
                q.append(child)

        if atleast_one_locked :

            self.locked[num] = user
        
            return True
        
        return False



# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)