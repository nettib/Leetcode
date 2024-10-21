class Solution:
    def minOperations(self, logs: List[str]) -> int:
        count = 0
        for dir in logs:
            if dir[:len(dir)-1] == "..":
                if count != 0:
                    count-=1
            elif dir[:len(dir)-1] == ".":
                continue
            else:
                count+=1
        return count
            

        