TITLE = 'Merge Two Sorted Lists'
'''
leet_0021 asks us to merge two sorted linked-lists

time: BigO(n)
space: BigO(n)

Results:
    Runtime: 70 ms, faster than 15.40%
    Memory Usage: 13.9 MB, less than 34.56%
'''



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(None)
        curr = head      
        
        while list1 or list2:
            val1 = list1.val if list1 else float('inf')
            val2 = list2.val if list2 else float('inf')
            next_node = list1 if val1 < val2 else list2
            curr.next = next_node
            curr = curr.next
            if val1 < val2:
                list1 = list1.next
            else:
                list2 = list2.next
                
        return head.next