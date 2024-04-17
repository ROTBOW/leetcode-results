# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import heapq
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        stack = [(root, [root.val])]
        words = list()
        
        while stack:
            node, curr_path = stack.pop()
            
            if not node.left and not node.right:
                heapq.heappush(
                    words, 
                    ''.join(chr(x+97) for x in curr_path[::-1])
                )
                    
            
            if node.left:
                stack.append(
                    (
                        node.left,
                        curr_path + [node.left.val]
                    )
                )
            if node.right:
                stack.append(
                    (
                        node.right,
                        curr_path + [node.right.val]
                    )
                )

        return heapq.heappop(words)