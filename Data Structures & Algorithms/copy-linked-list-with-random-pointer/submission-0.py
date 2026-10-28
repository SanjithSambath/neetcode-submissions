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
        old_to_new = {None: None}

        # Pass 1: create a copy of every node (values only, no pointers yet)
        curr = head
        while curr:
            old_to_new[curr] = Node(curr.val)
            curr = curr.next

        # Pass 2: wire next and random through the map
        curr = head # from beginning again
        while curr:
            copy = old_to_new[curr] # ptr 
            copy.next = old_to_new[curr.next] # alr indexed, assigns ptr 
            copy.random = old_to_new[curr.random] # alr indexed, assigns ptr
            curr = curr.next

        return old_to_new[head]