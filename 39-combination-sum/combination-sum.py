class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(i, path, total):
            if total == target:
                res.append(path[:])
                return
            if total > target or i == len(candidates):
                return

            path.append(candidates[i])
            backtrack(i, path, total + candidates[i])
            path.pop()
            backtrack(i + 1, path, total)
        
        backtrack(0, [], 0)
        return res
