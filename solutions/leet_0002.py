TITLE = 'add two numbers'
'''
leet_0002 is asking to add numbers in reverse, they are also stored in a linked-list.
I wanted to keep the data structure so I went with doing the math backwards.

time: BigO(n) #where n is the lenght of the longest linked-list
space: BigO(n)

Results:
    Runtime: 64 ms, faster than 96.95%
    Memory Usage: 13.8 MB, less than 88.37%
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(None)
        curr = head
        carry = 0
        
        while l1 or l2:
            num1 = l1.val if l1 else 0
            num2 = l2.val if l2 else 0
            new_num = num1 + num2
            if carry != 0:
                new_num += carry
                carry = 0
            if new_num > 9:
                curr.next = ListNode(new_num % 10)
                carry = new_num // 10
            else:
                curr.next = ListNode(new_num)
            curr = curr.next
                
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if carry != 0:
            curr.next = ListNode(carry)
                
        return head.next