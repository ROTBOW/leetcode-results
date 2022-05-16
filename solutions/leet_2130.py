TITLE = 'Maximum Twin Sum of a Linked List'
'''
time: BigO(n)
space: BigO(1)

Results:
    Runtime: 910 ms, faster than 96.26%
    Memory Usage: 45 MB, less than 84.71%
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
        curr, prev = slow, None
        while curr:       
            curr.next, prev, curr = prev, curr, curr.next 
            
        maximun = float('-inf')
        while prev:
            maximun = max(maximun, prev.val + head.val)
            prev = prev.next
            head = head.next
        return maximun
        