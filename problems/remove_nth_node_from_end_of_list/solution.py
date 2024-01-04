# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        
        dummy = head

        left_head = ListNode(0, next = head)        
        root = left_head

        len_list = 0
        while dummy:
            len_list += 1
            dummy = dummy.next

        
        for left in range(len_list):
            
            if left == len_list - n:
                if left_head.next and left_head.next.next:
                    left_head.next = left_head.next.next
                else:
                    left_head.next = None
                break
            else:
                left_head = left_head.next
        

        return root.next


     
        
        # return root.next






        