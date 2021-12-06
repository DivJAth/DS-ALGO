# Given an m x n matrix, return all elements of the matrix in spiral order.

# Example 1:
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]

# Example 2:
# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        nr, nc = len(matrix), len(matrix[0])
        r = c = 0

        while len(result) < nr * nc:
            for col in range(c, nc-c):
                result.append(matrix[r][col])
            
            for row in range(r + 1, nr - r):
                result.append(matrix[row][nc-c-1])
            
            # Make sure we are now on a different row.
            if r != nr -1 - r:
                # Traverse from right to left.
                for col in range(nc - c - 2, c, -1):
                    result.append(matrix[nr-r-1][col])
           
            # Make sure we are now on a different column.
            if c != nc-c-1:
                # Traverse upwards.
                for row in range(nr-r-1, r, -1):
                    result.append(matrix[row][c])
            r+=1
            c+=1
        return result