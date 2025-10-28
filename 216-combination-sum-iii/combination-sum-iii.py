class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []

        def backtrack(num, path, total):
            if total == n and len(path) == k:
                res.append(path[:])
                return 
            if len(path) == k or total > n or num > 9:
                return
            
            path.append(num)
            backtrack(num + 1, path, total + num)
            path.pop()
            backtrack(num + 1, path, total)
        
        backtrack(1, [], 0)
        return res
        
