# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        
        curr = head
        linked_list_set = set()

        while curr:
            if curr.next in linked_list_set:
                return True
            linked_list_set.add(curr)
            curr = curr.next
        
        return False



        