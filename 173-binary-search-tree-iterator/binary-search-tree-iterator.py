# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):

        self.st = []

        temp = root

        while temp :

            self.st.append(temp)

            temp = temp.left
        

    def next(self) -> int:

        if self.hasNext():

            nxt = self.st.pop()

            if nxt.right:

                temp = nxt.right

                while temp :

                    self.st.append(temp)

                    temp = temp.left
                
            return nxt.val
        
        return None
            
        

    def hasNext(self) -> bool:
        
        return len(self.st) != 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()