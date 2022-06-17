TITLE = 'Reverse Linked List'
'''
time: BigO(n)
space: BigO(1)

Results:
    Runtime: 74 ms, faster than 10.42%
    Memory Usage: 15.5 MB, less than 27.96%
'''
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head:
            curr, head, curr.next = head, head.next, prev
            prev = curr
        return prev