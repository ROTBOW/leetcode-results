# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    
    def search(self, node) -> bool:
        if node.val == 1:
            return True
        if node.left and self.search(node.left):
            return True
        elif node.right and self.search(node.right):
            return True
        
        return False
    
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = deque([root])
        
        while queue:
            node = queue.popleft()
            
            if node.left and self.search(node.left):
                queue.append(node.left)
            else:
                node.left = None
            if node.right and self.search(node.right):
                queue.append(node.right)
            else:
                node.right = None
                
        if root.val == 0 and root.left == None and root.right == None:
            return None
        
        return root
                