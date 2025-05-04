class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count = 0
        total = sum(arr[:k])
        avg = total / k
        if avg >= threshold:
            count += 1
        for i in range(k, len(arr)):
            total -= arr[i - k]
            total += arr[i]
            avg = total / k
            if avg >= threshold:
                count += 1
        return count



        


        