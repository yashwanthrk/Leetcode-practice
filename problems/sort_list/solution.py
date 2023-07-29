# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        # get the mid point of the linked list
        slow = fast = head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None
        
        # recursively split and merge
        left = self.sortList(head)
        right = self.sortList(slow)


        return self.merge(left, right)

    def merge(self, n1: ListNode, n2: ListNode) -> ListNode:
        dummy = ListNode(0)
        
        temp = dummy

        while n1 and n2:
            if n1.val < n2.val:
                temp.next = n1
                n1 = n1.next
            else:
                temp.next = n2
                n2 = n2.next
            temp = temp.next

        # while n1:
        #     temp.next = n1
        #     temp = temp.next
        #     n1 =n1.next

        # while n2:
        #     temp.next = n2
        #     temp = temp.next
        #     n2 =n2.next

        if n1:
            temp.next = n1
        elif n2:
            temp.next = n2

        return dummy.next

        # just returning dummy will be - That's why it's crucial to return dummy.next instead of dummy. The .next essentially skips the dummy node and points to the actual head of the sorted linked list.
        # outptut just for returning dummy [0,0,0,1,2,3,4]

