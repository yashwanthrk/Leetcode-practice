# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
    

        if head is None:
            return None

        dummy = ListNode(0)
        last = dummy

        seen = set()
        while head:
            if head.val not in seen:
                seen.add(head.val)

                # Create a new node with the value
                last.next = ListNode(head.val)  

                last = last.next 

            head = head.next
        
        return dummy.next


