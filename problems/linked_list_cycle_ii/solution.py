# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not (head and head.next):
            return
            
        current = head
        seen = set()

        while current:
            if current in seen:
                return current
            else:
                seen.add(current)
            current = current.next
        return None