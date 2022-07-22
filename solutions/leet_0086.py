TITLE = 'Partition List'
'''
time: BigO(n)
space: BigO(n)

Results:
    Runtime: 57 ms, faster than 42.58%
    Memory Usage: 13.8 MB, less than 98.64%
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left, right = [], []
        
        while head:
            if head.val < x:
                left.append(head)
            else:
                right.append(head)
            head = head.next
                
        dummy = ListNode(None, None)
        curr = dummy
        for node in left + right:
            curr.next = node
            curr = curr.next
        curr.next = None
            
        return dummy.next