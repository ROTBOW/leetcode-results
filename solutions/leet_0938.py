TITLE = 'Range Sum Of BST'
'''
time: BigO(n)
space: BigO(n)

Results:
    Runtime: 334 ms, faster than 52.85%
    Memory Usage: 23.3 MB, less than 8.24%
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        queue = deque([root])
        answer = 0
        
        while queue:
            node = queue.popleft()
            
            if low <= node.val <= high:
                answer += node.val
                
            if node.left:
                queue.append(node.left)
                
            if node.right:
                queue.append(node.right)
                
        return answer