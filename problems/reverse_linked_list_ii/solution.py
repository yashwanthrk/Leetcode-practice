# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """


        # left = 2
        # right = 4

        # i: 1    2    3    4    5
        #    1 -> 2 -> 3 -> 4 -> 5

        pre_head = ListNode(-1, -1)
        pre_head.next = head

        prev_curr = pre_head
        curr = head

        # Calculate starting point
        for _ in range(left - 1):
        #    1 -> 2 -> 3 -> 4 -> 5
        #         ^
            prev_curr = prev_curr.next
            curr = curr.next
        
        # Reverse linked list
        # i: 1    2    3    4    5
        #    1 -> 2 -> 3 -> 4 -> 5
        #         ^ ITERATE 3 TIMES | 4 - 2 + 1
        prev = prev_curr
        for _ in range(right - left + 1):
            tmp = curr.next
            curr.next = prev
            prev = curr 
            curr = tmp

        # Re-attach nodes
        prev_curr.next.next = curr
        prev_curr.next = prev

        return pre_head.next

       