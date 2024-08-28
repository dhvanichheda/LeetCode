'''
1. Store each node in a hash map and check if it appears again
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

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