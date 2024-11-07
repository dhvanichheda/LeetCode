# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy

        while l1 != None and l2 != None:
            new_node = ListNode()
            if l1.val < l2.val:
                new_node.val = l1.val 
                l1 = l1.next 
            else:
                new_node.val = l2.val 
                l2 = l2.next

            curr.next = new_node
            curr = curr.next 

        while l1 != None:
            new_node = ListNode(l1.val)
            curr.next = new_node 
            curr = curr.next 
            l1 = l1.next 

        while l2 != None:
            new_node = ListNode(l2.val)
            curr.next = new_node 
            curr = curr.next 
            l2 = l2.next 

        return dummy.next
            
        
        

        

