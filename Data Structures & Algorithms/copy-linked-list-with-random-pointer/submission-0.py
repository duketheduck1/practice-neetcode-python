"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        has = {None:None}
        curr = head
        while curr:
            node = Node(curr.val)
            has[curr] = node
            curr = curr.next

        curr = head
        while curr:
            has[curr].next = has.get(curr.next)
            has[curr].random = has.get(curr.random)
            curr = curr.next
        return has[head]
