# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        list3  = ListNode()
        tail = list3
        while list1 and list2:
            temp1 = list1
            temp2 = list2
            if list1.val <= list2.val:
                tail.next = temp1
                list1 = list1.next
            else:
                tail.next = temp2
                list2 = list2.next

            tail = tail.next

        if list1:
            tail.next = list1
        
        if list2:
            tail.next = list2
        
        return list3.next
                







        