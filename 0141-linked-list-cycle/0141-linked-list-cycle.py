'''
1. Store each node in a hash map and check if it appears again
2. Fast and slow runner 
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

'''
#Approach 1
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        node_set = set()

        while head != None:
            if head in node_set:
                return True 
            else:
                node_set.add(head)
                head = head.next

        return False 
'''

#Approach 2 
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None:
            return False

        slow = head
        fast = head.next

        while fast != slow:
            if fast is None or fast.next is None:
                return False
            
            slow = slow.next
            fast = fast.next.next

        return True 