class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ns = newInterval[0]
        ne = newInterval[1]
        res = []
        idx = 0
        while idx < len(intervals) and ns > intervals[idx][1]:
            res.append(intervals[idx])
            idx += 1
        
        while idx < len(intervals) and ne >= intervals[idx][0]:
            ns = min(intervals[idx][0], ns)
            ne = max(intervals[idx][1], ne)
            idx += 1
        res.append([ns, ne])

        while idx < len(intervals):
            res.append(intervals[idx])
            idx += 1

        return res
