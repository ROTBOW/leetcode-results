# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        queue = deque([[root, 0]])
        res = dict()
        
        while queue:
            node, lvl = queue.popleft()

            if lvl not in res:
                res[lvl] = node.val
            else:
                res[lvl] = max(res[lvl], node.val)

            if node.left:
                queue.append([node.left, lvl+1])

            if node.right:
                queue.append([node.right, lvl+1])

        return [res[x] for x in range(len(res))]