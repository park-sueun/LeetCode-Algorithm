class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        rows, cols = len(matrix), len(matrix[0])
        zero_positions = []

        # Find the zero positions
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    zero_positions.append((i, j))

        # Set rows and columns to zero based on zero positions
        for i, j in zero_positions:
            for k in range(cols):
                matrix[i][k] = 0
            for k in range(rows):
                matrix[k][j] = 0