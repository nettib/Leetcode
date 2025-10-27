class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def backtrack(first_num, path):
            if len(path) == k:
                res.append(path[:])
                return

            for num in range(first_num, n + 1):
                path.append(num)
                backtrack(num + 1, path)
                path.pop()

        backtrack(1, [])
        return res