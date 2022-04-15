TITLE = 'Merge k Sorted Lists'
'''
time: BigO(n log n)
space: BigO(n)
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from queue import PriorityQueue as pq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists: return None
        head = ListNode(None)
        curr = head
        queue = pq()
        
        for idx, node in enumerate(lists):
            if node:
                queue.put((node.val, idx, node))    
        while queue.qsize() > 0:
            val, idx, node = queue.get()
            curr.next = node
            curr = curr.next
            if node.next:
                queue.put((node.next.val, idx, node.next))
        return head.next
        