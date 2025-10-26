from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # Step 1: Reverse the matrix vertically (top ↔ bottom)
        l, r = 0, len(matrix) - 1
        while l < r:
            matrix[l], matrix[r] = matrix[r], matrix[l]
            l += 1
            r -= 1

        # Step 2: Transpose the matrix (swap across diagonal)
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
