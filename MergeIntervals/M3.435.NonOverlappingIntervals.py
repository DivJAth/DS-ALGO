# Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

# Example 1:
# Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
# Output: 1
# Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.

# Example 2:
# Input: intervals = [[1,2],[1,2],[1,2]]
# Output: 2
# Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.

# Example 3:
# Input: intervals = [[1,2],[2,3]]
# Output: 0
# Explanation: You don't need to remove any of the intervals since they're already non-overlapping.

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[0])
        i = 0
        j = 1
        cnt = 0
        while j < len(intervals):
            print(i, j, intervals[i], intervals[j], intervals)
            if intervals[i][1] > intervals[j][0]:
                if intervals[i][1] > intervals[j][1]: # case 2: interval[prev]completely overlaps[cur]. We choosing the smaller interval as the larger one can interset with more intervals. Hence we want to remove the larger interval.
                    i = j 
                # case 3: b1>a2 [a1,b1], [a2,b2] prev stays in the same place cur moves forward.
                cnt+=1
            else:
                i = j # case 1
            j += 1
        return cnt

# A simpler approach sort on endpoint then is to check if there exists no overlap them move the second pointer forward
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[1])
        i = 0
        j = 1
        cnt = 1
        while j < len(intervals):
            if intervals[i][1] <= intervals[j][0]:
                i = j
                cnt+=1
            j += 1
        return len(intervals) - cnt