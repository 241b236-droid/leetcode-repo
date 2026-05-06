class Solution(object):
    def searchRange(self, nums, target):
        first = -1
        last = -1

        # Find first occurrence
        for i in range(len(nums)):
            if nums[i] == target:
                first = i
                break

        # If target not found, no need to search for last
        if first == -1:
            return [-1, -1]

        # Find last occurrence
        for j in range(len(nums) - 1, -1, -1):
            if nums[j] == target:
                last = j
                break

        return [first, last]