class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        curr1 = list1
        curr2 = list2

        dummy = ListNode()          # fixes 1, 2, 4: a real node to attach to
        ptr = dummy

        while curr1 and curr2:
            if curr1.val <= curr2.val:
                ptr.next = curr1
                curr1 = curr1.next
            else:
                ptr.next = curr2
                curr2 = curr2.next

            ptr = ptr.next          # move onto the node just attached

        ptr.next = curr1 or curr2   # fixes 3: attach the leftovers

        return dummy.next           # fixes 2: the head is right after dummy