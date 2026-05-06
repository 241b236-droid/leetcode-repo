class Solution(object):
    def threeSum(self, nums):
        result = []
        nums.sort()
        n = len(nums)

        for i in range(n - 2):
        
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            target = -nums[i]
            seen = set()

            j = i + 1
            while j < n:
                complement = target - nums[j]

                if complement in seen:
                    result.append([nums[i], complement, nums[j]])
                
                    while j + 1 < n and nums[j] == nums[j + 1]:
                        j += 1
                seen.add(nums[j])
                j += 1

        return result