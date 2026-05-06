class Solution(object):
    def jump(self, nums):
        n = len(nums)
        jumps = 0
        current_end = 0
        farthest = 0

        # Process indices 0 to n-2; we don't need to jump from the last index
        for i in range(n - 1):
            farthest = max(farthest, i + nums[i])

            # Reached the end of the current BFS level
            if i == current_end:
                jumps += 1
                current_end = farthest

                # Early exit if we can already reach the end
                if current_end >= n - 1:
                    break

        return jumps