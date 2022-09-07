# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None:
            return None
        
        nodes = deque()
        while head:
            nodes.append(head)
            head = head.next
            
        k = k % len(nodes)
        for _ in range(k): nodes.appendleft(nodes.pop())
            
        dummy = ListNode()
        
        node = dummy
        nodes.append(None)
        for next_node in nodes:
            node.next = next_node
            node = next_node
            
        return dummy.next