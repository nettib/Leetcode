class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []

        def backtrack(first_num, path, total):
            if total == n and len(path) == k:
                res.append(path[:])
                return
            
            if total > n or len(path) == k:
                return

            for num in range(first_num, 10):
                path.append(num)
                backtrack(num + 1, path, total + num)
                path.pop()
            
        backtrack(1, [], 0)
        return res
            
        
