'''
1. Store the numbers in reverse order in a string. 
2. Convert the string numbers into integer (in non-reversed order)
3. Add the numbers, convert to string (in reversed order) and then create linked list 
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1_str = num2_str = ""
        while l1 != None:
            num1_str += str(l1.val)
            l1 = l1.next
        
        while l2 != None:
            num2_str += str(l2.val) 
            l2 = l2.next
        

        if num1_str == num2_str == "0":
            return ListNode()

        num1 = self.reversed_int(num1_str)
        num2 = self.reversed_int(num2_str)
        num_sum = num1 + num2

        pre_head = ListNode(-1)
        curr = pre_head
        while num_sum != 0:
            i = num_sum % 10
            num_sum = num_sum//10
            curr.next = ListNode(i)
            curr = curr.next

        return pre_head.next


        
    def reversed_int(self, num_str: str) -> int:
        str_len = len(num_str)
        tens_place = str_len - 1
        result = 0 
        for c in reversed(num_str):
            result += int(c) * (10 ** tens_place)
            tens_place -= 1

        return result