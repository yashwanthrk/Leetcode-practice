# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:


        # find lenth of list
        curr = head
        
        list_size = 0
        while curr is not None:
            curr = curr.next
            list_size += 1

        if n == list_size:
            return head.next


        curr =  head
        # Iterate through the list until one node before the node to be removed
        for index in range(1, list_size - n):
             # Start from 1 because we are already at the head
            curr = curr.next
          
        
        curr.next = curr.next.next
        # Returning head ensures that the caller has a reference to the beginning of the modified list.
        return head

        # In summary, always return head (or head.next if removing the head node) because you want to return the start of the modified list, not a pointer from somewhere in the middle.




