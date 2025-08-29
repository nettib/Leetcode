class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        columns = len(matrix[0])
        l, r = 0, rows - 1

        while l <= r:
            m = l + ((r - l) // 2)
            if target >= matrix[m][0] and target <= matrix[m][columns - 1]:
                l1, r1 = 0, columns - 1
                while l1 <= r1:
                    m1 = l1 + ((r1 - l1) // 2)
                    if matrix[m][m1] == target:
                        return True
                    elif matrix[m][m1] < target:
                        l1 = m1 + 1
                    else:
                        r1 = m1 - 1
                return False
            elif target < matrix[m][0]:
                r = m - 1
            else:
                l = m + 1
         
        return False


            