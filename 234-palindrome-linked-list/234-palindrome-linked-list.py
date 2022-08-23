# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        curr, prev = slow, None
        while curr:       
            curr.next, prev, curr = prev, curr, curr.next 
            
        while prev:
            if None in [head, prev]:
                return False
            if head.val != prev.val:
                return False
            head = head.next
            prev = prev.next
            
        return True