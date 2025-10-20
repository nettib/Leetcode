class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        comb = []

        def backtrack(start, combSum):
            if combSum == target:
                res.append(comb.copy())
                return
            
            if combSum > target:
                return
            
            for i in range(start, len(candidates)):
                comb.append(candidates[i])
                combSum += candidates[i]
                backtrack(i, combSum)
                val = comb.pop()
                combSum -= val
        
        backtrack(0, 0)
        return res
        