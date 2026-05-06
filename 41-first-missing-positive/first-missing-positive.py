class Solution(object):
    def firstMissingPositive(self, nums):
        nums.sort()
        expected = 1

        for i in range(len(nums)):
            # Skip negatives, zeros, and duplicates
            if nums[i] <= 0 or (i > 0 and nums[i] == nums[i - 1]):
                continue
            # If current number matches what we expect, move to next
            if nums[i] == expected:
                expected += 1
            else:
                # Gap found
                break

        return expected  