class Solution(object):
    def merge(self, intervals):
        # Sort by start time
        intervals.sort(key=lambda x: x[0])

        result = [intervals[0]]

        for i in range(1, len(intervals)):
            last = result[-1]

            if intervals[i][0] <= last[1]:
                # Overlapping: extend the end of the last merged interval
                last[1] = max(last[1], intervals[i][1])
            else:
                # No overlap: start a new interval
                result.append(intervals[i])

        return result