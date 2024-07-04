# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy
        sum_val = 0
        
        head = head.next
        
        while head:
            if head.val == 0:
                # When we encounter a zero, we finalize the sum and reset the counter
                current.next = ListNode(sum_val)
                current = current.next
                sum_val = 0
            else:
                sum_val += head.val
            head = head.next
        
        return dummy.next
