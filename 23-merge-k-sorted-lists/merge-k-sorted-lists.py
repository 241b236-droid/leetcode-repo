# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):

        values = []

        # Collect all values from every list
        for node in lists:
            while node:
                values.append(node.val)
                node = node.next

        # Sort all values
        values.sort()

        # Build the merged linked list
        dummy = ListNode(0)
        current = dummy
        for val in values:
            current.next = ListNode(val)
            current = current.next

        return dummy.next
        