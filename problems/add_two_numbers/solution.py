# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        dummy = ListNode()
        curr = dummy

        carry = 0

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            v3 = v1 + v2 + carry
            #  3342 + 465
            carry = v3 // 10
            v3 = v3 % 10

            curr.next = ListNode(v3)
            
            curr = curr.next 

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        
        return dummy.next
        
        # l1_str = ""
        # while l1:
        #     l1_str += str(l1.val)
        #     l1 = l1.next
        
        # l2_str = ""
        # while l2:
        #     l2_str += str(l2.val)
        #     l2 = l2.next


        # def reverse_string(s):
        #     return s[::-1]

        # l3_str = str(int(reverse_string(l1_str)) + int(reverse_string(l2_str)))

        # l3_str =  reverse_string(l3_str)
        
        # print(l3_str)

        # l3 = ListNode(int(l3_str[0]))
        # curr = l3
        # for index in range(1, len(l3_str)):
        #     node = ListNode(int(l3_str[index]))
        #     curr.next = node
        #     # Move the current pointer to the newly added node
        #     curr = node
        
        # return l3