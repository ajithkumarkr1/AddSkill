class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        flag = 0
        for i in range(len(matrix)):
            if matrix[i][0] <= target and target <= matrix[i][len(matrix[i])-1]:
                for j in range(len(matrix[i])):
                    if matrix[i][j] == target:
                        return True
                    elif i == len(matrix)-1 and j == len(matrix[i])-1:
                        return False
                    else:
                        flag = 1   
