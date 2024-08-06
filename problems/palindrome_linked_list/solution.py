# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        # find middle node of the list
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # reverse second half of the list
        curr, prev = slow, None
        while curr:
            next_ = curr.next 
            curr.next = prev # reverse pointer
            prev = curr # move pointers
            curr = next_

        # Check palindrome
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        
        return True
                