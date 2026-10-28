class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        main_ptr = head
        lagging_ptr = head

        head_ptr = ListNode()
        head_ptr.next = head
        lagging_ptr_minus_one = head_ptr

        counter = 0
        while main_ptr:

            if counter < n:                                          # phase 1: open the gap
                main_ptr = main_ptr.next
                counter += 1

            else:                                                    # CHANGE 1: else, not a separate if
                main_ptr = main_ptr.next                             # phase 2: all three move together
                lagging_ptr = lagging_ptr.next
                lagging_ptr_minus_one = lagging_ptr_minus_one.next   # CHANGE 2: moved here

        lagging_ptr_minus_one.next = lagging_ptr.next
        return head_ptr.next                                         # CHANGE 3: .next