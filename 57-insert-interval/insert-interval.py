class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        cand = newInterval[:]
        ans = []

        flag = 0
        for i, interval in enumerate(intervals):
            s, e = interval

            if s < newInterval[0] and e > newInterval[1]:
                return intervals
            elif s < newInterval[0] and e < newInterval[0]:
                ans.append(interval)
            elif s < newInterval[0] and newInterval[0] <= e <= newInterval[1]:
                cand[0] = s
            elif newInterval[0] <= s <= newInterval[1] and e > newInterval[1]:
                cand[1] = e 
            elif s > newInterval[1] and e > newInterval[1]:
                ans.append(cand)
                flag = 1
                ans.extend(intervals[i:])
                break
        
        if not flag:
            ans.append(cand)
        
        return ans
            
            