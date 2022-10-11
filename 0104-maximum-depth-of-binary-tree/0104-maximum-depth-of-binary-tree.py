# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        ans = 0
        
        def dig(node, depth=0):
            nonlocal ans
            if not node:
                return 0
            
            left, right = dig(node.left, depth+1), dig(node.right, depth+1)
            
            ans = max(ans, depth)
            
        if dig(root) == 0:
            return 0
        
        return ans + 1