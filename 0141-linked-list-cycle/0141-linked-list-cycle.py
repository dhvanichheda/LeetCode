# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head == None:
            return False 

        slow = ListNode(0)
        slow.next = head
        fast = head 

        while fast.next != None and fast.next.next != None:
            if slow != fast:
                slow = slow.next
                fast = fast.next.next
            else:
                return True

        return False 
