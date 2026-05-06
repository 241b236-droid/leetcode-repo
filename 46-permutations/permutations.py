class Solution(object):
    def permute(self, nums):
        result = []

        def backtrack(index):
            # All positions filled, add a copy of the current arrangement
            if index == len(nums):
                result.append(nums[:])
                return
            # Try each available element (from index onward) at the current position
            for i in range(index, len(nums)):
                nums[index], nums[i] = nums[i], nums[index]
                backtrack(index + 1)
                nums[index], nums[i] = nums[i], nums[index]  # Swap back to restore

        backtrack(0)
        return result