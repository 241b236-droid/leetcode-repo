class Solution(object):
    def groupAnagrams(self, strs):
        groups = {}

        for s in strs:
            # Count character frequencies and use as a hashable key
            freq = [0] * 26
            for c in s:
                freq[ord(c) - ord('a')] += 1

            # Tuples are hashable in Python, so use directly as key
            key = tuple(freq)

            if key not in groups:
                groups[key] = []
            groups[key].append(s)

        return list(groups.values()) 