# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import Optional

class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
# kth node from the end (the list is 1-indexed).

        
        curr = head
        count = 0
        while curr is not None:
            curr = curr.next
            count += 1



        p1 = head
        for _ in range(k - 1): 
            p1 = p1.next
            # print(p1.val)
        
        p2 = head
        for _ in range(count - k): 
            p2 = p2.next
            # print(p2.val)

        # Note that this approach only swaps the values of the nodes and not the nodes themselves. This means the links between the nodes remain unchanged.
        p1.val, p2.val = p2.val, p1.val

        return head

        
        