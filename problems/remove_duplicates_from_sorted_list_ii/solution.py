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

        unique_map = {}
        dummy  = head

        while head:
            if head.val in unique_map:
                unique_map[head.val] += 1
            else:
                unique_map[head.val] = 1
            head = head.next


        root = ListNode(0)
        pre_root = root

        while dummy:
            
            if unique_map[dummy.val] == 1:
                root.next = ListNode(dummy.val)
                root = root.next
            
            dummy = dummy.next

        return pre_root.next

            

