# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        
        first_cp = -1
        last_cp = -1
        prev_cp = -1
        min_distance = float('inf')
        index = 0
        
        if not head or not head.next or not head.next.next:
            return [-1, -1]
        
        prev = head
        curr = head.next
        next = curr.next
        index = 1
        
        while next:
            if (curr.val > prev.val and curr.val > next.val) or (curr.val < prev.val and curr.val < next.val):
                if first_cp == -1:
                    first_cp = index
                else:
                    min_distance = min(min_distance, index - prev_cp)
                last_cp = index
                prev_cp = index
            
            prev = curr
            curr = next
            next = next.next
            index += 1
        
        if first_cp == last_cp:
            return [-1, -1]
        
        return [min_distance, last_cp - first_cp]
