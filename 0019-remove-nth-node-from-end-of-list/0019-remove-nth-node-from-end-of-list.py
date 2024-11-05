# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        list_len = 0
        while curr.next != None:
            list_len += 1
            curr = curr.next

        list_len += 1
        traverse_len = list_len - n - 1
        curr = head
        if traverse_len > 0:
            for _ in range(list_len-n-1):
                curr = curr.next
            curr.next = curr.next.next
        elif traverse_len == 0:
            if curr.next.next != None:
                curr.next = curr.next.next
            else:
                curr.next = None
        else:
            head = head.next

        return head
