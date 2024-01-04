# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if not head:
            return head

        dummy = ListNode(head.val)
        root = dummy
        unique_elements = set([head.val])

        while head and head.next:
            if head.next.val in unique_elements:
                head = head.next
            else:
                unique_elements.add(head.next.val)
                dummy.next = ListNode(head.next.val)
                dummy = dummy.next
                head = head.next

        
        return root



        