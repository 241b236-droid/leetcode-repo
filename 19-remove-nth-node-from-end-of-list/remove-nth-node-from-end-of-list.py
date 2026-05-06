
class Solution(object):
    def removeNthFromEnd(self, head, n):
        # Dummy node handles the edge case of removing the head
        dummy = ListNode(0, head)
        slow = dummy
        fast = dummy

        # Advance fast by n + 1 steps to create the gap
        for _ in range(n + 1):
            fast = fast.next

        # Move both pointers until fast reaches the end
        while fast:
            slow = slow.next
            fast = fast.next

        # slow is now the node before the target, skip the target
        slow.next = slow.next.next

        return dummy.next