class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        newArr = []
        i = 0
        while i < len(intervals):
            if newInterval[1] < intervals[i][0]:
                newArr.append(newInterval)
                return newArr + intervals[i:]
            elif intervals[i][1] < newInterval[0]:
                newArr.append(intervals[i])
                i += 1
            else:
                newInterval = [
                    min(newInterval[0], intervals[i][0]),
                    max(newInterval[1], intervals[i][1])
                ]
                i += 1
        return newArr + [newInterval]