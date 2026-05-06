class Solution(object):
    def combinationSum2(self, candidates, target):
        candidates.sort()
        result = []
        self.backtrack(candidates, 0, target, [], result)
        return result

    def backtrack(self, candidates, start, remaining, current, result):
        if remaining == 0:
            result.append(list(current))
            return
        for i in range(start, len(candidates)):
            # Prune: all subsequent candidates are larger, so stop here
            if candidates[i] > remaining:
                break
            # Skip duplicates at the same decision level
            if i > start and candidates[i] == candidates[i - 1]:
                continue

            current.append(candidates[i])
            self.backtrack(candidates, i + 1, remaining - candidates[i], current, result)
            current.pop()