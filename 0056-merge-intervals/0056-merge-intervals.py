'''
Logic - starting range of an interval should fall within ending range of another interval for them to overlap
1. Brute force O(n^2) - for each array, check all the other arrays that overlap 
2. Sort and compare O(nlogn) - sort the intervals by starting range, and then compare end of new interval to start of previous interval 
'''
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals 

        intervals.sort(key=lambda x: x[0])

        merged = []
        for l in intervals:
            if not merged or merged[-1][1] < l[0]:
                merged.append(l)
            else:
                merged[-1][1] = max([merged[-1][1], l[1]])
        
        return merged