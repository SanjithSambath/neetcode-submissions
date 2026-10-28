# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        middle, fast = head, head.next
        while fast and fast.next:
            middle = middle.next
            fast = fast.next.next

        second_half = middle.next
        
        prev = None
        middle.next = None

        while second_half:
            tmp = second_half.next
            second_half.next = prev
            prev = second_half
            second_half = tmp # reverse linked list

        first, second_half = head, prev

        while second_half: # weave code
            tmp1, tmp2 = first.next, second_half.next
            first.next = second_half
            second_half.next = tmp1
            first, second_half = tmp1, tmp2
