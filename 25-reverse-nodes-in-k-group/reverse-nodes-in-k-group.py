# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        # Collect values into list
        values = []
        curr = head
        while curr:
            values.append(curr.val)
            curr = curr.next

        n = len(values)

        # Reverse each complete group of k
        for start in range(0, n, k):
            if start + k <= n:
                values[start:start + k] = values[start:start + k][::-1]

        # Write values back to linked list
        curr = head
        for val in values:
            curr.val = val
            curr = curr.next

        return head