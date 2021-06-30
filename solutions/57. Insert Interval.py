class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        newIntervals = []
        
        
        newIntervals.append(newInterval)
        
        for interval in intervals:
            
            if(interval[1] < newIntervals[-1][0]):
                backup = newIntervals[-1]
                newIntervals[-1] = interval
                newIntervals.append(backup)
            
            elif(interval[0] <= newIntervals[-1][1]):
                newIntervals[-1][0] = min(interval[0], newIntervals[-1][0])
                newIntervals[-1][1] = max(interval[1], newIntervals[-1][1])
            
            else:
                newIntervals.append(interval)
        return newIntervals
