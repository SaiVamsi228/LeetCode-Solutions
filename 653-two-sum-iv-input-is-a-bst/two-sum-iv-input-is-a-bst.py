# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):

        self.stack1 = []
        self.stack2 = []
    
    def pushAllLeft(self,node) -> None:
        while node:
            self.stack1.append(node)
            node = node.left

    def pushAllRight(self,node) -> None:
        while node:
            self.stack2.append(node)
            node = node.right
    
    def hasnext(self):
        if self.stack1:
            return True
        return False

    def next(self) -> TreeNode:
        if self.stack1:
            cur = self.stack1.pop()
            if cur.right :
                temp = cur.right
                self.pushAllLeft(temp)
            return cur.val
    
    def hasbefore(self):
        if self.stack2:
            return True
        return False

    def before(self) -> TreeNode:
        if self.stack2:
            cur = self.stack2.pop()
            if cur.left :
                temp = cur.left
                self.pushAllRight(temp)
            return cur.val

    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        
        if not root:

            return False
        
        self.pushAllLeft(root)
        self.pushAllRight(root)

        left_most , right_most = self.next(), self.before()

        while True and left_most != right_most:

            if left_most + right_most >k:
                if self.hasbefore():
                    right_most = self.before()
                else:
                    return False
            
            elif left_most + right_most < k :
                if self.hasnext():
                    left_most = self.next()
                else:
                    return False
                    
            else:
                return True
        
        return False