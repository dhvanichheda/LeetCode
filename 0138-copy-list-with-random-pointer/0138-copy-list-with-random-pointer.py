"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def __init__(self):
        self.visited = {}

    def getClonedNode(self, node: 'Optional[Node]') -> 'Optional[Node]':
        if node:
            if node not in self.visited:
                self.visited[node] = Node(node.val)

            return self.visited[node]

        return node


    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head 
        
        clone_head = self.getClonedNode(head)
        curr = clone_head
        
        while head != None:
            curr.next = self.getClonedNode(head.next)
            curr.random = self.getClonedNode(head.random)

            curr = curr.next 
            head = head.next

        return clone_head 




        

        

