# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        cnt = 0

        def get_kth_smallest(root):
            
            nonlocal cnt

            if not root:

                return None
            
            left_found = get_kth_smallest(root.left)

            cnt += 1

            if cnt == k:

                return root
            
            right_found = get_kth_smallest(root.right)

            return left_found or right_found
        
        return get_kth_smallest(root).val