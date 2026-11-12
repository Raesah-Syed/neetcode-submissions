class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key=lambda x:x[0])
        prev_end=float('-inf')
        c=0

        for i in range(len(intervals)):

            if prev_end>intervals[i][0]:
                c+=1
                prev_end=min(prev_end,intervals[i][1])
            else:
                prev_end=intervals[i][1]
        
        return c


