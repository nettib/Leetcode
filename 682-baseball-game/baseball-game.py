class Solution:
    def calPoints(self, operations: List[str]) -> int:
        arr = []
        for i in range(len(operations)):
            if operations[i] == "C":
                arr.pop()
            elif operations[i] == "D":
                arr.append(arr[len(arr) - 1] * 2)
            elif operations[i] == "+":
                arr.append(arr[len(arr) - 1] + arr[len(arr) - 2])
            else:
                arr.append(int(operations[i]))

        return sum(arr)
         