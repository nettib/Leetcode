class Solution:
    def minFlips(self, s: str) -> int:
        def get_swaps(arr, check):
            curr = 0
            for i in range(len(s)):
                curr += abs(arr[i] - check[i])

            swaps = curr

            for i in range(len(s), len(arr)):
                curr -= abs(arr[i - len(s)] - check[i - len(s)])
                curr += abs(arr[i] - check[i])
                swaps = min(swaps, curr)
            
            return swaps

        arr = list(s) * 2

        for i in range(len(arr)):
            arr[i] = int(arr[i])

        check1 = [0] * len(arr)
        check2 = [0] * len(arr)

        for i in range(len(check1)):
            if i % 2 != 0:
                check1[i] = 1
        
        for i in range(len(check2)):
            if i % 2 == 0:
                check2[i] = 1
        
        return min(get_swaps(arr, check1), get_swaps(arr, check2))
        
        

        


        
            