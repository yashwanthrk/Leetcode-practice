# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        stack = [] 
        current = head

        while current:
            stack.append(current)
            current = current.next

        dummy = ListNode()
        current = dummy

        while stack:
            current.next = stack.pop()
            current = current.next
        
        current.next = None
        
        return dummy.next


        