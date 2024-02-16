# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        dummy = ListNode(next=list1)
        curr = dummy
        count = 0
         
        while curr.next:
            if count == a:
                a_node = curr
            elif count == b+1:
                b_node = curr
                break
            curr = curr.next
            count += 1
        
        curr2 = list2
        while curr2.next:
            curr2 = curr2.next

        a_node.next = list2
        curr2.next = b_node.next    

        return dummy.next
        