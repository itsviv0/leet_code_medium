class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        # transpose of the same matrix
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
              
        # reverse the rows of the matrix
        matrix = [row.reverse() for row in matrix]

# beats 53.65% runtime and 34.70% memory
# https://leetcode.com/problems/rotate-image/submissions/1325894921/
